import os
import json


def load_json_file(directory, filename):
    path = os.path.join(directory, filename)
    with open(path) as json_file:
        return json.load(json_file)
