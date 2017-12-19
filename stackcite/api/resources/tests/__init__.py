from stackcite.api import resources as _resources
from stackcite.api import testing as _testing


class MockSerializableResource(_resources.SerializableResource):

    _SCHEMA = _testing.mock.MockDocumentSchema
