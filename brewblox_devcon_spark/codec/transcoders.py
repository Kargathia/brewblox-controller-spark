"""
Object-specific transcoders
"""


from abc import ABC, abstractclassmethod, abstractmethod
from collections import defaultdict
from typing import Dict, Iterable, List, Union

from brewblox_service import brewblox_logger
from google.protobuf import json_format
from google.protobuf.message import Message

from . import pb2
from .modifiers import Modifier
from .opts import CodecOpts, ProtoEnumOpt

ObjType_ = Union[int, str]
Decoded_ = dict
Encoded_ = bytes

LOGGER = brewblox_logger(__name__)


class Transcoder(ABC):

    def __init__(self, mods: Modifier):
        self.mod = mods

    @abstractclassmethod
    def type_int(cls) -> int:
        pass  # pragma: no cover

    @abstractclassmethod
    def type_str(cls) -> str:
        pass  # pragma: no cover

    @classmethod
    def type_impl(cls) -> List[int]:
        return []

    @abstractmethod
    def encode(self, values: Decoded_, opts: CodecOpts) -> Encoded_:
        pass  # pragma: no cover

    @abstractmethod
    def decode(self, encoded: Encoded_, opts: CodecOpts) -> Decoded_:
        pass  # pragma: no cover

    @classmethod
    def get(cls, obj_type: ObjType_, mods: Modifier) -> 'Transcoder':
        try:
            return _TYPE_MAPPING[obj_type](mods)
        except KeyError:
            raise KeyError(f'No codec found for object type [{obj_type}]')

    @classmethod
    def type_tree(cls, mods: Modifier) -> Dict[str, List[str]]:
        impl_tree = defaultdict(list)
        for trc in _TRANSCODERS:
            name = trc.type_str()
            for intf in [Transcoder.get(t, mods).type_str() for t in trc.type_impl()]:
                impl_tree[intf].append(name)
        return impl_tree


class BlockInterfaceTranscoder(Transcoder):

    @classmethod
    def type_int(cls) -> int:
        return cls._ENUM_VAL

    @classmethod
    def type_str(cls) -> str:
        return pb2.brewblox_pb2.BrewBloxTypes.BlockType.Name(cls._ENUM_VAL)

    def encode(self, values: Decoded_, _) -> Encoded_:
        return b'\x00'

    def decode(self, values: Encoded_, _) -> Decoded_:
        return dict()


def interface_factory(value: int) -> BlockInterfaceTranscoder:
    name = f'{pb2.brewblox_pb2.BrewBloxTypes.BlockType.Name(value)}TranscoderStub'
    return type(name, (BlockInterfaceTranscoder, ), {'_ENUM_VAL': value})


class InactiveObjectTranscoder(Transcoder):

    @classmethod
    def type_int(cls) -> int:
        return 65535

    @classmethod
    def type_str(cls) -> str:
        return 'InactiveObject'

    def encode(self, values: Decoded_, _) -> Encoded_:
        type_id = values['actualType']
        encoded = Transcoder.get(type_id, self.mod).type_int().to_bytes(2, 'little')
        return encoded

    def decode(self, encoded: Encoded_, _) -> Decoded_:
        type_id = int.from_bytes(encoded, 'little')
        return {'actualType': Transcoder.get(type_id, self.mod).type_str()}


class DeprecatedObjectTranscoder(Transcoder):

    @classmethod
    def type_int(cls) -> int:
        return 65533

    @classmethod
    def type_str(cls) -> str:
        return 'DeprecatedObject'

    def encode(self, values: Decoded_, _) -> Encoded_:
        actual_id = values['actualId']
        encoded = actual_id.to_bytes(2, 'little')
        return encoded

    def decode(self, encoded: Encoded_, _) -> Decoded_:
        actual_id = int.from_bytes(encoded, 'little')
        return {'actualId': actual_id}


class GroupsTranscoder(Transcoder):

    @classmethod
    def type_int(cls) -> int:
        return 65534

    @classmethod
    def type_str(cls) -> str:
        return 'Groups'

    def encode(self, values: Decoded_, _) -> Encoded_:
        active = self.mod.pack_bit_flags(values.get('active', []))
        return active.to_bytes(1, 'little')

    def decode(self, encoded: Encoded_, _) -> Decoded_:
        active = self.mod.unpack_bit_flags(int.from_bytes(encoded, 'little'))
        return {'active': active}


class ProtobufTranscoder(Transcoder):

    @classmethod
    def type_int(cls) -> int:
        return cls._MESSAGE.DESCRIPTOR.GetOptions().Extensions[pb2.brewblox_pb2.brewblox_msg].objtype

    @classmethod
    def type_str(cls) -> str:
        return cls._MESSAGE.__name__

    @classmethod
    def type_impl(cls) -> List[int]:
        return cls._MESSAGE.DESCRIPTOR.GetOptions().Extensions[pb2.brewblox_pb2.brewblox_msg].impl

    def create_message(self) -> Message:
        return self.__class__._MESSAGE()

    def encode(self, values: Decoded_, _) -> Encoded_:
        # LOGGER.debug(f'encoding {values} to {self.__class__._MESSAGE}')
        obj = json_format.ParseDict(values, self.create_message())
        data = obj.SerializeToString()
        return data + b'\x00'  # Include null terminator

    def decode(self, encoded: Encoded_, opts: CodecOpts) -> Decoded_:
        # Remove null terminator
        encoded = encoded[:-1]
        int_enum = opts.enums == ProtoEnumOpt.INT

        obj = self.create_message()
        obj.ParseFromString(encoded)
        decoded = json_format.MessageToDict(
            message=obj,
            preserving_proto_field_name=True,
            including_default_value_fields=True,
            use_integers_for_enums=int_enum,
        )
        # LOGGER.debug(f'decoded {self.__class__._MESSAGE} to {decoded}')
        return decoded


class OptionsTranscoder(ProtobufTranscoder):

    def encode(self, values: Decoded_, opts: CodecOpts) -> Encoded_:
        self.mod.encode_options(self.create_message(), values, opts)
        return super().encode(values, opts)

    def decode(self, encoded: Encoded_, opts: CodecOpts) -> Decoded_:
        decoded = super().decode(encoded, opts)
        self.mod.decode_options(self.create_message(), decoded, opts)
        return decoded


class EdgeCaseTranscoder(OptionsTranscoder):
    _MESSAGE = pb2.EdgeCase_pb2.EdgeCase

    @classmethod
    def type_int(cls) -> int:
        return 9001

    @classmethod
    def type_str(cls) -> str:
        return 'EdgeCase'


def options_type_factory(message):
    name = f'{message.__name__}Transcoder'
    return type(name, (OptionsTranscoder, ), {'_MESSAGE': message})


def _generate_mapping(vals: Iterable[Transcoder]):
    for trc in vals:
        yield trc.type_int(), trc
        yield trc.type_str(), trc


_TRANSCODERS = [
    # Raw system objects
    InactiveObjectTranscoder,
    DeprecatedObjectTranscoder,
    GroupsTranscoder,

    # Interface objects
    # Actual implementations will override this later
    *[
        interface_factory(v)
        for v in pb2.brewblox_pb2.BrewBloxTypes.BlockType.values()
    ],

    # Protobuf objects
    *[
        options_type_factory(msg)
        for msg in [
            pb2.ActuatorAnalogMock_pb2.ActuatorAnalogMock,
            pb2.ActuatorLogic_pb2.ActuatorLogic,
            pb2.ActuatorOffset_pb2.ActuatorOffset,
            pb2.ActuatorPwm_pb2.ActuatorPwm,
            pb2.Balancer_pb2.Balancer,
            pb2.DigitalActuator_pb2.DigitalActuator,
            pb2.DisplaySettings_pb2.DisplaySettings,
            pb2.DS2408_pb2.DS2408,
            pb2.DS2413_pb2.DS2413,
            pb2.MockPins_pb2.MockPins,
            pb2.MotorValve_pb2.MotorValve,
            pb2.Mutex_pb2.Mutex,
            pb2.OneWireBus_pb2.OneWireBus,
            pb2.Pid_pb2.Pid,
            pb2.SetpointProfile_pb2.SetpointProfile,
            pb2.SetpointSensorPair_pb2.SetpointSensorPair,
            pb2.Spark2Pins_pb2.Spark2Pins,
            pb2.Spark3Pins_pb2.Spark3Pins,
            pb2.SysInfo_pb2.SysInfo,
            pb2.TempSensorCombi_pb2.TempSensorCombi,
            pb2.TempSensorMock_pb2.TempSensorMock,
            pb2.TempSensorOneWire_pb2.TempSensorOneWire,
            pb2.Ticks_pb2.Ticks,
            pb2.TouchSettings_pb2.TouchSettings,
            pb2.WiFiSettings_pb2.WiFiSettings,
        ]
    ],

    # Debugging object
    EdgeCaseTranscoder,
]

_TYPE_MAPPING = {k: v for k, v in _generate_mapping(_TRANSCODERS)}
