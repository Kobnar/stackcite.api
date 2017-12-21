import unittest

from stackcite.api import testing


class KeyValidatorUnitTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from ..keys import KeyValidator
        self.validator = KeyValidator()

    def test_valid_keys_pass(self):
        """KeyValidator does nothing for valid keys
        """
        good_keys = testing.data.validation.valid_keys()
        from ..exceptions import ValidationError
        for uri in good_keys:
            try:
                self.validator(uri)
            except ValidationError as err:
                self.fail(err)

    def test_invalid_keys_fail(self):
        """KeyValidator raises exception for invalid keys
        """
        bad_keys = testing.data.validation.invalid_keys()
        from ..exceptions import ValidationError
        for uri in bad_keys:
            with self.assertRaises(ValidationError):
                self.validator(uri)

    def test_non_string_raises_exception(self):
        """KeyValidator raises exceptions for non-strings
        """
        bad_vals = [None, 123, 1.23, True, False]
        from ..exceptions import ValidationError
        for val in bad_vals:
            with self.assertRaises(ValidationError):
                self.validator(val)

    def test_default_msg(self):
        """KeyValidator sets a default message
        """
        bad_key = 'bad key'
        from ..exceptions import ValidationError
        try:
            self.validator(bad_key)
        except ValidationError as err:
            self.assertIsNotNone(err.message)
            self.assertIsInstance(err.message, str)

    def test_custom_msg(self):
        """KeyValidator can set a custom message
        """
        msg = 'Custom message.'
        from ..keys import KeyValidator
        validator = KeyValidator(msg)
        from ..exceptions import ValidationError
        bad_key = 'bad key'
        try:
            validator(bad_key)
        except ValidationError as err:
            self.assertEqual(err.message, msg)
