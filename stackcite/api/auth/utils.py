import os
import hashlib
import json

from stackcite.api.validators.oids import validate_objectid
from stackcite.api.validators.groups import validate_group

from . import models


def gen_key():
    """
    Generates a cryptographic key used for API Tokens and account confirmation.
    """
    return hashlib.sha224(os.urandom(128)).hexdigest()


def get_user(request):
    """
    Returns a user based on an API key located in the request header.
    """

    auth_type, auth_data = request.authorization
    if auth_type.lower() == 'user':
        auth_data = json.loads(auth_data)
        valid_id = validate_objectid(auth_data['id'])
        valid_groups = [g for g in auth_data['groups'] if validate_group(g)] == auth_data['groups']
        if valid_id and valid_groups:
            return models.SessionUser(**auth_data)


def get_groups(user_id, request):
    """
    Returns a list of groups for the current user if `user_id` matches the `id`
    field of the current request's :class:`stackcite.User`.
    """

    return request.user.groups if request.user.id == user_id else []
