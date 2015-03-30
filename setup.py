# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tictactoe-py',
    version='1.0.0',
    description='Yet another Python Tic-Tac-Toe library',
    long_description=long_description,
    url='https://github.com/daniboy/tictactoe-py',
    author='Daniel Rozenberg',
    author_email='me@danielrozenberg.com',
    license='GPL',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Games/Entertainment :: Board Games',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        # FIXME I have no idea if this works on older versions, if you want to test it please let me know the results!
    ],
    keywords='tictactoe tic-tac-toe',
    packages=['tictactoe'],
)