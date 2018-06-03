#! /usr/bin/python36
import os
from os.path import join
import sys
from lib.path import src_to_static, path_split
from lib.make_html import make_html


# TODO: blog generation will be here


def make_blog(path, menu):
    # prepare new path
    new_path = src_to_static(path)
    # Path to root of web from posts
    path_to_root = '..{}'.format(os.sep) * (len(path_split(path)))

    # create new blog directories
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    if not os.path.exists(join(new_path, 'posts')):
        os.mkdir(join(new_path, 'posts'))

    posts = os.listdir(join(path, 'posts'))

    for post in posts:
        # Create post directory
        new_post_path = join(path, 'posts', post)
        if not os.path.exists(new_post_path):
            os.mkdir(new_post_path)
        make_html(new_post_path, path_to_root, menu)

    html = 'test'
    with open(join(new_path, 'index.html'), 'w') as file:
        file.write(html)
