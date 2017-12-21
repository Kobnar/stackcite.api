from stackcite.api import validators

from . import exceptions


class KeyValidator(object):
    """
    A `mongoengine` style key validator. Raises :class:`.ValidationError`
    if the key provided is invalid.
    """
    def __init__(self, msg=None):
        if msg is None:
            self.msg = 'Invalid key: {}'
        else:
            self.msg = msg

    def __call__(self, key):
        if not (isinstance(key, str) and validators.validate_key(key)):
            raise exceptions.ValidationError(self.msg.format(key))
