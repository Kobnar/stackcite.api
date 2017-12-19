import unittest

from stackcite.api import testing


class ValidatePasswordUnitTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def test_good_passwords_return_password(self):
        """'validate_password()' accepts good passwords
        """
        good_passwords = testing.data.valid_passwords()
        from ..passwords import validate_password
        for password in good_passwords:
            password_out = validate_password(password)
            self.assertEqual(password_out, password)

    def test_bad_passwords_return_none(self):
        """'validate_password()' rejects bad passwords
        """
        bad_passwords = testing.data.invalid_passwords()
        from ..passwords import validate_password
        for password in bad_passwords:
            password_out = validate_password(password)
            self.assertIsNone(password_out)

    def test_non_passwords_fail(self):
        """'validate_password()' returns 'None' if password is 'None'
        """
        non_passwords = ['', None, False]
        from ..passwords import validate_password
        for password in non_passwords:
            self.assertEqual(validate_password(password), None)
