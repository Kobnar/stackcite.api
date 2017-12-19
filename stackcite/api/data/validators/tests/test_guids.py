import unittest

from stackcite.data import testing


class ObjectIdValidatorTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from ..oids import ObjectIdValidator
        self.validator = ObjectIdValidator()

    def test_valid_ids_pass(self):
        """ObjectIdDataValidator does nothing for valid passwords
        """
        good_object_ids = testing.data.valid_object_ids()
        from ..exceptions import ValidationError
        for id_str in good_object_ids:
            try:
                self.validator(id_str)
            except ValidationError as err:
                self.fail(err)

    def test_invalid_ids_fail(self):
        """ObjectIdDataValidator raises exception for invalid passwords
        """
        bad_object_ids = testing.data.invalid_object_ids()
        from ..exceptions import ValidationError
        for id_str in bad_object_ids:
            with self.assertRaises(ValidationError):
                self.validator(id_str)

    def test_non_string_raises_exception(self):
        """ObjectIdDataValidator raises exceptions for non-strings
        """
        bad_vals = [None, 123, 1.23, True, False]
        from ..exceptions import ValidationError
        for val in bad_vals:
            with self.assertRaises(ValidationError):
                self.validator(val)

    def test_default_msg(self):
        """ObjectIdDataValidator sets a default message
        """
        bad_guid = 'bad GUID'
        from ..exceptions import ValidationError
        try:
            self.validator(bad_guid)
        except ValidationError as err:
            self.assertIsNotNone(err.message)
            self.assertIsInstance(err.message, str)

    def test_custom_msg(self):
        """ObjectIdDataValidator can set a custom message
        """
        msg = 'Custom message.'
        from ..oids import ObjectIdValidator
        validator = ObjectIdValidator(msg)
        from ..exceptions import ValidationError
        bad_guid = 'bad GUID'
        try:
            validator(bad_guid)
        except ValidationError as err:
            self.assertEqual(err.message, msg)
