import os
from PIL import Image
from lib.settings import Settings as S

#TODO: Add side image

def make_gallery(data):
    '''
    Make image - must be put inside gallery div with class "gallery"

    :param data: list - ['@image', filename, image_title/caption]
    :return: image html
    '''
    image_filename = data[1].rstrip()
    image_title = ''
    if len(data) == 3:
        image_title = data[2].rstrip()

    # Create thumbnail
    thumb_name = make_thumbnail(image_filename)

    # Image html
    image_html = '   <a href="{image}" title="{title}"><img src="{thumb}" alt="{title}"></a>\n'

    return image_html.format(image=os.path.join(S().web_root, 'images', image_filename),
                             title=image_title,
                             thumb=os.path.join(S().web_root, 'images', 'thumbs', thumb_name))


def make_big_image(data, medium=False):
    '''
    Make big or medium image

    :param data: list - ['@medimage', filename, image_title/caption]
    :param medium: True/False create medium image instead of big
    :return: image html
    '''

    image_filename = data[1].rstrip()
    image_title = ''
    if len(data) == 3:
        image_title = data[2].rstrip()

    if medium:
        style = 'medium_image'
    else:
        style = 'big_image'

    # Image html
    image_html = '''
    <div class="gallery">
        <a href="{image}" title="{title}">
            <img class="{style}" src="{image}" alt="{title}">
        </a>
        <br>
        <span class="image_caption">{title}</span>
    </div><br>\n'''

    return image_html.format(image=os.path.join(S().web_root, 'images', image_filename), title=image_title, style=style)


def make_thumbnail(filename):
    '''
    Create image thumbnails

    :param filename: image filename without path
    :return: Thumbnail path
    '''

    image_path = os.path.join('src', 'images', filename)
    thumb_path = os.path.join('output', 'images', 'thumbs', filename)
    thumb_path = os.path.splitext(thumb_path)[0] + '.jpg'

    try:
        # Load image
        image = Image.open(image_path)
        # Convert to RGB
        image = image.convert('RGB')

        # Scale down
        if image.height > image.width:
            size = 150, 150*10
        else:
            size = 150*10, 150
        image.thumbnail(size)

        # Crop to 1:1 ratio
        if image.height > image.width:
            remove = (image.height - 150) / 2
            crop = (0, remove, 150, image.height - remove)
        else:
            remove = (image.width - 150) / 2
            crop = (remove, 0, image.width - remove, 150)
        image = image.crop(crop)

        # Save image
        image.save(thumb_path, 'JPEG')

        return os.path.split(thumb_path)[1]

    except IOError:
        print('ERROR: Can\'t process image: ' + image_path)
        return ''
