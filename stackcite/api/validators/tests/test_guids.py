import unittest

from stackcite.api import testing


class ValidateObjectIdTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def test_valid_ids_return_object_id_instance(self):
        """validate_objectid() returns an instance of ObjectId with a valid string
        """
        good_object_ids = testing.data.validation.valid_guids()
        from ..oids import validate_objectid
        from bson import ObjectId
        for id_str in good_object_ids:
            result = validate_objectid(id_str)
            self.assertIsInstance(result, ObjectId)

    def test_valid_ids_return_same_object_id(self):
        """validate_objectid() returns an instance of ObjectId with the same valid string
        """
        good_object_ids = testing.data.validation.valid_guids()
        from ..oids import validate_objectid
        from bson import ObjectId
        for id_str in good_object_ids:
            result = validate_objectid(id_str)
            expected = ObjectId(id_str)
            self.assertEqual(result, expected)

    def test_invalid_ids_return_none(self):
        """validate_objectid() returns `None` for invalid ObjectId strings
        """
        bad_object_ids = testing.data.validation.invalid_guids()
        from ..oids import validate_objectid
        for id_str in bad_object_ids:
            result = validate_objectid(id_str)
            self.assertIsNone(result)

    def test_invalid_type_returns_none(self):
        """validate_isbn() returns `None` for invalid types
        """
        from ..oids import validate_objectid
        invalid_types = (12, [1, 2], True)
        for oid in invalid_types:
            result = validate_objectid(oid)
            self.assertIsNone(result)
