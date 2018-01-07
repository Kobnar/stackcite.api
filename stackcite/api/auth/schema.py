from marshmallow import Schema, fields as mm_fields

from stackcite.api.schema import fields as api_fields

from . import GROUPS


class SessionUser(Schema):

    id = api_fields.ObjectIdField(required=True)
    groups = mm_fields.List(
        mm_fields.String(validate=lambda g: g in GROUPS),
        required=True)
