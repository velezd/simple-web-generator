import json


def load_json(path):
    try:
        with open(path, 'r') as file:
            return json.loads(file.read())
    except IOError:
        print('ERROR: Can\'t load file: ' + path)
    except ValueError:
        print('ERROR: Wrong values in file: ' + path)
