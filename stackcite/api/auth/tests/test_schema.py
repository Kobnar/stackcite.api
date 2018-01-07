import unittest

from stackcite.api import testing


class SessionUserTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from .. import schema
        self.schema = schema.SessionUser()

    def test_id_required(self):
        """SessionUser.id is a required field
        """
        json_data = {'groups': ['users']}
        errors = self.schema.load(json_data).errors
        self.assertIn('id', errors)

    def test_groups_required(self):
        """SessionUser.groups is a required field
        """
        from bson import ObjectId
        json_data = {'id': str(ObjectId())}
        errors = self.schema.load(json_data).errors
        self.assertIn('groups', errors)

    def test_valid_groups_pass_validation(self):
        """SessionUser.groups passes validation for an valid users
        """
        from bson import ObjectId
        from .. import USERS, STAFF, ADMIN
        json_data = {
            'id': str(ObjectId()),
            'groups': [USERS, STAFF, ADMIN]}
        errors = self.schema.load(json_data).errors
        self.assertNotIn('groups', errors)

    def test_invalid_groups_fail_validation(self):
        """SessionUser.groups fails validation for an invalid user
        """
        from bson import ObjectId
        from .. import USERS
        json_data = {
            'id': str(ObjectId()),
            'groups': [USERS, 'cats']}
        errors = self.schema.load(json_data).errors
        self.assertIn('groups', errors)


class AuthTokenTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from .. import schema
        self.schema = schema.AuthToken()

    def test_load_key_required(self):
        """AuthToken.load() requires a 'key' field
        """
        from bson import ObjectId
        json_data = {
            'user': {
                'id': str(ObjectId()),
                'email': 'test@email.com',
                'groups': ['users']}}
        errors = self.schema.load(json_data).errors
        self.assertIn('key', errors)

    def test_load_invalid_keys_fail(self):
        """AuthToken.load() fails validation with an invalid key
        """
        from bson import ObjectId
        json_data = {
            'key': 'invalid_key',
            'user': {
                'id': str(ObjectId()),
                'email': 'test@email.com',
                'groups': ['users']}}
        errors = self.schema.load(json_data).errors
        self.assertIn('key', errors)

    def test_load_user_required(self):
        """AuthToken.load() requires a 'user' field
        """
        from .. import utils
        json_data = {'key': utils.gen_key()}
        errors = self.schema.load(json_data).errors
        self.assertIn('user', errors)

    def test_dump_user_with_id(self):
        """AuthToken.dump() includes a user with an ObjectId
        """
        from bson import ObjectId
        from datetime import datetime
        from .. import models, utils
        expected = str(ObjectId())
        user = models.SessionUser(id=expected, email='test@email.com', groups=['users'])
        auth_token = models.AuthToken(
            key=utils.gen_key(), user=user, issued=datetime.utcnow(), touched=datetime.utcnow())
        result = self.schema.dump(auth_token).data['user']['id']
        self.assertEqual(expected, result)

    def test_dump_user_with_groups(self):
        """AuthToken.dump() includes a user with a list of associated groups
        """
        from bson import ObjectId
        from datetime import datetime
        from .. import models, utils
        expected = ['groups']
        user_id = str(ObjectId())
        user = models.SessionUser(id=user_id, email='test@email.com', groups=expected)
        auth_token = models.AuthToken(
            key=utils.gen_key(), user=user, issued=datetime.utcnow(), touched=datetime.utcnow())
        result = self.schema.dump(auth_token).data['user']['groups']
        self.assertEqual(expected, result)
