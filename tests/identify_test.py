# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import io
import os
import stat

import pytest

from identify import identify


def test_tags_from_path_does_not_exist(tmpdir):
    x = tmpdir.join('foo')
    with pytest.raises(ValueError):
        identify.tags_from_path(x.strpath)


def test_tags_from_path_directory(tmpdir):
    x = tmpdir.join('foo')
    x.mkdir()
    assert identify.tags_from_path(x.strpath) == {'directory'}


def test_tags_from_path_symlink(tmpdir):
    x = tmpdir.join('foo')
    x.mksymlinkto(tmpdir.join('lol').ensure())
    assert identify.tags_from_path(x.strpath) == {'symlink'}


def test_tags_from_path_broken_symlink(tmpdir):
    x = tmpdir.join('foo')
    x.mksymlinkto(tmpdir.join('lol'))
    assert identify.tags_from_path(x.strpath) == {'symlink'}


def test_tags_from_path_simple_file(tmpdir):
    x = tmpdir.join('test.py').ensure()
    assert identify.tags_from_path(x.strpath) == {
        'file', 'text', 'non-executable', 'python',
    }


def test_tags_from_path_file_with_shebang_non_executable(tmpdir):
    x = tmpdir.join('test')
    x.write_text('#!/usr/bin/env python\nimport sys\n', encoding='UTF-8')
    assert identify.tags_from_path(x.strpath) == {
        'file', 'text', 'non-executable',
    }


def test_tags_from_path_file_with_shebang_executable(tmpdir):
    x = tmpdir.join('test')
    x.write_text('#!/usr/bin/env python\nimport sys\n', encoding='UTF-8')
    make_executable(x.strpath)
    assert identify.tags_from_path(x.strpath) == {
        'file', 'text', 'executable', 'python',
    }


def test_tags_from_path_binary(tmpdir):
    x = tmpdir.join('test')
    x.write(b'\x7f\x45\x4c\x46\x02\x01\x01')
    make_executable(x.strpath)
    assert identify.tags_from_path(x.strpath) == {
        'file', 'binary', 'executable',
    }


@pytest.mark.parametrize(('filename', 'expected'), (
    ('test.py', {'text', 'python'}),
    ('test.mk', {'text', 'makefile'}),
    ('Makefile', {'text', 'makefile'}),
    ('Dockerfile', {'text', 'dockerfile'}),
    ('Dockerfile.xenial', {'text', 'dockerfile'}),
    ('xenial.Dockerfile', {'text', 'dockerfile'}),
    ('test.weird-unrecognized-extension', set()),
    ('test', set()),
    ('', set()),
))
def test_tags_from_filename(filename, expected):
    assert identify.tags_from_filename(filename) == expected


@pytest.mark.parametrize(('interpreter', 'expected'), (
    ('python', {'python'}),
    ('python3', {'python3', 'python'}),
    ('python3.5.2', {'python3', 'python'}),
    ('/usr/bin/python3.5.2', {'python3', 'python'}),
    ('/usr/bin/herpderpderpderpderp', set()),
    ('something-random', set()),
    ('', set()),
))
def test_tags_from_interpreter(interpreter, expected):
    assert identify.tags_from_interpreter(interpreter) == expected


@pytest.mark.parametrize(('data', 'expected'), [
    (b'hello world', True),
    (b'', True),
    ('éóñəå  ⊂(◉‿◉)つ(ノ≥∇≤)ノ'.encode('utf8'), True),
    ('¯\_(ツ)_/¯'.encode('utf8'), True),
    ('♪┏(・o･)┛♪┗ ( ･o･) ┓♪┏ ( ) ┛♪┗ (･o･ ) ┓♪┏(･o･)┛♪'.encode('utf8'), True),
    ('éóñå'.encode('latin1'), True),

    (b'hello world\x00', False),
    (b'\x7f\x45\x4c\x46\x02\x01\x01', False),  # first few bytes of /bin/bash
    (b'\x43\x92\xd9\x0f\xaf\x32\x2c', False),  # some /dev/urandom output
])
def test_is_text(data, expected):
    assert identify.is_text(io.BytesIO(data)) is expected


def test_file_is_text_simple(tmpdir):
    x = tmpdir.join('f')
    x.write_text('hello there\n', encoding='UTF-8')
    assert identify.file_is_text(x.strpath) is True


def test_file_is_text_does_not_exist(tmpdir):
    x = tmpdir.join('f')
    with pytest.raises(ValueError):
        identify.file_is_text(x.strpath)


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        (b'', ()),
        (b'#!/usr/bin/python', ('/usr/bin/python',)),
        (b'#!/usr/bin/env python', ('python',)),
        (b'#! /usr/bin/python', ('/usr/bin/python',)),
        (b'#!/usr/bin/foo  python', ('/usr/bin/foo', 'python')),
        (b'\xf9\x93\x01\x42\xcd', ()),
        (b'#!\xf9\x93\x01\x42\xcd', ()),
        (b'#!\x00\x00\x00\x00', ()),
    ),
)
def test_parse_shebang(s, expected):
    assert identify.parse_shebang(io.BytesIO(s)) == expected


def test_parse_shebang_from_file_does_not_exist():
    with pytest.raises(ValueError):
        identify.parse_shebang_from_file('herp derp derp')


def test_parse_shebang_from_file_nonexecutable(tmpdir):
    x = tmpdir.join('f')
    x.write_text('#!/usr/bin/env python', encoding='UTF-8')
    assert identify.parse_shebang_from_file(x.strpath) == ()


def test_parse_shebang_from_file_simple(tmpdir):
    x = tmpdir.join('f')
    x.write_text('#!/usr/bin/env python', encoding='UTF-8')
    make_executable(x.strpath)
    assert identify.parse_shebang_from_file(x.strpath) == ('python',)


def make_executable(filename):
    original_mode = os.stat(filename).st_mode
    os.chmod(
        filename,
        original_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH,
    )
