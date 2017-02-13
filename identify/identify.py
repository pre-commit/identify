# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import io
import os
import shlex
import string


printable = frozenset(string.printable)


def parse_shebang(bytesio):
    """Parse the shebang from a file opened for reading binary."""
    if bytesio.read(2) != b'#!':
        return ()
    first_line = bytesio.readline()
    try:
        first_line = first_line.decode('US-ASCII')
    except UnicodeDecodeError:
        return ()

    # Require only printable ascii
    for c in first_line:
        if c not in printable:
            return ()

    cmd = tuple(shlex.split(first_line))
    if cmd[0] == '/usr/bin/env':
        cmd = cmd[1:]
    return cmd


def parse_shebang_from_file(path):
    """Parse the shebang given a file path."""
    if not os.path.exists(path) or not os.access(path, os.X_OK):
        return ()

    with io.open(path, 'rb') as f:
        return parse_shebang(f)
