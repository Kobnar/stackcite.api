from bson import ObjectId
from bson.errors import InvalidId

from . import exceptions


class ObjectIdValidator(object):
    """
    A `mongoengine` style :class:`bson.ObjectId` validator. Raises
    :class:`.ValidationError` if the string provided is not a valid
    :class:`bson.ObjectId`.
    """
    def __init__(self, msg=None):
        if msg is None:
            # TODO: format errors
            self.msg = 'Invalid ObjectId: {}'
        else:
            self.msg = msg

    def __call__(self, object_id):
        if not (isinstance(object_id, str) and validate_objectid(object_id)):
            raise exceptions.ValidationError(self.msg.format(object_id))
