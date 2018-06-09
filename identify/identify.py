# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import os.path
import shlex
import string

from identify import extensions
from identify import interpreters


printable = frozenset(string.printable)

DIRECTORY = 'directory'
SYMLINK = 'symlink'
FILE = 'file'
EXECUTABLE = 'executable'
NON_EXECUTABLE = 'non-executable'
TEXT = 'text'
BINARY = 'binary'

ALL_TAGS = {DIRECTORY, SYMLINK, FILE, EXECUTABLE, NON_EXECUTABLE, TEXT, BINARY}
ALL_TAGS.update(*extensions.EXTENSIONS.values())
ALL_TAGS.update(*extensions.NAMES.values())
ALL_TAGS.update(*interpreters.INTERPRETERS.values())
ALL_TAGS = frozenset(ALL_TAGS)


def tags_from_path(path):
    if not os.path.lexists(path):
        raise ValueError('{} does not exist.'.format(path))
    if os.path.isdir(path):
        return {DIRECTORY}
    if os.path.islink(path):
        return {SYMLINK}

    tags = {FILE}

    executable = os.access(path, os.X_OK)
    if executable:
        tags.add(EXECUTABLE)
    else:
        tags.add(NON_EXECUTABLE)

    # As an optimization, if we're able to read tags from the filename, then we
    # don't peek at the file contents.
    t = tags_from_filename(os.path.basename(path))
    if len(t) > 0:
        tags.update(t)
    else:
        if executable:
            shebang = parse_shebang_from_file(path)
            if len(shebang) > 0:
                tags.update(tags_from_interpreter(shebang[0]))

        if file_is_text(path):
            tags.add(TEXT)
        else:
            tags.add(BINARY)

    assert {TEXT, BINARY} & tags, tags
    assert {EXECUTABLE, NON_EXECUTABLE} & tags, tags
    return tags


def tags_from_filename(filename):
    _, filename = os.path.split(filename)
    _, ext = os.path.splitext(filename)

    ret = set()

    # Allow e.g. "Dockerfile.xenial" to match "Dockerfile"
    for part in {filename} | set(filename.split('.')):
        if part in extensions.NAMES:
            ret.update(extensions.NAMES[part])
            break

    if len(ext) > 0:
        ext = ext[1:].lower()
        if ext in extensions.EXTENSIONS:
            ret.update(extensions.EXTENSIONS[ext])

    return ret


def tags_from_interpreter(interpreter):
    _, _, interpreter = interpreter.rpartition('/')

    # Try "python3.5.2" => "python3.5" => "python3" until one matches.
    while interpreter:
        if interpreter in interpreters.INTERPRETERS:
            return interpreters.INTERPRETERS[interpreter]
        else:
            interpreter, _, _ = interpreter.rpartition('.')

    return set()


def is_text(bytesio):
    """Return whether the first KB of contents seems to be binary.

    This is roughly based on libmagic's binary/text detection:
    https://github.com/file/file/blob/df74b09b9027676088c797528edcaae5a9ce9ad0/src/encoding.c#L203-L228
    """
    text_chars = (
        bytearray([7, 8, 9, 10, 11, 12, 13, 27]) +
        bytearray(range(0x20, 0x7F)) +
        bytearray(range(0x80, 0X100))
    )
    return not bool(bytesio.read(1024).translate(None, text_chars))


def file_is_text(path):
    if not os.path.lexists(path):
        raise ValueError('{} does not exist.'.format(path))
    with open(path, 'rb') as f:
        return is_text(f)


def _shebang_split(line):
    try:
        # shebangs aren't supposed to be quoted, though some tools such as
        # setuptools will write them with quotes so we'll best-guess parse
        # with shlex first
        return shlex.split(line)
    except ValueError:
        # failing that, we'll do a more "traditional" shebang parsing which
        # just involves splitting by whitespace
        return line.split()


def parse_shebang(bytesio):
    """Parse the shebang from a file opened for reading binary."""
    if bytesio.read(2) != b'#!':
        return ()
    first_line = bytesio.readline()
    try:
        first_line = first_line.decode('UTF-8')
    except UnicodeDecodeError:
        return ()

    # Require only printable ascii
    for c in first_line:
        if c not in printable:
            return ()

    cmd = tuple(_shebang_split(first_line.strip()))
    if cmd[0] == '/usr/bin/env':
        cmd = cmd[1:]
    return cmd


def parse_shebang_from_file(path):
    """Parse the shebang given a file path."""
    if not os.path.lexists(path):
        raise ValueError('{} does not exist.'.format(path))
    if not os.access(path, os.X_OK):
        return ()

    with open(path, 'rb') as f:
        return parse_shebang(f)
