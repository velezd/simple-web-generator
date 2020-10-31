from os import path
from lib.settings import Settings as S


def make_icon(name):
    return '<img class="icon" src="%s.svg">' % path.join(S().web_root, 'style', 'icons', name)