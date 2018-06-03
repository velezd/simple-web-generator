import os


def path_split(path):
    """ Split path to components """
    directories = []
    while True:
        path, directory = os.path.split(path)

        if directory != "":
            directories.append(directory)
        else:
            if path != "":
                directories.append(path)

            break

    directories.reverse()
    return directories


def src_to_static(path):
    """ Replaces src to static at the start of path """
    new_path = path_split(path)
    if new_path[0] == 'src':
        new_path[0] = 'output'

    try:
        new_path[2] = new_path[2].split('-')[1]
    except IndexError:
        print('ERROR: All page directories must start with "[number]-"')

    return os.path.join(*new_path)

