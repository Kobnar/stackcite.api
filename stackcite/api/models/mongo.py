import mongoengine

from . import utils


class IEmbeddedDocument(mongoengine.EmbeddedDocument, utils.IDeserializable):
    """
    A common interface for all embedded documents.
    """

    meta = {'abstract': True}


class IDocument(mongoengine.Document, utils.IDeserializable):
    """
    A common interface for all documents.
    """

    meta = {'abstract': True}
