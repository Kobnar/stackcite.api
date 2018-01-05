import mongoengine


class IEmbeddedDocument(mongoengine.EmbeddedDocument):
    """
    A common interface for all embedded documents.
    """

    meta = {'abstract': True}


class IDocument(mongoengine.Document):
    """
    A common interface for all documents.
    """

    meta = {'abstract': True}
