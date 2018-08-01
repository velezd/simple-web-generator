import shutil
import os
from os.path import join
from lib.path import src_to_static
from lib.make_html import make_html


def make_misc(menu):
    '''
    Creates misc directory copies static files and processes html files

    :param menu: menu html
    :return: nothing
    '''

    # make misc pages
    misc_path = join('src', 'misc')
    new_misc_path = src_to_static(misc_path)

    # Create misc directory if doesn't exist
    if not os.path.exists(new_misc_path):
        os.mkdir(new_misc_path)

    # go through misc files
    misc_list = os.listdir(misc_path)
    for line in misc_list:
        # Make html or copy file
        if os.path.splitext(line)[1] == '.html':
            make_html(join(misc_path, line), menu)
        else:
            shutil.copy(join(misc_path, line), src_to_static(join(misc_path, line)))
