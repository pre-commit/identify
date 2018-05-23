# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import find_packages
from setuptools import setup


setup(
    name='identify',
    description='File identification library for Python',
    url='https://github.com/chriskuehl/identify',
    version='1.0.17',

    author='Chris Kuehl',
    author_email='ckuehl@ocf.berkeley.edu',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    entry_points={'console_scripts': ['identify-cli=identify.cli:main']},
)
