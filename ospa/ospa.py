import os

from . import OspaException


def get_only_names(file_list: list) -> list:
    """
    remove all from path except file
    :param file_list: list with files
    :return: list with file names only
    """
    result = (os.path.split(f)[-1] for f in file_list)
    result = [f for f in result if f]
    return result


def listdir(path='.',
            full_path=True,
            only_files=False,
            walk=False,
            extensions=None) -> list:
    """
    Generate items list of directory
    :param path: source path, can be '.' or contains one '..' which means one level top
    :param full_path: if True return will return full path of files
    :param only_files: if True return only files without dir (os.path.isfile is used)
    :param walk: Generate the file names in a directory tree by walking the tree either
    top-down or bottom-up, using os.walk() https://docs.python.org/3/library/os.html#os.walk
    :param extensions: list, tuple or set with file extensions
    :return: files or/and dirs in path
    """
    if path == '.':
        path = os.getcwd()
    if '..' in path:
        if path.count('..') != 1:
            raise OspaException('Only one ".." can be in path')
        current_path = os.getcwd()
        previous_path = os.path.split(current_path)[0]
        path = path.replace('..', previous_path)
    if not only_files and walk:
        raise OspaException('The parameter only_files is False and walk is True, it is not correct. '
                            'Walk can be True only when only_files is True')

    file_list = os.listdir(path)
    if only_files:
        if walk:
            file_list = []
            for root, dirs, files in os.walk(path):
                for file_ in files:
                    file_list.append(os.path.join(root, file_))
            if not full_path:
                file_list = get_only_names(file_list)
        else:
            file_list = [x for x in file_list if os.path.isfile(os.path.join(path, x))]
    if full_path and not walk:  # when walk we have full paths already
        file_list = [os.path.join(path, x) for x in file_list]

    # Extensions filter
    if extensions:
        if isinstance(extensions, list) or isinstance(extensions, tuple) or isinstance(extensions, set):
            extensions = list(map(lambda x: x.replace('.', '').lower(), extensions))
            file_list = [f for f in file_list if os.path.splitext(f)[-1][1:].lower() in extensions]
        else:
            raise OspaException('The parameter extensions must be one of: list, set, tuple. ')
    return file_list
