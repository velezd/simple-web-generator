import json
from os.path import join


def singleton(cls):
    '''
    Decorator for creating one instance of class accessible from anywhere without additional initializing

    :param cls: Class
    :return: function returning instance
    '''

    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class Settings():
    def __init__(self):
        ''' Load and store web settings from json file. '''
        self.name = ''
        self.default_page = ''
        self.copyright = ''
        self.web_root = ''
        self.blogposts_on_page = ''

        try:
            with open(join('src', 'web_settings.json'), 'r') as file:
                temp = json.loads(file.read())
                self.name = temp['name']
                self.default_page = temp['default_page']
                self.copyright = temp['copyright']
                self.web_root = temp['web_root']
                self.blogposts_on_page = temp['blogposts_on_page']
        except IOError:
            print('Can\'t load web settings')
