import json


def load_json(path):
    '''
    Loads json file

    :param path: path to json file
    :return: dictionary
    '''

    try:
        with open(path, 'r') as file:
            return json.loads(file.read())
    except IOError:
        print('ERROR: Can\'t load file: ' + path)
        exit(1)
    except ValueError:
        print('ERROR: Wrong values in file: ' + path)
        exit(1)
