from .exceptions import ValidationError


class ISBNValidator(object):
    """
    A `mongoengine` style ISBN validator. Raises :class:`.ValidationError` if
    the ISBN provided is invalid. Automatically detects the difference between
    ISBN-10 and ISBN-13 formatted strings.
    """
    def __init__(self, msg=None):
        if msg is None:
            self.msg = 'Invalid ISBN: {}'
        else:
            self.msg = msg

    def __call__(self, isbn):
        if not (isinstance(isbn, str) and validate_isbn(isbn)):
            raise ValidationError(self.msg.format(isbn))
