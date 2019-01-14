import json
import time
from contextlib import contextmanager

import requests


@contextmanager
def timed(description):
    start = time.time()
    yield
    end = time.time()
    print(description, end - start)


def main():
    with open('spark_blocks.json') as f:
        blocks = json.load(f)

    with timed('delete initial'):
        resp = requests.delete('http://localhost/spark/objects')
        print(resp, resp.status_code == 200 or resp.text)

    with timed('create normal'):
        resp = requests.post('http://localhost/spark/reset_objects', json=blocks)
        print(resp, resp.status_code == 200 or resp.text)

    clone_block = next(block for block in blocks if block['id'] == 'profile-1')
    for i in range(100):
        b = clone_block.copy()
        b['id'] = f'pid-copy-{i}'
        blocks.append(b)

    with timed('create big'):
        resp = requests.post('http://localhost/spark/reset_objects', json=blocks)
        print(resp, resp.status_code == 200 or resp.text)

    with timed('delete big'):
        resp = requests.delete('http://localhost/spark/objects')
        print(resp, resp.status_code == 200 or resp.text)


if __name__ == '__main__':
    main()
