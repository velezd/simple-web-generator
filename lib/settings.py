import json
from os.path import join


def load_settings():
    """
    Load web settings from json file.

    :return: dict
    """
    try:
        with open(join('src', 'web_settings.json'), 'r') as file:
            return json.loads(file.read())
    except IOError:
        print('Can\'t load web settings')