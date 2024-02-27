""" Module with finctions for loading data """

import json
import requests


def load(data: list):
    """ Function loading data """
    requests.post('address:port/uri', data=json.dumps(data))
