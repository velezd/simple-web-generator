from lib.path import src_to_static
from lib.make_image import make_gallery, make_big_image
from lib.make_download import make_download
from lib.assemble_page import assemble_page


def make_html(path, menu):
    '''
    Processes html files (images, titles, gallery, downloads) inserts the html into template via assemble_page
    and saves the new html file to the corresponding output directory

    :param path: path to the html file
    :param menu: menu html
    :return: Nothing
    '''

    with open(path, 'r') as file:
        name = None
        html = '<article>\n'
        gallery = False
        gallery_added = False
        downloads = False
        count = 0

        for line in file:
            count += 1
            if line.startswith('@') and len(line.split(':')) < 2:
                print('ERROR: Wrong line command: ' + line)
                exit(1)

            if line.startswith('@header_image'):
                temp = '''<div class="post_header" style="background: linear-gradient(to bottom, 
                rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0) 59%, rgba(255, 255, 255, 1) 100%), 
                url('/images/{img}') center center no-repeat; background-size: cover;"></div>\n'''
                html += temp.format(img=format(line.split(':')[1].rstrip()))
                if count != 1:
                    print('WARNING: Header image must be on first line')

            elif line.startswith('@name'):
                name = line.split(':')[1].rstrip()
                html += '<h2>{}</h2>\n'.format(name)

            elif line.startswith('@date'):
                html += '<span class="post_date">{date}</span>'.format(date=line.split(':')[1].rstrip())

            elif line.startswith('@bigimage'):
                gallery_added = True
                html += make_big_image(line.split(':'))

            elif line.startswith('@medimage'):
                gallery_added = True
                html += make_big_image(line.split(':'), True)

            elif line.startswith('@image'):
                # Start gallery
                if not gallery:
                    html += '<div class="gallery">\n'
                    gallery = True
                    gallery_added = True

                # Generate html and create thumbnail
                html += make_gallery(line.split(':'))

            elif gallery:
                # End gallery
                html += '</div>\n'
                gallery = False

            elif line.startswith('@download'):
                # Start downloads
                if not downloads:
                    html += '<div class="download">'
                    downloads = True

                # Generate html, get size, assign icon
                html += make_download(line)

            elif downloads:
                # End downloads
                html += '</div>\n'
                downloads = False

            # Remove any special tags that are not processed at this point
            elif line.startswith('@'):
                pass

            else:
                html += line

    if gallery_added:
        # Add gallery js if gallery was added
        html += '<script>$(\'.gallery a\').simpleLightbox();</script>'

    html += '\n</article>\n'

    html = assemble_page(html, menu, name)

    new_path = src_to_static(path)

    with open(new_path, 'w') as file:
        file.write(html)
