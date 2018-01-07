class IDeserializable(object):
    """
    Provides a simple interface for deserializing data through an object's
    interface.
    """

    def deserialize(self, data):
        """
        Recursively deserializes data onto a tree of nested objects.

        :param data: A dictionary of values.
        """
        for key, value in data.items():
            try:
                getattr(self, key).deserialize(value)
            except AttributeError:
                setattr(self, key, value)
