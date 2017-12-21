import os

from stackcite.api import utils


_DIR = os.path.dirname(__file__)


GROUP_CHOICES = utils.load_json_file(_DIR, 'groups.json')
GROUPS = [k for k, v in GROUP_CHOICES]
USERS, STAFF, ADMIN = GROUPS
