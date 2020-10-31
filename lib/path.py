import os


def path_split(path):
    ''' Split path to components '''
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
    ''' Replaces src to output at the start of path '''
    new_path = path_split(path)
    if new_path[0] == 'src':
        new_path[0] = 'output'

    # Remove numbering from path:
    # /pages/10-blog/posts/10-skoda_forman.html -> /pages/blog/posts/skoda_forman.html
    for x in range(len(new_path)):
        if '-' in new_path[x]:
            new_path[x] = new_path[x].split('-')[1]

    return os.path.join(*new_path)


def src_to_link(path):
    ''' Replaces src to / at the start of path '''
    new_path = path_split(path)
    if new_path[0] == 'src':
        new_path[0] = '/'

    # Remove numbering from path:
    # /pages/10-blog/posts/10-skoda_forman.html -> /pages/blog/posts/skoda_forman.html
    for x in range(len(new_path)):
        if '-' in new_path[x]:
            new_path[x] = new_path[x].split('-')[1]

    return os.path.join(*new_path)

