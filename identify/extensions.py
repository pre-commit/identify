# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


EXTENSIONS = {
    'conf': {'text', 'conf'},
    'css': {'text', 'css'},
    'gif': {'binary', 'image', 'gif'},
    'go': {'text', 'go'},
    'ini': {'text', 'ini'},
    'md': {'text', 'markdown'},
    'mk': {'text', 'makefile'},
    'png': {'binary', 'image', 'png'},
    'pp': {'text', 'puppet'},
    'py': {'text', 'python'},
    'rb': {'text', 'ruby'},
    'scss': {'text', 'scss'},
    'sh': {'text', 'shell'},
    'yaml': {'text', 'yaml'},
    'yml': {'text', 'yaml'},
}

NAMES = {
    '.dockerignore': {'text', 'dockerignore'},
    '.gitignore': {'text', 'gitignore'},
    '.gitmodules': {'text', 'gitmodules'},
    'Dockerfile': {'text', 'dockerfile'},
    'Gemfile': EXTENSIONS['rb'],
    'Makefile': EXTENSIONS['mk'],
}
