# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import pytest

from identify import extensions


@pytest.mark.parametrize('extension', extensions.EXTENSIONS)
def test_extensions_have_binary_or_text(extension):
    tags = extensions.EXTENSIONS[extension]
    assert len({'text', 'binary'} & tags) == 1, tags
