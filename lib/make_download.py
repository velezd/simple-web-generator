import os
from os.path import join
from lib.misc import load_json
from lib.settings import Settings as S


def make_download(data):
    '''
    Creates html for file download

    :param data: string @download:filename:license_name(optional):license_path(optional)
    :return: download html
    '''

    # Get filename and license if exists
    filename = data.split(':')[1].rstrip()
    if len(data.split(':')) >= 3:
        license = data.split(':', 3)[2:]
    else:
        license = None

    # Load mimetypes
    mimetypes = load_json(join('lib', 'mimetypes.json'))
    licenses = load_json(join('lib', 'licenses.json'))
    new_download_path = join('output', 'downloads', filename)

    # Get file extension
    if len(os.path.splitext(filename)) != 1:
        extension = os.path.splitext(filename)[1].lstrip('.')
    else:
        extension = None

    # Get extension icon name
    if extension in mimetypes.keys():
        icon_name = mimetypes[extension]
    else:
        icon_name = mimetypes['unknown']

    # Get license
    if license:
        license_html = '<br>License: <a href="{link}" target="_blank">{name}</a>'
        # Check if license is defined and use it
        license_found = False
        for key in licenses.keys():
            if key.lower() == license[0].rstrip().lower():
                license_html = license_html.format(link=licenses[key], name=key)
                license_found = True
                break

        # Custom license or no license
        if not license_found:
            # Link to license defined
            if len(license) > 1:
                if license[1].startswith('http'):
                    # Web link - use it
                    license_html = license_html.format(link=license[1].rstrip(),  name=license[0].rstrip())
                else:
                    # File name - check if exists and use it
                    license_file = join(S().web_root, 'misc', license[1].rstrip())
                    misc_path = join('output', 'misc', license[1].rstrip())

                    if os.path.exists(misc_path):
                        license_html = license_html.format(link=license_file, name=license[0].rstrip())
                    else:
                        print('ERROR: Wrong license definition:\n', license)

            # Use just name if there is any
            elif len(license) == 1:
                license_html = '<br>License: ' + license[0].rstrip()
            # No license
            else:
                license_html = ''
    else:
        license_html = ''

    # Get file size
    size = int(os.stat(new_download_path).st_size)
    sizes = {' GB': 1000000000,
             ' MB': 1000000,
             ' KB': 1000,
             ' B': 1}

    for key in sizes.keys():
        if size >= sizes[key]:
            size = str(round(size / sizes[key], 1)) + key
            break

    download_html = '''
    <div>
        <img src="/style/mimetypes/{icon}">
        <a href="{link}"><h4>{filename}</h4></a>
        Size: {size}{license}
    </div>
    '''

    return download_html.format(icon=icon_name,
                                link=join('/', 'downloads', filename),
                                filename=filename,
                                size=size,
                                license=license_html)
