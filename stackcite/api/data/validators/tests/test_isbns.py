import unittest

from stackcite.data import testing


class ISBNValidatorTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def setUp(self):
        from ..isbns import ISBNValidator
        self.validator = ISBNValidator()

    def test_valid_isbn10s_pass(self):
        """ISBNDataValidator does nothing for valid ISBN-10s
        """
        valid_isbn_10s = testing.data.valid_isbn10s()
        from ..exceptions import ValidationError
        for isbn in valid_isbn_10s:
            try:
                self.validator(isbn)
            except ValidationError as err:
                self.fail(err)

    def test_valid_isbn13s_pass(self):
        """ISBNDataValidator does nothing for valid ISBN-13s
        """
        valid_isbn13s = testing.data.valid_isbn13s()
        from ..exceptions import ValidationError
        for isbn in valid_isbn13s:
            try:
                self.validator(isbn)
            except ValidationError as err:
                self.fail(err)

    def test_invalid_isbns_fail(self):
        """ISBNDataValidator raises exception for invalid ISBNs
        """
        invalid_isbns = testing.data.invalid_isbns()
        from ..exceptions import ValidationError
        for isbn in invalid_isbns:
            with self.assertRaises(ValidationError):
                self.validator(isbn)

    def test_non_string_raises_exception(self):
        """ISBNDataValidator raises exceptions for non-strings
        """
        bad_vals = [None, 123, 1.23, True, False]
        from ..exceptions import ValidationError
        for val in bad_vals:
            with self.assertRaises(ValidationError):
                self.validator(val)

    def test_default_msg(self):
        """ISBNDataValidator sets a default message
        """
        bad_isbn = 'bad ISBN'
        from ..exceptions import ValidationError
        try:
            self.validator(bad_isbn)
        except ValidationError as err:
            self.assertIsNotNone(err.message)
            self.assertIsInstance(err.message, str)

    def test_custom_msg(self):
        """ISBNDataValidator can set a custom message
        """
        msg = 'Custom message.'
        from ..isbns import ISBNValidator
        validator = ISBNValidator(msg)
        from ..exceptions import ValidationError
        bad_isbn = 'bad ISBN'
        try:
            validator(bad_isbn)
        except ValidationError as err:
            self.assertEqual(err.message, msg)
