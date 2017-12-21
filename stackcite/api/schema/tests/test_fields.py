import unittest

from stackcite.api import testing

from marshmallow import Schema


class AuthTokenKeyFieldTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from .. import fields
        self.field = fields.AuthTokenKeyField()

    def test_deserialize_does_not_raise_exception_for_valid_string(self):
        """AuthTokenKeyField.deseriaize() does not raise ValidationError for a valid string
        """
        # A valid key contains 56 lowercase letters and numbers
        valid_key = '01dbaff045b7259cf57cb2c2abc637efeadad416eb17544b9784f598'
        from marshmallow import ValidationError
        try:
            self.field.deserialize(valid_key)
        except ValidationError as err:
            msg = 'Unexpected exception raised: {}'
            self.fail(msg.format(err))

    def test_deserialize_raises_exception_for_invalid_string(self):
        """AuthTokenKeyField.deserialize() raises ValidationError for an invalid string
        """
        invalid_key = 'invalid_key'
        from marshmallow import ValidationError
        with self.assertRaises(ValidationError):
            self.field.deserialize(invalid_key)


class _MockObj(object):
    def __init__(self, object_id=None, password=None):
        from bson import ObjectId
        self.id = object_id or ObjectId()
        self.password = password or 'T3stPa$$word'


class _MockSchema(Schema):
    from .. import fields
    id = fields.ObjectIdField()
    password = fields.PasswordField()


class ObjectIdFieldTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from ..fields import ObjectIdField
        self.field = ObjectIdField()

    def test_deserialize_accepts_valid_string(self):
        """ObjectIdField accepts a valid ObjectId string
        """
        from bson import ObjectId
        object_id = str(ObjectId())
        result = self.field.deserialize(object_id)
        self.assertEqual(object_id, result)

    def test_deserialize_raises_exception_for_invalid_string(self):
        """ObjectIdField raises exception for an invalid string
        """
        bad_id = 'bad_id'
        from marshmallow import ValidationError
        with self.assertRaises(ValidationError):
            self.field.deserialize(bad_id)

    def test_dump_returns_string(self):
        """ObjectIdField "dumps" to a string
        """
        obj = _MockObj()
        expected = str(obj.id)
        schema = _MockSchema()
        data, errors = schema.dump(obj)
        result = data['id']
        self.assertEqual(expected, result)


class PasswordFieldTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from ..fields import PasswordField
        self.field = PasswordField()

    def test_deserialize_accepts_valid_string(self):
        """PasswordField accepts a valid ObjectId string
        """
        valid_passwords = testing.data.validation.valid_passwords()
        for password in valid_passwords:
            result = self.field.deserialize(password)
            self.assertEqual(password, result)

    def test_deserialize_raises_exception_for_invalid_string(self):
        """PasswordField raises exception for an invalid string
        """
        invalid_passwords = testing.data.validation.invalid_passwords()
        from marshmallow import ValidationError
        for password in invalid_passwords:
            msg = 'Invalid password passed validation: {}'.format(password)
            with self.assertRaises(ValidationError, msg=msg):
                self.field.deserialize(password)

    def test_dump_returns_string(self):
        """PasswordField "dumps" to a string
        """
        expected = 'S0mePa$$word'
        obj = _MockObj(password=expected)
        schema = _MockSchema()
        data, errors = schema.dump(obj)
        result = data['password']
        self.assertEqual(expected, result)


class GroupFieldTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from ..fields import GroupField
        self.field = GroupField()

    def test_deserialize_accepts_valid_groups(self):
        """GroupField accepts all valid groups
        """
        from stackcite.api import auth
        for group in auth.GROUPS:
            result = self.field.deserialize(group)
            self.assertEqual(group, result)

    def test_deserialize_raises_exception_for_invalid_group(self):
        """GroupField raises exception for invalid group name
        """
        invalid_group = 'gods'
        msg = 'Invalid group passed validation: {}'.format(invalid_group)
        from marshmallow import ValidationError
        with self.assertRaises(ValidationError, msg=msg):
            self.field.deserialize(invalid_group)


class UsernameFieldTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from ..fields import UsernameField
        self.field = UsernameField()

    def test_deserialize_accepts_valid_string(self):
        """UsernameField accepts a valid ObjectId string
        """
        valid_usernames = testing.data.validation.valid_usernames()
        for username in valid_usernames:
            result = self.field.deserialize(username)
            self.assertEqual(username, result)

    def test_deserialize_raises_exception_for_invalid_string(self):
        """UsernameField raises exception for an invalid string
        """
        invalid_usernames = testing.data.validation.invalid_usernames()
        from marshmallow import ValidationError
        for username in invalid_usernames:
            msg = 'Invalid username passed validation: {}'.format(username)
            with self.assertRaises(ValidationError, msg=msg):
                self.field.deserialize(username)


class ListFieldTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from ..fields import ListField
        from marshmallow import fields
        self.field = ListField(fields.String)

    def test_deserialize_list_items(self):
        """ListSchema.deserialize() parses a list string into a python list
        """
        data = '12,cat,Michael Bolton'
        result = self.field.deserialize(data)
        expected = ['12', 'cat', 'Michael Bolton']
        self.assertEqual(expected, result)

    def test_deserialize_single_list_item(self):
        """ListSchema.deserialize() parses a single string into a list w/ one item
        """
        data = 'Michael Bolton'
        result = self.field.deserialize(data)
        expected = ['Michael Bolton']
        self.assertEqual(expected, result)

    def test_deserialize_empty_string(self):
        """ListSchema.deserialize() parses an empty string into an empty list
        """
        data = ''
        result = self.field.deserialize(data)
        expected = []
        self.assertEqual(expected, result)

    def test_deserialize_none(self):
        """ListSchema.deserialize() raises exception for None
        """
        from marshmallow import ValidationError
        with self.assertRaises(ValidationError):
            self.field.deserialize(None)


class FieldsFieldTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from ..fields import FieldsListField
        self.fields = FieldsListField()

    def test_deserialize_list_items(self):
        """FieldsSchema.deserialize() parses a list string into a python list
        """
        data = '12,cat,Michael Bolton'
        result = self.fields.deserialize(data)
        expected = ['12', 'cat', 'Michael Bolton']
        self.assertEqual(expected, result)

    def test_deserialize_single_list_item(self):
        """FieldsSchema.deserialize() parses a single string into a list w/ one item
        """
        data = 'Michael Bolton'
        result = self.fields.deserialize(data)
        expected = ['Michael Bolton']
        self.assertEqual(expected, result)

    def test_deserialize_empty_string(self):
        """FieldsSchema.deserialize() parses an empty string into an empty list
        """
        data = ''
        result = self.fields.deserialize(data)
        expected = []
        self.assertEqual(expected, result)

    def test_deserialize_none(self):
        """ListSchema.deserialize() raises exception for None
        """
        from marshmallow import ValidationError
        with self.assertRaises(ValidationError):
            self.fields.deserialize(None)

    def test_deserialize_converts_subfield_notation(self):
        """FieldsSchema.deserialize() converts underscores to dots for subfields
        """
        data = 'id,name__full,birth,pets__dogs__indoor'
        expected = ['id', 'name.full', 'birth', 'pets.dogs.indoor']
        result = self.fields.deserialize(data)
        self.assertEqual(expected, result)