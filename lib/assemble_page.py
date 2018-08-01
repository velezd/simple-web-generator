import os
from lib.settings import Settings as S


def assemble_page(html, menu, page_name=None):
    '''
    Inserts page html and menu html into web template

    :param html: page html
    :param menu: menu html
    :return: complete web page html
    '''

    with open(os.path.join('src', 'page.html'), 'r') as file:
        template = file.read()

    if page_name is not None:
        title = S().name + ' - ' + page_name
    else:
        title = S().name

    page = template.format(web_name=title,
                           menu=menu,
                           content=html,
                           copy=S().copyright,
                           path=S().web_root)

    return page

