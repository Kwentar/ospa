.. role:: python(code)
   :language: python


Parameters description
--------------------
.. automodule:: ospa
    :members: listdir

Usage samples
--------------------

All samples are with dummy_test_folder (you can find it in repo_) which structure is:

.. code-block:: text

    dummy_test_folder/
    ├─antigravity.png
    ├─egg.png
    ├─empty.txt
    ├─holy_grenade.png
    ├─spam.jpg
    ├─txt_files/
    |  ├─1.txt
    |  ├─2.txt
    |  ├─3.txt
    |  └-not_txt.not_txt
    └-memes/
      ├─meme1.jpg
      ├─meme2.png
      ├─meme4.jpg
      ├─meme4.png
      └-meme monty python/
        ├─meme1.jpg
        ├─meme2.jpg
        └-meme3.jpg


____________________

Get all files in directory (without dirs) with absolute path
************************************************************

Filter dir items and return only files with full path:

.. code-block:: python

   import ospa
   dummy_folder = '/path/to/dummy_test_folder/'
   files = ospa.listdir(dummy_folder, only_files=True)

The result is:

.. code-block:: python

    ['/path/to/dummy_test_folder/antigravity.png',
     '/path/to/dummy_test_folder/egg.png',
     '/path/to/dummy_test_folder/empty.txt',
     '/path/to/dummy_test_folder/holy_grenade.png',
     '/path/to/dummy_test_folder/spam.jpg']

____________________

Get all file names in directory (without dirs)
************************************************

Filter dir items and return only file names:

.. code-block:: python

   import ospa
   dummy_folder = '/path/to/dummy_test_folder/'
   files = ospa.listdir(dummy_folder, full_path=False, only_files=True)

The result is:

.. code-block:: python

    ['antigravity.png',
     'egg.png',
     'empty.txt',
     'holy_grenade.png',
     'spam.jpg']

____________________

Get all files and directories in directory with absolute path
**************************************************************

Return all dir items with absolute path:

.. code-block:: python

   import ospa
   dummy_folder = '/path/to/dummy_test_folder/'
   files = ospa.listdir(dummy_folder)

The result is:

.. code-block:: python

    ['/path/to/dummy_test_folder/antigravity.png',
     '/path/to/dummy_test_folder/egg.png',
     '/path/to/dummy_test_folder/empty.txt',
     '/path/to/dummy_test_folder/holy_grenade.png',
     '/path/to/dummy_test_folder/spam.jpg',
     '/path/to/dummy_test_folder/memes',
     '/path/to/dummy_test_folder/txt_files']
____________________


The same as os.listdir_
***********************************

The behaviour is exactly the same as :python:`os.listdir()`:

.. code-block:: python

   import ospa
   dummy_folder = '/path/to/dummy_test_folder/'
   files = ospa.listdir(dummy_folder, full_path=False)

The result is:

.. code-block:: python

    ['antigravity.png',
     'egg.png',
     'empty.txt',
     'holy_grenade.png',
     'spam.jpg',
     'memes',
     'txt_files']
____________________


Get all images in directory and its subdirectories
***************************************************

You can use :python:`extensions` for getting all specific files.
:python:`Extensions` list can contains dot or not and not sensitive to register:

.. code-block:: python

   import ospa
   dummy_folder = '/path/to/dummy_test_folder/'
   files = ospa.listdir(dummy_folder, only_files=True,
                        walk=True, extensions=['png', 'jpg'])

The result is:

.. code-block:: python

    ['/path/to/dummy_test_folder/antigravity.png',
     '/path/to/dummy_test_folder/egg.png',
     '/path/to/dummy_test_folder/holy_grenade.png',
     '/path/to/dummy_test_folder/spam.jpg',
     '/path/to/dummy_test_folder/memes/meme1.jpg',
     '/path/to/dummy_test_folder/memes/meme2.png',
     '/path/to/dummy_test_folder/memes/meme4.jpg',
     '/path/to/dummy_test_folder/memes/meme4.png',
     '/path/to/dummy_test_folder/memes/meme monty python/meme1.jpg',
     '/path/to/dummy_test_folder/memes/meme monty python/meme2.jpg',
     '/path/to/dummy_test_folder/memes/meme monty python/meme3.jpg']


.. _repo: https://github.com/Kwentar/ospa
.. _os.listdir: https://docs.python.org/3/library/os.html#os.listdir