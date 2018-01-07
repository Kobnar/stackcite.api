import mongoengine

from stackcite.api import models


class MockDocument(models.IDocument):
    """
    Provides a very basic models model to perform integration tests with MongoDB.
    This class can be sub-classed for specific test cases that require
    additional fields or methods.

    :cvar name: A unique string value.
    :cvar number: An arbitrary integer value.
    :cvar fact: An arbitrary boolean value.
    """

    name = mongoengine.StringField(required=True, unique=True)
    number = mongoengine.IntField()
    fact = mongoengine.BooleanField()

    meta = {
        'allow_inheritance': True,
        'indexes': [
            {
                'fields': ['$name'],
                'cls': False
            }
        ]
    }
