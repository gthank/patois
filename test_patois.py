#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for patois."""
from __future__ import (print_function, absolute_import,
                        unicode_literals, division)
# Copyright (c) 2014 Hank Gay
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import unittest
import patois


class TestPatoisFunctions(unittest.TestCase):
    """Tests for the unbound functions in ``patois``."""

    def test_module_name_from_file_name(self):
        """Test :py:func:`patois.module_name_from_file_name`."""
        # Standard CPython bytecode filename
        self.assertEqual('a', patois.module_name_from_file_name('a.py'))
        # Standard CPython bytecode filename that *isn't* all lower-case.
        self.assertEqual('a', patois.module_name_from_file_name('a.PY'))
        # Jython bytecode filename
        self.assertEqual('a', patois.module_name_from_file_name('a$py.class'))
        # Jython bytecode filename that *isn't* all lower-case.
        self.assertEqual('a', patois.module_name_from_file_name('a$PY.CLASS'))


if __name__ == '__main__':
    unittest.main()
