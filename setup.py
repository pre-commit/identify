# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import find_packages
from setuptools import setup


setup(
    name='identify',
    version='0.0.3',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[],
    packages=find_packages(exclude=('tests*', 'testing*')),
    entry_points={'console_scripts': ['identify-cli=identify.cli:main']},
)
