"""
Command-based device communication
"""

import asyncio
from binascii import hexlify, unhexlify
from collections import defaultdict
from concurrent.futures import CancelledError
from contextlib import suppress
from datetime import datetime, timedelta

from aiohttp import web
from brewblox_devcon_spark import commands, communication
from brewblox_service import brewblox_logger, features

LOGGER = brewblox_logger(__name__)

# Spark protocol is to echo the request in the response
# To prevent decoding ambiguity, a non-hexadecimal character separates the request and response
RESPONSE_SEPARATOR = '|'

# As requests are matched on request code + arguments, they may cause bloating in the matcher
# This would happen if the same request is made often with different arguments
#
# There is no functional danger here - we just need to curb this equivalent of a memory leak
QUEUE_VALID_DURATION = timedelta(minutes=15)
CLEANUP_INTERVAL = timedelta(seconds=60)

# There is no strict guarantee that when ClientA and ClientB make the same request at the same time,
# they get the exact response they triggered.
# We only guarantee that they get a response that matches their request + arguments.
#
# This leaves the error condition where ClientA makes a request, but never retrieves its response.
# When ClientB makes the same request an hour later, the ClientA response is still in the queue.
#
# RESPONSE_VALID_DURATION sets how long ago the response may have been received by the matcher.
# Example:
#   t=0   -> request made, and sent to controller
#   t=100 -> response received from controller, stored in queue
#   t=110 -> response retrieved from queue
#
# In this scenario, the response will only be t=10 old, as it was stored at t=100
RESPONSE_VALID_DURATION = timedelta(seconds=5)
REQUEST_TIMEOUT = timedelta(seconds=5)


def setup(app: web.Application):
    features.add(app, SparkCommander(app))


def get_commander(app: web.Application):
    return features.get(app, SparkCommander)


class TimestampedQueue():

    def __init__(self):
        self._queue = asyncio.Queue()
        self._timestamp = datetime.utcnow()

    @property
    def queue(self):
        self._timestamp = datetime.utcnow()
        return self._queue

    @property
    def fresh(self):
        return self._timestamp + QUEUE_VALID_DURATION > datetime.utcnow()


class TimestampedResponse():

    def __init__(self, content):
        self._content = content
        self._timestamp = datetime.utcnow()

    def __str__(self):
        return f'{self._content} @ {self._timestamp}'

    @property
    def content(self):
        return self._content

    @property
    def fresh(self):
        return self._timestamp + RESPONSE_VALID_DURATION > datetime.utcnow()


class SparkCommander(features.ServiceFeature):

    def __init__(self, app: web.Application=None):
        super().__init__(app)

        self._requests = defaultdict(TimestampedQueue)
        self._conduit: communication.SparkConduit = None
        self._cleanup_task: asyncio.Task = None

    def __str__(self):
        return f'<{type(self).__name__} for {self._conduit}>'

    async def startup(self, app: web.Application):
        await self.shutdown()

        self._conduit = communication.get_conduit(app)
        self._conduit.add_data_callback(self._process_response)
        self._cleanup_task = app.loop.create_task(self._cleanup())

    async def shutdown(self, *_):
        with suppress(AttributeError):
            self._conduit.remove_data_callback(self._process_response)

        with suppress(Exception):
            self._cleanup_task.cancel()
            await self._cleanup_task

        self._conduit = None
        self._cleanup_task = None

    async def _cleanup(self):
        while True:
            try:

                await asyncio.sleep(CLEANUP_INTERVAL.seconds)
                stale = [k for k, queue in self._requests.items()
                         if not queue.fresh]

                if stale:
                    LOGGER.debug(f'Cleaning stale queues: {stale}')

                for key in stale:
                    del self._requests[key]

            except CancelledError:
                LOGGER.debug(f'{self} cleanup task shutdown')
                break

            except Exception as ex:
                LOGGER.warn(f'{self} cleanup task error: {ex}')

    async def _process_response(self, conduit, msg: str):
        try:
            raw_request, raw_response = [
                unhexlify(part)
                for part in msg.replace(' ', '').split(RESPONSE_SEPARATOR)]

            # Match the request queue
            # key is the encoded request
            queue = self._requests[raw_request].queue
            await queue.put(TimestampedResponse(raw_response))

        except Exception as ex:
            LOGGER.error(f'Response error in {self} : {ex}', exc_info=True)

    async def execute(self, command: commands.Command) -> dict:
        encoded_request = command.encoded_request
        assert await self._conduit.write_encoded(hexlify(encoded_request))

        while True:
            # Wait for a request resolution (matched by request)
            # Request will be resolved with a timestamped response
            queue = self._requests[encoded_request].queue
            response = await asyncio.wait_for(queue.get(), timeout=REQUEST_TIMEOUT.seconds)

            if not response.fresh:
                LOGGER.warn(f'Discarding stale response: {response}')
                continue

            # Create new command to avoid changing the 'command' argument
            response_cmd = type(command)().from_encoded(encoded_request, response.content)
            decoded = response_cmd.decoded_response

            # If the call failed, its response will be an exception
            # We can raise it here
            if isinstance(decoded, BaseException):
                raise decoded

            return decoded
