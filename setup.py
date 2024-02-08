__author__ = 'mod by atotickov'

from pathlib import Path
from os.path import join, dirname
from setuptools import setup, find_packages

dependencies = ['scipy', 'numpy', 'pandas', 'matplotlib', 'biopython',
                'lxml', 'beautifulsoup4', 'requests']

setup(name='quarTeT',
      version='1.1.6',
      packages=find_packages(),
      author='mod by Azamat Totikov',
      author_email='a.totickov1@gmail.com',
      install_requires=dependencies,
      long_description=open(join(dirname(__file__), 'README.md')).read(),
      scripts=list(map(str, sorted(Path('./').rglob("*.py")))))
