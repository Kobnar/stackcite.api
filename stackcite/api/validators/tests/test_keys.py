import unittest

from stackcite.api import testing


class ValidateKeyUnitTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def test_good_keys_return_key(self):
        """'validate_key()' accepts good keys
        """
        good_keys = testing.data.validation.valid_keys()
        from ..keys import validate_key
        for key in good_keys:
            key_out = validate_key(key)
            self.assertEqual(key_out, key)

    def test_bad_keys_return_none(self):
        """'validate_key()' rejects bad keys
        """
        bad_keys = testing.data.validation.invalid_keys()
        from ..keys import validate_key
        for key in bad_keys:
            key_out = validate_key(key)
            self.assertIsNone(key_out)

    def test_non_keys_fail(self):
        """'validate_key()' returns 'None' if key is 'None'
        """
        non_keys = ['', None, False]
        from ..keys import validate_key
        for key in non_keys:
            self.assertEqual(validate_key(key), None)
