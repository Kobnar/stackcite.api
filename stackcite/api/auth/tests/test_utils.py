import unittest

from stackcite.api import testing


class GenKeyTestCase(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def test_returns_56_char_key(self):
        from .. import utils
        result = utils.gen_key()
        self.assertEqual(56, len(result))


class GetUserTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from pyramid.testing import DummyRequest
        self.request = DummyRequest()

    def test_returns_session_user_with_id(self):
        """get_user() returns a SessionUser with a valid ID
        """
        from bson import ObjectId
        import json
        from stackcite.api import auth
        expected = str(ObjectId())
        data = {'id': expected, 'groups': auth.GROUPS}
        self.request.authorization = ('user', json.dumps(data))
        from .. import utils
        result = utils.get_user(self.request).id
        self.assertEqual(expected, result)

    def test_returns_session_user_with_groups(self):
        """get_user() returns a SessionUser with a valid list of groups
        """
        from bson import ObjectId
        import json
        from stackcite.api import auth
        expected = auth.GROUPS
        data = {'id': str(ObjectId()), 'groups': auth.GROUPS}
        self.request.authorization = ('user', json.dumps(data))
        from .. import utils
        result = utils.get_user(self.request).groups
        self.assertEqual(expected, result)

    def test_unset_authorization_header_returns_none(self):
        """get_user() returns None if authorization header is not set
        """
        from .. import utils
        self.request.authorization = ('', '')
        result = utils.get_user(self.request)
        self.assertEqual(None, result)

    def test_invalid_objectid_returns_none(self):
        """get_user() returns None if user ID is invalid
        """
        import json
        from stackcite.api import auth
        data = {'id': 'invalid_id', 'groups': auth.GROUPS}
        self.request.authorization = ('user', json.dumps(data))
        from .. import utils
        result = utils.get_user(self.request)
        self.assertEqual(None, result)

    def test_invalid_groups_returns_none(self):
        """get_user() returns None if user groups are invalid
        """
        from bson import ObjectId
        import json
        data = {'id': str(ObjectId()), 'groups': ['cats']}
        self.request.authorization = ('user', json.dumps(data))
        from .. import utils
        result = utils.get_user(self.request)
        self.assertEqual(None, result)
