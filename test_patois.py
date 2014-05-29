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
import rstr


class TestPatoisFunctions(unittest.TestCase):
    """Tests for the unbound functions in ``patois``."""
    def setUp(self):
        if patois._is_ucs2():
            bad_ucs2_string = "([%s-%s](?![%s-%s])|(?<![%s-%s])[%s-%s])"
            self.bad_string = bad_ucs2_string % (unichr(0xD800), unichr(0xDBFF), unichr(0xDC00), unichr(0xDFFF), unichr(0xD800), unichr(0xDBFF), unichr(0xDC00), unichr(0xDFFF))
        elif patois._is_ucs4():
            bad_ucs4_string = "[%s-%s]"
            self.bad_string = bad_ucs4_string % (unichr(0xD800), unichr(0xDFFF))

    def test_find_invalid_unicode(self):
        """Test :py:func:`patois.find_invalid_unicode`."""
        if patois.is_jython():
            return
        data = rstr.xeger(self.bad_string)
        # We expect a non-empty list, so that should evaluate to True.
        self.assertTrue(patois.find_invalid_unicode(data))

    def test_find_invalid_unicode_iter(self):
        """Test :py:func:`patois.find_invalid_unicode_iter`."""
        if patois.is_jython():
            return
        data = rstr.xeger(self.bad_string)
        # We expect a non-empty result. If we get an empty, next() will raise
        # StopIteration and the test will fail.
        next(patois.find_invalid_unicode_iter(data))

    def test_scrub_invalid_unicode(self):
        """Test :py:func:`patois.scrub_invalid_unicode`."""
        if patois.is_jython():
            return

        data = rstr.xeger(self.bad_string)
        before = len(data)
        after = len(patois.scrub_invalid_unicode(data))
        self.assertEquals(before, after)

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
