from stackcite.api.config import auth


def validate_group(group):
    """
    Validates a given group. Returns the initial ``group`` string if
    the group is good and ``None`` if the group fails validation.

    :param str group: A group name string.
    """
    if group in auth.GROUPS:
        return group
