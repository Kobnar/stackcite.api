import re


def validate_username(username):
    """
    Validates a given username. Returns the initial `username` value if it is
    valid, or `None`.

    :param username: A username string

    This validator enforces the following requirements:

    * 3-32 characters long
    * May include letters
    * May include numbers
    * May include underscores
    * No whitespaces (including newline characters)
    * No special characters (except for '_')
    """
    if not isinstance(username, str):
        return None
    else:
        white_list = re.compile(r"^[\S]{3,32}$")
        spec_chars = re.escape(r"`~!@#$%^&*()+-=[]{};':\"<>,./?\|")
        black_list = re.compile(r"[" + spec_chars + r"\s\n]")
        if not white_list.search(username) or black_list.search(username):
            return None
    return username
