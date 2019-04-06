import os

from ospa_exception import OspaException


def listdir(path: str, full_path=True, only_files=False, use_walk=False) -> list:
    """
    Generate list of dir based on parameters
    :param path: source path, can be '.' or contains one '..' which means one level top
    :param full_path: if True return will return full path of files
    :param only_files: if True return only files without dir (os.path.isfile is used)
    :param use_walk:
    :return: list of dir
    """
    if path == '.':
        path = os.getcwd()
    if '..' in path:
        if path.count('..') != 1:
            raise OspaException('only one ".." can be in path')
        current_path = os.getcwd()
        previous_path = os.path.split(current_path)[0]
        path = path.replace('..', previous_path)
    if not only_files and use_walk:
        raise OspaException('only_files is False and use_walk is True, it is not correct')
    items = [x for x in os.listdir(path)]
    if only_files:
        items = [x for x in items if os.path.isfile(os.path.join(path, x))]
    if full_path:
        items = [os.path.join(path, x) for x in items]
    return items


if __name__ == '__main__':
    print(listdir('..\\dummy_test_folder', only_files=True))
