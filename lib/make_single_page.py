import os
from lib.path import src_to_static
from lib.make_html import make_html


def make_single_page(path, menu):
    '''
    Creates single page

    :param path: path to the page
    :param menu: menu html
    :return:
    '''

    directory = src_to_static(path)
    if not os.path.exists(directory):
        os.mkdir(directory)

    make_html(os.path.join(path, 'index.html'), menu)
