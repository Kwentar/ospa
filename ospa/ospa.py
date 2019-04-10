import os

from . import OspaException


def listdir(path='.',
            full_path=True,
            only_files=False,
            walk=False,
            extensions=None) -> list:
    """
    Generate items list of directory

    :param path: source path
    :type path: str
    :param full_path: if True, return full path of files.
    :type full_path: bool
    :param only_files: if True, return only files without dir (os.path.isfile() is used).
    :type only_files: bool
    :param walk: Generate the file names in a directory tree by walking the tree top-down, using os.walk().
    :type walk: bool
    :param extensions: list, tuple or set with file extensions.
    :return: files or/and dirs in path

    """
    path = os.path.abspath(path)
    if not only_files and walk:
        raise OspaException('The parameter only_files is False and walk is True, it is not correct. '
                            'Walk can be True only when only_files is True')

    file_list = os.listdir(path)
    if only_files:
        if walk:
            file_list = []
            for root, dirs, files in os.walk(path):
                for file_ in files:
                    if full_path:
                        file_list.append(os.path.join(root, file_))
                    else:
                        file_list.append(file_)
        else:
            file_list = [x for x in file_list if os.path.isfile(os.path.join(path, x))]
    if full_path and not walk:  # when walk we have full paths already
        file_list = [os.path.join(path, x) for x in file_list]

    # Extensions filter
    if extensions:
        if isinstance(extensions, list) or \
                isinstance(extensions, tuple) or \
                isinstance(extensions, set):
            extensions = list(map(lambda x: x.replace('.', '').lower(), extensions))
            file_list = [f for f in file_list if os.path.splitext(f)[-1][1:].lower() in extensions]
        else:
            raise OspaException('The parameter extensions must be one of: list, set, tuple. ')
    return file_list
