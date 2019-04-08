import os
import platform
import unittest

from ospa import _listdir, listdir


class TestOspaListDir(unittest.TestCase):
    """
    Test class for ospa.listdir function
    """
    @staticmethod
    def get_dummy_folder() -> str:
        """
        Get dummy test folder path
        :return: path to dummy folder
        """
        dummy_folder = f'..{os.path.sep}dummy_test_folder'
        return dummy_folder

    def test_main(self):
        """
        Test random test cases
        """
        dummy_folder = TestOspaListDir.get_dummy_folder()
        result = listdir(dummy_folder,
                         full_path=True,
                         only_files=False,)
        need_result = ['memes',
                       'txt_files',
                       'antigravity.png',
                       'egg.png',
                       'empty.txt',
                       'holy_grenade.png',
                       'spam.jpg',
                       ]
        need_result = [os.path.join(*(os.path.split(os.getcwd())[:-1]), 'dummy_test_folder', x) for x in need_result]
        self.assertEqual(set(need_result), set(result))

        result = listdir(dummy_folder,
                         full_path=False,
                         only_files=False,)
        need_result = ['memes',
                       'txt_files',
                       'antigravity.png',
                       'egg.png',
                       'empty.txt',
                       'holy_grenade.png',
                       'spam.jpg',
                       ]

        self.assertEqual(set(need_result), set(result))

        result = listdir(dummy_folder,
                         full_path=True,
                         only_files=True,)
        need_result = ['antigravity.png',
                       'egg.png',
                       'empty.txt',
                       'holy_grenade.png',
                       'spam.jpg',
                       ]
        need_result = [os.path.join(*(os.path.split(os.getcwd())[:-1]), 'dummy_test_folder', x) for x in need_result]
        self.assertEqual(set(need_result), set(result))

    def test_full(self):
        """
        Test full_path parameter on inner function
        """
        path = 'tmp'
        files = ['1.txt',
                 '2',
                 '3.jpg',
                 'folder',
                 ]
        need_result = []
        for file_ in files:
            need_result.append(os.path.join(path, file_))
        self.assertEqual(_listdir(path, files, full_path=True), need_result)
        self.assertEqual(_listdir(path, files, full_path=False), files)

    def test_only_files(self):
        """
        Test only files parameter
        """
        dummy_folder = TestOspaListDir.get_dummy_folder()
        need_result = ['meme1.jpg',
                       'meme2.png',
                       'meme4.jpg',
                       'meme4.png',
                       'meme monty python',
                       ]
        need_result_new = [os.path.join(*(os.path.split(os.getcwd())[:-1]),
                                        os.path.join('dummy_test_folder', 'memes'), x) for x in need_result[:-1]]
        result = listdir(os.path.join(dummy_folder, 'memes'), only_files=True)
        self.assertEqual(set(result), set(need_result_new))

        need_result_new = [os.path.join(*(os.path.split(os.getcwd())[:-1]),
                                        os.path.join('dummy_test_folder', 'memes'), x) for x in need_result]
        result = listdir(os.path.join(dummy_folder, 'memes'), only_files=False)
        self.assertEqual(set(result), set(need_result_new))


if __name__ == '__main__':
    unittest.main()
