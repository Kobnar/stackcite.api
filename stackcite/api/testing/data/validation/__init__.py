import os
import json


_DIR = os.path.dirname(__file__)


def _load_json_file(filename):
    path = os.path.join(_DIR, filename)
    with open(path) as json_file:
        return json.load(json_file)


def valid_guids():
    return _load_json_file('guids.json')['valid_guids']


def invalid_guids():
    return _load_json_file('guids.json')['invalid_guids']


def valid_isbns():
    return _load_json_file('isbns.json')['valid_isbns']


def invalid_isbns():
    return _load_json_file('isbns.json')['invalid_isbns']


def valid_keys():
    return _load_json_file('keys.json')['valid_keys']


def invalid_keys():
    return _load_json_file('keys.json')['invalid_keys']


def valid_passwords():
    return _load_json_file('passwords.json')['valid_passwords']


def invalid_passwords():
    return _load_json_file('passwords.json')['invalid_passwords']


def valid_usernames():
    return _load_json_file('usernames.json')['valid_usernames']


def invalid_usernames():
    return _load_json_file('usernames.json')['invalid_usernames']
