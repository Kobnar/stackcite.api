from bson import ObjectId
from bson.errors import InvalidId


def validate_objectid(object_id):
    """
    A simple :class:`bson.ObjectId` validator.
    :param object_id: The ObjectId to be checked
    :return: A fully qualified ObjectId or `None` if unsuccessful
    """
    if not isinstance(object_id, str):
        return None

    try:
        object_id = ObjectId(object_id)
        return object_id
    except InvalidId:
        return None
