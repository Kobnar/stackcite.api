import unittest

from stackcite.api import testing


class ValidateUsernameUnitTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def test_good_usernames_return_username(self):
        """'validate_username()' accepts good usernames
        """
        good_usernames = testing.data.validation.valid_usernames()
        from ..usernames import validate_username
        for username in good_usernames:
            username_out = validate_username(username)
            self.assertEqual(username_out, username)

    def test_bad_usernames_return_none(self):
        """'validate_username()' rejects bad usernames
        """
        bad_usernames = testing.data.validation.invalid_usernames()
        from ..usernames import validate_username
        for username in bad_usernames:
            username_out = validate_username(username)
            self.assertIsNone(username_out)

    def test_non_usernames_fail(self):
        """'validate_username()' returns 'None' if username is 'None'
        """
        non_usernames = ['', None, False]
        from ..usernames import validate_username
        for username in non_usernames:
            self.assertEqual(validate_username(username), None)
