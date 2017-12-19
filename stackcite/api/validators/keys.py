import re


def validate_key(key):
    """
    Validates a given API key. Returns the initial `key` value if it is
    valid, or `None`.

    :param key: An API key string

    This validator enforces the following requirements:

    * Must be 56 characters long
    * May not include special characters
    * May not include a space (including newline characters)
    """
    if not isinstance(key, str):
        return None
    else:
        white_list = re.compile(r"^[\S]{56}$")
        spec_chars = re.escape(r"`~!@#$%^&*()+-=[]{};':\"<>,./?\|")
        black_list = re.compile(r"[" + spec_chars + r"\s\n]")
        if not white_list.search(key) or black_list.search(key):
            return None
    return key
