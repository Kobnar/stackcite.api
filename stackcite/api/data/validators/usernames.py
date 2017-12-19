from . import exceptions


class UsernameValidator(object):
    """
    A `mongoengine` style username validator. Raises :class:`.ValidationError`
    if the username provided is invalid.
    """
    def __init__(self, msg=None):
        if msg is None:
            self.msg = 'Invalid username: {}'
        else:
            self.msg = msg

    def __call__(self, username):
        if not (isinstance(username, str) and validate_username(username)):
            raise exceptions.ValidationError(self.msg.format(username))
