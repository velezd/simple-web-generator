import os
from lib.settings import load_settings


def assemble_page(html, path_to_root, menu):
    settings = load_settings()

    with open(os.path.join('src', 'page.html'), 'r') as file:
        template = file.read()

    page = template.format(web_name=settings['name'], menu=menu, content=html, copy=settings['copyright'], path=path_to_root)

    return page

