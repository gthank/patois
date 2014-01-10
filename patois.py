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


JYTHON_COMPILED_EXTENSION = '$py.class'


def module_name_from_file_name(file_name):
    """Figure out a module's name given the name of a compiled Python file."""
    if not file_name:
        return None

    if file_name.lower().endswith(JYTHON_COMPILED_EXTENSION):
        return file_name[:-len(JYTHON_COMPILED_EXTENSION)]

    return os.path.splitext(file_name)[0]
