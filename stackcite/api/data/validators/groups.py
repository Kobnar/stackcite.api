from stackcite.api import validators

from . import exceptions


class GroupValidator(object):
    """
    A `mongoengine` style group validator. Raises :class:`.ValidationError`
    if the group provided is invalid.
    """
    def __init__(self, msg=None):
        if msg is None:
            self.msg = 'Invalid group: {}'
        else:
            self.msg = msg

    def __call__(self, group):
        if not (isinstance(group, str) and validators.validate_group(group)):
            raise exceptions.ValidationError(self.msg.format(group))
