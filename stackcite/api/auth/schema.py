from marshmallow import Schema, fields as mm_fields

from stackcite.api.schema import fields as api_fields

from . import GROUPS


class SessionUser(Schema):

    id = api_fields.ObjectIdField(required=True)
    groups = mm_fields.List(
        mm_fields.String(validate=lambda g: g in GROUPS),
        required=True)


class AuthToken(Schema):

    key = api_fields.AuthTokenKeyField(required=True)
    user = mm_fields.Nested(SessionUser, required=True)
    issued = mm_fields.DateTime()
    touched = mm_fields.DateTime()
