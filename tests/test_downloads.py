import os
import json


def test_downloads():
    # Load mimetypes
    mimetypes = {}
    try:
        with open('../lib/mimetypes.json', 'r') as file:
            mimetypes = json.loads(file.read())
    except IOError:
        print('ERROR: Can\'t load mimetypes')
    except ValueError:
        print('ERROR: Wrong values in mimetypes file')

    # Load licenses
    licenses = []
    try:
        with open('../lib/licenses.json', 'r') as file:
            temp = json.loads(file.read())
            for key in temp.keys():
                licenses.append([':'+key, ''])

    except IOError:
        print('ERROR: Can\'t load licenses')
    except ValueError:
        print('ERROR: Wrong values in licenses file')

    # Add custom license
    licenses.append([':MIT', ':https://opensource.org/licenses/MIT'])

    # Create files in the downloads directory and prepare html for test page
    if mimetypes is not None:
        html = '@name:Downloads test\n<p>This is test of all downloads mimetypes defined.</p>\n'

        for type in mimetypes:
            name = '../src/downloads/{name}.{ext}'.format(name=mimetypes[type].split('.')[0], ext=type)
            if not os.path.exists(name):
                with open(name, 'w') as f:
                    f.write('\n')
            # Get one license
            license = ['','']
            if len(licenses):
                license = licenses.pop()
            html += '@download:{name}{license_name}{license_link}\n'.format(name=os.path.split(name)[1],
                                                                            license_name=license[0],
                                                                            license_link=license[1])

        html += '\n\n'

        # save test page
        if os.path.exists('../src/pages'):
            if not os.path.exists('../src/pages/100-downloads'):
                os.mkdir('../src/pages/100-downloads')

            with open('../src/pages/100-downloads/index.html', 'w') as file:
                file.write(html)


if __name__ == '__main__':
    test_downloads()
