#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pynetoptix import __version__

setup(
    name='pynetoptix',
    version=__version__,
    description="A simple Python wrapper over NetworkOptix' HTTP API",
    url='https://github.com/davidvuong/pynetoptix',

    author='David Vuong',
    author_email='david.vuong256@gmail.com',

    classifiers=[
        'Intended Audience :: Developers',

        'Topic :: Utilities',

        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    install_requires=[],
    include_package_data=True,
    package_data={'': ['README.md']}
)