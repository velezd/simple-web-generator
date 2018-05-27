import json
import os
import shutil


def clear_destination():
    """ Delete old assembled web """
    if os.path.exists('static'):
        shutil.rmtree('static')


def copy_static_files():
    """ Copy static files """
    shutil.copytree(os.path.join('src', 'static'), os.path.join('static'))


def load_settings():
    """
    Load web settings from json file.

    :return: dict
    """
    try:
        with open(os.path.join('src', 'web_settings.json'), 'r') as file:
            return json.loads(file.read())
    except IOError:
        print('Can\'t load web settings')


if __name__ == "__main__":
    settings = load_settings()

    clear_destination()
    copy_static_files()

    # make index
    with open(os.path.join('src', 'page.html'), 'r') as file:
        template = file.read()

    with open(os.path.join('src', 'pages', settings['default_page'], 'index.html'), 'r') as file:
        content = file.read()

    web = template.format(web_name=settings['name'], menu="Menu", content=content, copy=settings['copyright'])

    with open(os.path.join('static', 'index.html'), 'w') as file:
        file.write(web)