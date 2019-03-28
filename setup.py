import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    setuptools.setup(
     name='ospa',
     version='0.11',
     author="Aleksei Alekseev",
     author_email="alekseev.yeskela@gmail.com",
     description="OS extension",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/kwentar/ospa",
     packages=['ospa'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )