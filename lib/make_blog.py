import os
from os.path import join
from lib.path import src_to_static
from lib.make_html import make_html
from lib.make_image import make_thumbnail
from lib.assemble_page import assemble_page
from lib.settings import Settings as S


def make_blog(path, menu):
    '''
    Creates blog index pages and processes blog posts

    :param path: path to blog
    :param menu: menu html
    :return: nothing
    '''

    # prepare new path
    new_path = src_to_static(path)

    # create new blog directories
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    if not os.path.exists(join(new_path, 'posts')):
        os.mkdir(join(new_path, 'posts'))

    # create blog index
    # TODO: Maybe add pagination
    posts_list = get_posts_info(path)
    html = generate_blog_index(posts_list)
    html = assemble_page(html, menu)

    with open(join(new_path, 'index.html'), 'w') as file:
        file.write(html)

    posts = os.listdir(join(path, 'posts'))

    # create posts
    for post in posts:
        new_post_path = join(path, 'posts', post)
        if os.path.exists(src_to_static(new_post_path)):
            print('ERROR: Duplicit post name: ' + post)
        else:
            make_html(new_post_path, menu)


def generate_blog_index(posts_list):
    '''
    Creates html for list of blog posts

    :param posts_list: list of blog posts
    :return: html string
    '''

    html = ''
    for post in posts_list:
        if not post['image']:
            image = '<img>'
        else:
            tmp = join(S().web_root, 'images', 'thumbs', make_thumbnail(post['image']))
            image = '<img src="{}">'.format(tmp)

        if not post['date']:
            date = ''
        else:
            date ='<span class="blog_date">{date}</span><br>'.format(date=post['date'])

        tmp = '''<div class="blogitem">
                     {image}
                     <a href="{link}"><h3>{name}</h3></a>
                     {date}
                     <div class="blog_text">{text}</div>
                 </div>\n'''

        html += tmp.format(image=image, link=post['link'], name=post['name'], date=date, text=post['text'])

    return html


def get_posts_info(path):
    '''
    Reads information from posts html file

    :param path: Path to blog posts
    :return: list of dictionaries with post name, date, image, text and link
    '''

    try:
        posts = sorted(os.listdir(join(path, 'posts')), reverse=True, key=lambda x: int(x.split('-')[0]))
    except ValueError:
        print('ERROR: All blog posts must start with number. Example: 130-post_name')
        exit(1)

    posts_list = []

    for post in posts:
        # Get info for creating blog index
        pname = None
        pdate = None
        pimage = None
        ptext = None

        plink = src_to_static(join(S().web_root, 'pages', os.path.split(path)[1], 'posts', post))

        with open(join(path, 'posts', post), 'r') as file:
            for line in file:
                if line.startswith('@name'):
                    pname = line.split(':')[1].rstrip()
                if line.startswith('@date'):
                    pdate = line.split(':')[1].rstrip()
                if line.startswith('@post_image'):
                    pimage = line.split(':')[1].rstrip()
                if line.startswith('@post_text'):
                    ptext = line.split(':')[1].rstrip()
                if '<p>' in line and not ptext:
                    # TODO: Find better way to automaticaly select text - probably good enough
                    if line.strip() == '<p>':
                        ptext = file.readline().replace('<p>', '').replace('</p>', '')
                    else:
                        ptext = line.replace('<p>', '').replace('</p>', '')

                    break

        if not pname:
            print('WARNING: Blog post must have a @name: ' + post)

        posts_list.append({'name': pname,
                           'date': pdate,
                           'image': pimage,
                           'text': ptext,
                           'link': plink})

    return posts_list
