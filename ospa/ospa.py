import os


def _listdir(main_dir, file_list, full_path=True, only_files=False):
    if only_files:
        file_list = [x for x in file_list if os.path.isfile(os.path.join(main_dir, x))]
    if full_path:
        file_list = [os.path.join(main_dir, x) for x in file_list]
    return file_list


def listdir(path: str, full_path=True, only_files=False) -> list:
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
    # if not only_files and use_walk:
    #     raise OspaException('only_files is False and use_walk is True, it is not correct')
    return _listdir(path, os.listdir(path), full_path, only_files)


if __name__ == '__main__':
    print(listdir('..\\dummy_test_folder', only_files=True))