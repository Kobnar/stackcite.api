import unittest

from stackcite.api import testing


class ValidateGroupUnitTests(unittest.TestCase):

    layer = testing.layers.UnitTestLayer

    def test_users_group_returns_group(self):
        """'validate_group()' accepts users group
        """
        from ..groups import validate_group
        result = validate_group('users')
        self.assertIsNotNone(result)

    def test_staff_group_returns_group(self):
        """'validate_group()' accepts staff group
        """
        from ..groups import validate_group
        result = validate_group('staff')
        self.assertIsNotNone(result)

    def test_admin_group_returns_group(self):
        """'validate_group()' accepts admin group
        """
        from ..groups import validate_group
        result = validate_group('admin')
        self.assertIsNotNone(result)

    def test_invalid_group_returns_none(self):
        """'validate_group()' rejects invalid group"""
        from ..groups import validate_group
        result = validate_group('invalid_group')
        self.assertIsNone(result)
