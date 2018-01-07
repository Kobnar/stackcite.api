import unittest


class MockDocumentSchemaTests(unittest.TestCase):

    def make_schema(self, method=None):
        from .. import MockDocumentSchema
        schema = MockDocumentSchema()
        schema.method = method
        return schema


class CreateMockDocumentSchemaTests(MockDocumentSchemaTests):

    def setUp(self):
        self.schema = self.make_schema(method='POST')

    def test_name_required(self):
        """MockDocumentSchema validation requires 'name' field for POST
        """
        data = {'number': 42}
        result, errors = self.schema.load(data)
        self.assertIn('name', errors.keys())


class RetrieveMockDocumentSchemaTests(MockDocumentSchemaTests):

    def setUp(self):
        self.schema = self.make_schema(method='GET')


class UpdateMockDocumentSchemaTests(MockDocumentSchemaTests):

    def setUp(self):
        self.schema = self.make_schema(method='PUT')

    def test_unknown_field_dropped(self):
        """MockDocumentSchema validation drops an unknown field for PUT
        """
        data = {
            'name': 'Document',
            'unknown': 'field'}
        result, errors = self.schema.load(data)
        self.assertNotIn('unknown', result.keys())


class MockDocumentSchemaIntegrationTests(MockDocumentSchemaTests):

    def test_schema_loads_data(self):
        """MockDocumentSchema loads all MockDocument data
        """
        data = {
            'name': 'Test Document',
            'number': 42,
            'fact': True}
        schm = self.make_schema()
        doc = schm.load(data).data
        for key, expected in data.items():
            result = doc[key]
            self.assertEqual(expected, result)

    def test_schema_dumps_data(self):
        """MockDocumentSchema dumps a MockDocument object
        """
        expected = {
            'name': 'Test Document',
            'number': 42,
            'fact': True}
        from .. import models
        doc = models.MockDocument(**expected)
        schm = self.make_schema()
        data = schm.dump(doc).data
        for key, expected in data.items():
            result = getattr(doc, key)
            self.assertEqual(expected, result)
