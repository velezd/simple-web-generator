import os
from os.path import join
import shutil
from lib.make_misc import make_misc
from lib.make_blog import make_blog
from lib.make_single_page import make_single_page
from lib.settings import Settings as S
from lib.make_memu import make_menu

# TODO: Add options for meta tag description or something


def clear_destination():
    ''' Delete old output directory '''
    if os.path.exists('output'):
        print('Removing old output')
        shutil.rmtree('output')


def copy_static_files():
    ''' Copy static files '''
    if not os.path.exists('output'):
        os.mkdir('output')

    if not os.path.exists(join('output', 'misc')):
        os.mkdir(join('output', 'misc'))

    shutil.copytree(join('src', 'images'), join('output', 'images'))
    shutil.copytree(join('src', 'downloads'), join('output', 'downloads'))
    shutil.copytree(join('src', 'scripts'), join('output', 'scripts'))
    shutil.copytree(join('src', 'style'), join('output', 'style'))

    if not os.path.exists(join('output', 'images', 'thumbs')):
        os.mkdir(join('output', 'images', 'thumbs'))


if __name__ == "__main__":
    # Init settings
    S()

    clear_destination()
    copy_static_files()

    pages_path = join('src', 'pages')
    # sort by number that should be before the name
    try:
        pages_list = sorted(os.listdir(pages_path), key=lambda x: int(x.split('-')[0]))
    except ValueError:
        print('ERROR: All pages directories must start with number. Example: 25-page_name')
        exit(1)

    # make menu
    menu = make_menu(pages_list, pages_path)

    # make misc pages
    make_misc(menu)

    # make pages
    os.mkdir(join('output', 'pages'))
    for line in pages_list:
        if os.path.isfile(join(pages_path, line, 'blog.json')):
            make_blog(join(pages_path, line), menu)
        if os.path.isfile(join(pages_path, line, 'index.html')):
            make_single_page(join(pages_path, line), menu)

    # make index
    default_page_path = join('output', 'pages', S().default_page, 'index.html')
    if os.path.exists(default_page_path):
        shutil.copy(default_page_path, join('output', 'index.html'))
    else:
        print('ERROR: Default page doesn\'t exists.')
        exit(1)
