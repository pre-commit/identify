# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import pytest

from identify import extensions


@pytest.mark.parametrize('extension', extensions.EXTENSIONS)
def test_extensions_have_binary_or_text(extension):
    tags = extensions.EXTENSIONS[extension]
    assert len({'text', 'binary'} & tags) == 1, tags


@pytest.mark.parametrize('extension', extensions.EXTENSIONS_NEED_BINARY_CHECK)
def test_need_binary_check_do_not_specify_text_binary(extension):
    tags = extensions.EXTENSIONS_NEED_BINARY_CHECK[extension]
    assert len({'text', 'binary'} & tags) == 0, tags


def test_mutually_exclusive_check_types():
    assert not (
        set(extensions.EXTENSIONS) &
        set(extensions.EXTENSIONS_NEED_BINARY_CHECK)
    )
