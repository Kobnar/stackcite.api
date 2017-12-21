import os

from stackcite.api import utils


_DIR = os.path.dirname(__file__)


def valid_guids():
    return utils.load_json_file(_DIR, 'guids.json')['valid_guids']


def invalid_guids():
    return utils.load_json_file(_DIR, 'guids.json')['invalid_guids']


def valid_isbn10s():
    return utils.load_json_file(_DIR, 'isbns.json')['valid_isbn10s']


def valid_isbn13s():
    return utils.load_json_file(_DIR, 'isbns.json')['valid_isbn13s']


def invalid_isbns():
    return utils.load_json_file(_DIR, 'isbns.json')['invalid_isbns']


def valid_keys():
    return utils.load_json_file(_DIR, 'keys.json')['valid_keys']


def invalid_keys():
    return utils.load_json_file(_DIR, 'keys.json')['invalid_keys']


def valid_passwords():
    return utils.load_json_file(_DIR, 'passwords.json')['valid_passwords']


def invalid_passwords():
    return utils.load_json_file(_DIR, 'passwords.json')['invalid_passwords']


def valid_usernames():
    return utils.load_json_file(_DIR, 'usernames.json')['valid_usernames']


def invalid_usernames():
    return utils.load_json_file(_DIR, 'usernames.json')['invalid_usernames']
