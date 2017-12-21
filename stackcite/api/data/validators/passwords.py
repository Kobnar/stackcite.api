from stackcite.api import validators

from . import exceptions


class PasswordValidator(object):
    """
    A `mongoengine` style password validator. Raises :class:`.ValidationError`
    if the password provided is invalid.
    """
    def __init__(self, msg=None):
        if msg is None:
            self.msg = 'Invalid Password: {}'
        else:
            self.msg = msg

    def __call__(self, password):
        if not (isinstance(password, str) and validators.validate_password(password)):
            raise exceptions.ValidationError(self.msg.format(password))
