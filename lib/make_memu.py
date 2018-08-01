import os
from lib.misc import load_json
from lib.path import src_to_static
from os.path import join
from lib.settings import Settings as S


def make_menu(pages_list, pages_path):
    '''
    Creates menu html from list of pages and path to pages

    :param pages_list: list of pages  ex: ['10-blog', '15-github', '20-about']
    :param pages_path: path to pages usually "src/pages"
    :return: menu html <li><a>page1</a></li>\n<li><a>page2</a></li>...
    '''

    menu = ''
    for line in pages_list:
        # MENU: make blogs
        if os.path.isfile(join(pages_path, line, 'blog.json')):
            page = load_json(join(pages_path, line, 'blog.json'))
            menu += make_menu_entry(page['name'], join(S().web_root, 'pages', line))

        # MENU: make single pages
        if os.path.isfile(join(pages_path, line, 'index.html')):
            with open(join(pages_path, line, 'index.html'), 'r') as file:
                for line2 in file:
                    if line2.startswith('@name'):
                        name = line2.split(':')[1].rstrip()
                        if name:
                            menu += make_menu_entry(name, join(S().web_root, 'pages', line))
                        else:
                            print('ERROR: Empty name: ' + line)
                        break

        # MENU: make links
        if os.path.isfile(join(pages_path, line, 'link.json')):
            page = load_json(join(pages_path, line, 'link.json'))
            menu += make_menu_entry_link(page['name'], page['link'])

    return menu


def make_menu_entry(name, path):
    link = join(src_to_static(path), 'index.html')
    template = '    <li><a href="{link}">{name}</a></li>\n'
    return template.format(link=link, name=name)


def make_menu_entry_link(name, link):
    template = '    <li><a href="{link}">{name}</a></li>\n'
    return template.format(link=link, name=name)
