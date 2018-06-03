from lib.path import src_to_static
from os.path import join


def make_menu_entry(name, path):
    link = join(src_to_static(path), 'index.html')
    template = '    <li><a href="{link}">{name}</a></li>\n'
    return template.format(link=link, name=name)
