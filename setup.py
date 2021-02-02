#!/usr/bin/env python
# -*- coding: utf-8 -*

from __future__ import absolute_import

import os
from codecs import open

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()


long_desc = '''Asynchronous python library for Libgen.rs to search and download books.\n\n Installing libgenesis\n \
        using the command line\n \
        pip install libgenesis\n\n \
        Importing libgenesis\n \
        from libgenesis import Libgen\n\n \
        Creating libgenesis object\n \
        lg = Libgen()\n \
        or\n \
        lg = Libgen(sort= "year", sort_mode= "ASC", result_limit= 50)\n\n \
        Searching for a book\n \
        async def search():\n \
            q = "japan history"\n \
            result = await lg.search(q)\n \
            for item in result:\n \
                print("id = " + item)\n \
                print("title = " + result[item]["title"])\n \
                print("md5 = " + result[item]["md5"])\n\n
        Downloading for a book\n
        async def download():\n
            q = "japan history"\n
            result = await lg.search(q)\n
            download_location = []\n
            for item in result:\n
                file_path = await lg.download(result[item]["mirrors"]["main"])\n
                # path = Path("Downloads")\n
                # file_path = await lg.download(result[item]["mirrors"]["main"]], dest_folder=path)\n
                download_location.append(file_path)'''


setup(name='libgenesis',
      version='0.1.0',
      packages=find_packages(exclude=('tests')),
      zip_safe=False,
      url='https://github.com/Samfun75/libgenesis',
      long_description_content_type='text/markdown',
      description='Asynchronous python lib for Libgen.rs',
      download_url='https://github.com/Samfun75/libgenesis/archive/v0.1.0.tar.gz',
      long_description=long_desc,
      author='Samson Misganaw',
      author_email='samfunn75@gmail.com',
      license='MIT License',
      install_requires=install_requires,
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Internet :: WWW/HTTP',
      ])
