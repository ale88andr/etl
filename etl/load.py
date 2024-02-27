""" Module with finctions for loading data """

import json
import requests


ES_HOST = '127.0.0.1'
ES_PORT = '9200'
ES_IDX = 'movies'


def bulk_prepare(data):
    """ Preparing data for bulk load """
    result = []
    for item in data:
        result.append(json.dumps({
            'index': {
                '_index': 'movies',
                '_id': item.get('id')
            }
        }))
        result.append(json.dumps(item))

    return '\n'.join(result) + '\n'


def load(data: list):
    """ Function loading data """
    data = bulk_prepare(data)
    response = requests.put(
        f'http://{ES_HOST}:{ES_PORT}/{ES_IDX}/_bulk?filter_path=items.*.error',
        data=data,
        headers={'Content-Type': 'application/x-ndjson'},
        timeout=10
    )

    print(response.json())
