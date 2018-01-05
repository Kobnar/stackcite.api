import unittest

from stackcite.api import testing


class StackciteErrorTestCase(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def test_default_message(self):
        from .. import base
        expected = ''
        error = base.StackciteError()
        result = error.message
        self.assertEqual(expected, result)

    def test_custom_message(self):
        from .. import base
        expected = 'Something went wrong'
        error = base.StackciteError(expected)
        result = error.message
        self.assertEqual(expected, result)

    def test_str_returns_default_message(self):
        from .. import base
        expected = 'StackciteError'
        error = base.StackciteError()
        result = str(error)
        self.assertEqual(expected, result)

    def test_str_returns_custom_message(self):
        from .. import base
        message = 'Something went wrong'
        expected = 'StackciteError: {}'.format(message)
        error = base.StackciteError(message)
        result = str(error)
        self.assertEqual(expected, result)
