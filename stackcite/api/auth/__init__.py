from stackcite.api.config import auth as _auth

from .utils import gen_key, get_user
from .policies import AuthTokenAuthenticationPolicy


GROUP_CHOICES = _auth.GROUP_CHOICES
GROUPS = _auth.GROUPS
USERS = _auth.USERS
STAFF = _auth.STAFF
ADMIN = _auth.ADMIN
