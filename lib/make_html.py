import os
from lib.path import src_to_static
from lib.make_thumbnail import make_thumbnail
from lib.assemble_page import assemble_page


def make_html(path, path_to_root, menu):
    with open(path, 'r') as file:
        html = '<article>\n'
        gallery = False
        gallery_added = False
        for line in file:
            if line.startswith('@name'):
                html += '<h2>{}</h2>\n'.format(line.split(':')[1].rstrip())
            elif line.startswith('@date'):
                print(line.split(':')[1].rstrip())
            elif line.startswith('@image'):
                # start new gallery
                if not gallery:
                    html += '<div class="gallery">\n'
                    gallery = True
                    gallery_added = True

                # get image info
                data = line.split(':')
                image_filename = data[1].rstrip()
                image_title = ''
                if len(data) == 3:
                    image_title = data[2].rstrip()

                # Create thumbnail
                thumb_name = make_thumbnail(image_filename)

                # Image html
                image_html = '   <a href="{image}" title="{title}"><img src="{thumb}"></a>\n'

                html += image_html.format(image=os.path.join(path_to_root, 'images', image_filename),
                                          title=image_title,
                                          thumb=os.path.join(path_to_root, 'images', 'thumbs', thumb_name))
            elif gallery:
                # end gallery
                html += '</div>\n'
                gallery = False
            else:
                html += line

        if gallery_added:
            html += '<script>$(\'.gallery a\').simpleLightbox();</script>'
    html += '</article>\n'

    html = assemble_page(html, path_to_root, menu)

    new_path = src_to_static(path)
    print(new_path)
    with open(new_path, 'w') as file:
        file.write(html)




