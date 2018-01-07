class SessionUser(object):

    def __init__(self, id, email, groups):
        self.id = id
        self.email = email
        self.groups = groups


class AuthToken(object):

    def __init__(self, key, user, issued, touched):
        self.key = key
        self.user = user
        self.issued = issued
        self.touched = touched
