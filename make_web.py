import os
from os.path import join
import shutil
from lib.make_blog import make_blog
from lib.settings import load_settings
from lib.misc import load_json
from lib.make_memu import make_menu_entry

"""
Directory structure:
    /lib
        make_blog
        make_page
    /output
        images
            thumbs
        downloads
        scripts
        style
        pages
            10-blog
                posts
                    gaming_in_qemu.html
                    skoda_forman.html
                blog.html
            20-about
                about.html
        index.html
    /src
        images
        downloads
        scripts
        style
        pages
            10-blog
                posts
                    2-gaming_in_qemu.html
                    1-skoda_forman.html
                blog.json
            20-about
                page.html
            30-github
                link.json
        page.html
        web_settings.json
            
"""


def clear_destination():
    """ Delete old assembled web """
    if os.path.exists('output'):
        shutil.rmtree('output')


def copy_static_files():
    """ Copy static files """
    if not os.path.exists('output'):
        os.mkdir('output')
    shutil.copytree(join('src', 'images'), join('output', 'images'))
    shutil.copytree(join('src', 'downloads'), join('output', 'downloads'))
    shutil.copytree(join('src', 'scripts'), join('output', 'scripts'))
    shutil.copytree(join('src', 'style'), join('output', 'style'))
    if not os.path.exists(join('output', 'images', 'thumbs')):
        os.mkdir(join('output', 'images', 'thumbs'))


if __name__ == "__main__":
    settings = load_settings()

    clear_destination()
    copy_static_files()

    # make pages
    os.mkdir(join('output', 'pages'))
    pages_path = join('src', 'pages')
    pages_list = os.listdir(pages_path)

    # make menu
    menu = ''
    for line in pages_list:
        if os.path.isfile(join(pages_path, line, 'blog.json')):
            page = load_json(join(pages_path, line, 'blog.json'))
            menu += make_menu_entry(page['name'], join('/', line))

        if os.path.isfile(join(pages_path, line, 'index.html')):
            pass

        if os.path.isfile(join(pages_path, line, 'link.json')):
            pass

    # make pages
    for line in pages_list:
        if os.path.isfile(join(pages_path, line, 'blog.json')):
            make_blog(join(pages_path, line), menu)
        if os.path.isfile(join(pages_path, line, 'page.html')):
            pass
        if os.path.isfile(join(pages_path, line, 'link.json')):
            pass

    # make index
    #with open(join('src', 'page.html'), 'r') as file:
    #    template = file.read()

    #with open(join('output', 'pages', settings['default_page'], 'blog.html'), 'r') as file:
    #    content = file.read()

    #web = template.format(web_name=settings['name'], menu="Menu", content=content, copy=settings['copyright'])

    #with open(join('output', 'index.html'), 'w') as file:
    #    file.write(web)