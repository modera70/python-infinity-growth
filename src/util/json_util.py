import json


def json_to_dict(filepath):
    with open(filepath) as json_file:
        return json.load(json_file)
