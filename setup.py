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


with open('README.md', 'r', encoding='utf-8') as rm_file:
    readme = rm_file.read()

setup(name='libgenesis',
      version='0.1.4',
      packages=find_packages(exclude=('tests')),
      zip_safe=False,
      url='https://github.com/Samfun75/libgenesis',
      long_description_content_type='text/markdown',
      description='Asynchronous python lib for Libgen.rs',
      download_url='https://github.com/Samfun75/libgenesis/archive/v0.1.4.tar.gz',
      long_description=readme,
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
