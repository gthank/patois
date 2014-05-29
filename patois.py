"""Utilities for writing code that runs on CPython, Jython, and other VMs."""
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
__author__ = 'Hank Gay <hank@realultimateprogramming.com>'
__version__ = '0.1.0'


import os
import platform
import re


def is_jython():
    return platform.python_implementation() == "Jython"


invalid_unicode_template = "[\u0001-\u0008\u000B\u000E-\u001F\u007F-\u009F\uFDD0-\uFDEF\uFFFE\uFFFF\U0001FFFE\U0001FFFF\U0002FFFE\U0002FFFF\U0003FFFE\U0003FFFF\U0004FFFE\U0004FFFF\U0005FFFE\U0005FFFF\U0006FFFE\U0006FFFF\U0007FFFE\U0007FFFF\U0008FFFE\U0008FFFF\U0009FFFE\U0009FFFF\U000AFFFE\U000AFFFF\U000BFFFE\U000BFFFF\U000CFFFE\U000CFFFF\U000DFFFE\U000DFFFF\U000EFFFE\U000EFFFF\U000FFFFE\U000FFFFF\U0010FFFE\U0010FFFF%s]"

if is_jython():
    # Jython is based on UTF-16, and as such, does not allow the use of
    # unmatched surrogate pairs (\uD800-\uDFFF), in literals or otherwise.
    invalid_unicode_re = re.compile(invalid_unicode_template % "")
else:
    # For those cases where unmatched surrogate pairs can exist, we still can't
    # use them in a literal (because it would break Jython to scan them).
    # Instead use one extra step of indirection and create surrogates with
    # unichr.
    invalid_unicode_re = re.compile(invalid_unicode_template % (
        "%s-%s" % (unichr(0xD800), unichr(0xDFFF)),))

replace_characters_regexp = re.compile(
        "([%s-%s](?![%s-%s])|(?<![%s-%s])[%s-%s])" % (
            unichr(0xD800), unichr(0xDBFF),
            unichr(0xDC00), unichr(0xDFFF),
            unichr(0xD800), unichr(0xDBFF),
            unichr(0xDC00), unichr(0xDFFF)))


def find_invalid_unicode(data):
    if is_jython():
        return []
    return invalid_unicode_re.findall(data)


def find_invalid_unicode_iter(data):
    if is_jython():
        return iter([])
    return invalid_unicode_re.finditer(data)


def scrub_invalid_unicode(data):
    if is_jython():
        return data
    return replace_characters_regexp.sub("\ufffd", data)


def _is_ucs2():
    if is_jython():
        return false
    return len("\U0010FFFF") != 1


def _is_ucs4():
    if is_jython():
        return false
    return len("\U0010FFFF") == 1


JYTHON_COMPILED_EXTENSION = "$py.class"


def module_name_from_file_name(file_name):
    """Figure out a module's name given the name of a compiled Python file."""
    if not file_name:
        return None

    if file_name.lower().endswith(JYTHON_COMPILED_EXTENSION):
        return file_name[:-len(JYTHON_COMPILED_EXTENSION)]

    return os.path.splitext(file_name)[0]
