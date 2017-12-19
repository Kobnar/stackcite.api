import unittest

from stackcite.data import testing


class PasswordValidatorUnitTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from ..passwords import PasswordValidator
        self.validator = PasswordValidator()

    def test_valid_passwords_pass(self):
        """PasswordDataValidator does nothing for valid passwords
        """
        good_passwords = testing.data.valid_passwords()
        from ..exceptions import ValidationError
        for uri in good_passwords:
            try:
                self.validator(uri)
            except ValidationError as err:
                self.fail(err)

    def test_invalid_passwords_fail(self):
        """PasswordDataValidator raises exception for invalid passwords
        """
        bad_passwords = testing.data.invalid_passwords()
        from ..exceptions import ValidationError
        for uri in bad_passwords:
            with self.assertRaises(ValidationError):
                self.validator(uri)

    def test_non_string_raises_exception(self):
        """PasswordDataValidator raises exceptions for non-strings
        """
        bad_vals = [None, 123, 1.23, True, False]
        from ..exceptions import ValidationError
        for val in bad_vals:
            with self.assertRaises(ValidationError):
                self.validator(val)

    def test_default_msg(self):
        """PasswordDataValidator sets a default message
        """
        bad_password = 'bad password'
        from ..exceptions import ValidationError
        try:
            self.validator(bad_password)
        except ValidationError as err:
            self.assertIsNotNone(err.message)
            self.assertIsInstance(err.message, str)

    def test_custom_msg(self):
        """PasswordDataValidator can set a custom message
        """
        msg = 'Custom message.'
        from ..passwords import PasswordValidator
        validator = PasswordValidator(msg)
        from ..exceptions import ValidationError
        bad_password = 'bad password'
        try:
            validator(bad_password)
        except ValidationError as err:
            self.assertEqual(err.message, msg)
