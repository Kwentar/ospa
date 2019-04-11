import os
import unittest

from ospa import listdir
from ospa import OspaException


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
        dummy_folder = os.path.join(os.getcwd(), 'dummy_test_folder')
        return dummy_folder

    def test_main(self):
        """
        Test random test cases
        """
        dummy_folder = TestOspaListDir.get_dummy_folder()
        result = listdir(dummy_folder,
                         full_path=True,
                         only_files=False,
                         )
        need_result = ['memes',
                       'txt_files',
                       'antigravity.png',
                       'egg.png',
                       'empty.txt',
                       'holy_grenade.png',
                       'spam.jpg',
                       ]
        need_result = [os.path.join(dummy_folder, x) for x in need_result]
        self.assertEqual(sorted(need_result), sorted(result))

        result = listdir(dummy_folder,
                         full_path=False,
                         only_files=False,
                         )
        need_result = ['memes',
                       'txt_files',
                       'antigravity.png',
                       'egg.png',
                       'empty.txt',
                       'holy_grenade.png',
                       'spam.jpg',
                       ]

        self.assertEqual(sorted(need_result), sorted(result))

        result = listdir(dummy_folder,
                         full_path=True,
                         only_files=True,
                         )
        need_result = ['antigravity.png',
                       'egg.png',
                       'empty.txt',
                       'holy_grenade.png',
                       'spam.jpg',
                       ]
        need_result = [os.path.join(dummy_folder, x) for x in need_result]
        self.assertEqual(sorted(need_result), sorted(result))
        self.assertEqual(sorted(os.listdir('.')), sorted(listdir(path='.', full_path=False)))

    def test_full(self):
        """
        Test full_path parameter on inner function
        """
        dummy_folder = TestOspaListDir.get_dummy_folder()
        need_result = ['meme1.jpg',
                       'meme2.png',
                       'meme4.jpg',
                       'meme4.png',
                       'meme monty python',
                       ]
        result = listdir(os.path.join(dummy_folder, 'memes'), full_path=False)
        self.assertEqual(sorted(result), sorted(need_result))

        need_result_new = [os.path.join(dummy_folder, 'memes', x) for x in need_result]
        result = listdir(os.path.join(dummy_folder, 'memes'), full_path=True)
        self.assertEqual(sorted(result), sorted(need_result_new))

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
        need_result_new = [os.path.join(dummy_folder, 'memes', x) for x in need_result[:-1]]
        result = listdir(os.path.join(dummy_folder, 'memes'), only_files=True)
        self.assertEqual(sorted(result), sorted(need_result_new))

        need_result_new = [os.path.join(dummy_folder, 'memes', x) for x in need_result]
        result = listdir(os.path.join(dummy_folder, 'memes'), only_files=False)
        self.assertEqual(sorted(result), sorted(need_result_new))

    def test_walk_full(self):
        """
        Test walk parameter with full path
        """
        dummy_folder = TestOspaListDir.get_dummy_folder()
        need_result = []
        for i in range(1, 4):
            need_result.append(os.path.join(dummy_folder, 'memes', 'meme monty python', 'meme{}.jpg'.format(i)))
        need_result.append(os.path.join(dummy_folder, 'memes', 'meme1.jpg'))
        need_result.append(os.path.join(dummy_folder, 'memes', 'meme2.png'))
        need_result.append(os.path.join(dummy_folder, 'memes', 'meme4.jpg'))
        need_result.append(os.path.join(dummy_folder, 'memes', 'meme4.png'))

        need_result.append(os.path.join(dummy_folder, 'txt_files', '1.txt'))
        need_result.append(os.path.join(dummy_folder, 'txt_files', '2.txt'))
        need_result.append(os.path.join(dummy_folder, 'txt_files', '3.txt'))
        need_result.append(os.path.join(dummy_folder, 'txt_files', 'not_txt.not_txt'))

        for i in ['antigravity.png',
                  'egg.png',
                  'empty.txt',
                  'holy_grenade.png',
                  'spam.jpg',
                  ]:
            need_result.append(os.path.join(dummy_folder, i))

        result = listdir(dummy_folder, full_path=True, only_files=True, walk=True)
        self.assertEqual(sorted(result), sorted(need_result))

    def test_walk_not_full(self):
        """
        Test walk parameter without full path
        """
        dummy_folder = TestOspaListDir.get_dummy_folder()
        need_result = []
        for i in range(1, 4):
            need_result.append('meme{}.jpg'.format(i))
        need_result.extend(['meme1.jpg',
                            'meme2.png',
                            'meme4.jpg',
                            'meme4.png',
                            '1.txt',
                            '2.txt',
                            '3.txt',
                            'not_txt.not_txt',
                            'antigravity.png',
                            'egg.png',
                            'empty.txt',
                            'holy_grenade.png',
                            'spam.jpg',
                            ])

        result = listdir(dummy_folder, full_path=False, only_files=True, walk=True)
        self.assertEqual(sorted(result), sorted(need_result))

    def test_exceptions(self):
        """
        Test exceptions
        """
        dummy_folder = TestOspaListDir.get_dummy_folder()
        with self.assertRaises(OspaException):
            listdir(dummy_folder, full_path=True, only_files=False, walk=True)
        with self.assertRaises(OspaException):
            listdir(extensions='wrong ext')

    def test_double_dot(self):
        result = listdir(os.path.join('..', 'ospa', 'dummy_test_folder'), full_path=False)
        need_result = ['memes',
                       'txt_files',
                       'antigravity.png',
                       'egg.png',
                       'empty.txt',
                       'holy_grenade.png',
                       'spam.jpg',
                       ]

        self.assertEqual(sorted(result), sorted(need_result))

    def test_get_only_names(self):
        """
        Test function get only names from list of files with full path
        """
        dummy_folder = TestOspaListDir.get_dummy_folder()
        result = listdir(dummy_folder, full_path=False, only_files=True, walk=True)
        need_result = []
        for i in range(1, 4):
            need_result.append('meme{}.jpg'.format(i))
        need_result.extend(['meme1.jpg',
                            'meme2.png',
                            'meme4.jpg',
                            'meme4.png',
                            '1.txt',
                            '2.txt',
                            '3.txt',
                            'not_txt.not_txt',
                            'antigravity.png',
                            'egg.png',
                            'empty.txt',
                            'holy_grenade.png',
                            'spam.jpg',
                            ])
        self.assertEqual(sorted(result), sorted(need_result))

    def test_extensions(self):
        """
        Test extensions parameter with full path
        """
        dummy_folder = TestOspaListDir.get_dummy_folder()
        need_result = []
        for i in range(1, 4):
            need_result.append(os.path.join(dummy_folder, 'memes', 'meme monty python', 'meme{}.jpg'.format(i)))
        need_result.append(os.path.join(dummy_folder, 'memes', 'meme1.jpg'))
        need_result.append(os.path.join(dummy_folder, 'memes', 'meme2.png'))
        need_result.append(os.path.join(dummy_folder, 'memes', 'meme4.jpg'))
        need_result.append(os.path.join(dummy_folder, 'memes', 'meme4.png'))

        for i in ['antigravity.png',
                  'egg.png',
                  'holy_grenade.png',
                  'spam.jpg',
                  ]:
            need_result.append(os.path.join(dummy_folder, i))

        result = listdir(dummy_folder, full_path=True, only_files=True, walk=True, extensions=['jpg', 'png'])
        self.assertEqual(sorted(result), sorted(need_result))
        result = listdir(dummy_folder, full_path=True, only_files=True, walk=True, extensions=['.jpg', '.png'])
        self.assertEqual(sorted(result), sorted(need_result))
        result = listdir(dummy_folder, full_path=True, only_files=True, walk=True, extensions=['.JPG', 'png'])
        self.assertEqual(sorted(result), sorted(need_result))
        result = listdir(dummy_folder, full_path=True, only_files=True, walk=True, extensions=('.JPG', 'png'))
        self.assertEqual(sorted(result), sorted(need_result))
        result = listdir(dummy_folder, full_path=True, only_files=True, walk=True, extensions={'.JPG', 'png'})
        self.assertEqual(sorted(result), sorted(need_result))

    def test_os_listdir(self):
        """
        Compare the result of listdir from os with ours
        """
        need_result = os.listdir('.')
        result = listdir(path='.', full_path=False)
        self.assertEqual(sorted(result), sorted(need_result))
