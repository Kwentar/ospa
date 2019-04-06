import os

from ospa_exception import OspaException


def listdir(path, full_path=True, only_files=False, use_walk=False):
    if only_files is False and use_walk is True:
        raise OspaException('only_files is False and use_walk is True, it is not correct')
    return [os.path.join(path, x) for x in os.listdir(path)]


if __name__ == '__main__':
    # listdir('.', only_files=False, use_walk=True)
    listdir('.', only_files=False, use_walk=False)
    listdir('.', only_files=True, use_walk=True)
    listdir('.', only_files=True, use_walk=False)
