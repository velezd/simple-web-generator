from PIL import Image
import os


def make_thumbnail(filename):
    """ Create image thumbnails """
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
        image.thumbnail(size, Image.ANTIALIAS)

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
