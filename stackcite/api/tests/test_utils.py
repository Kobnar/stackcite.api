import unittest

from stackcite.api import testing


class LoadJSONFileTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def test_loads_json_data(self):
        """load_json_data() loads data from a json file
        """
        import os
        directory = os.path.dirname(__file__)
        from .. import utils
        data = utils.load_json_file(directory, 'test_utils.json')
        expected = 'testPassed'
        result = data['testUtils']
        self.assertEqual(expected, result)
