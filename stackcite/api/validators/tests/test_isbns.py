import unittest

from stackcite.api import testing


class ValidateISBNTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def test_valid_isbn_13s_return_isbn(self):
        """valdiate_isbn() returns valid ISBN-13s
        """
        valid_isbn13s = testing.data.validation.valid_isbn13s()
        from ..isbns import validate_isbn
        for isbn in valid_isbn13s:
            expected = isbn.replace('-', '')
            result = validate_isbn(isbn)
            self.assertEqual(expected, result)

    def test_valid_isbn_10s_return_isbn(self):
        """valdiate_isbn() returns valid ISBN-10s
        """
        valid_isbn_10s = testing.data.validation.valid_isbn10s()
        from ..isbns import validate_isbn
        for isbn in valid_isbn_10s:
            expected = isbn.replace('-', '')
            result = validate_isbn(isbn)
            self.assertEqual(expected, result)

    def test_invalid_isbns_return_none(self):
        """validate_isbn() returns `None` if ISBN is invalid
        """
        invalid_isbns = testing.data.validation.invalid_isbns()
        from ..isbns import validate_isbn
        for isbn in invalid_isbns:
            result = validate_isbn(isbn)
            self.assertIsNone(result)
