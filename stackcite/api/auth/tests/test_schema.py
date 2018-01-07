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
