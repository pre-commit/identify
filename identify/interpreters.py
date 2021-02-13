# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

INTERPRETERS = {
    'ash': {'shell', 'ash'},
    'awk': {'awk'},
    'bash': {'shell', 'bash'},
    'bats': {'shell', 'bash', 'bats'},
    'csh': {'shell', 'csh'},
    'dash': {'shell', 'dash'},
    'expect': {'expect'},
    'ksh': {'shell', 'ksh'},
    'node': {'javascript'},
    'nodejs': {'javascript'},
    'perl': {'perl'},
    'python': {'python'},
    'python2': {'python', 'python2'},
    'python3': {'python', 'python3'},
    'ruby': {'ruby'},
    'sh': {'shell', 'sh'},
    'tcsh': {'shell', 'tcsh'},
    'zsh': {'shell', 'zsh'},
}
