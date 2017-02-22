# -*- coding: utf-8 -*-
"""Gaia

Gaia is a Python library for ecological modelling.

Disclaimer
----------
This software may be used, copied, or redistributed as long as it is
not sold and this copyright notice is reproduced on each copy made.
This routine is provided as is without any express or implied
warranties whatsoever.

Author
------
Sebastian Krieger (sebastian.krieger@usp.br)

Revision
--------
1 (2014-12-16 18:37 -0300 DST)

"""
from __future__ import division

from sys import stdout

__version__ = '$Revision: 1 $'
__author__ = 'Sebastian Krieger (sebastian.krieger@usp.br)'
# $Source$


###############################################################################
# CLASSES
###############################################################################
class BaseClass(object):
    """Base class for module."""
    def __init__(self, **kwargs):
        # Initializes the attributes dictionary
        self._attributes = dict()
        #
        for key, item in kwargs.items():
            try:
                setattr(self, key, item)
            except:
                print 'Warning: Invalid attribute {0}'.format(key)
                pass
        #
        return

    def _set_attribute(self, attrib, val):
        self._attributes[attrib] = val

    def _get_attribute(self, attrib):
        if attrib in self._attributes.keys():
            return self._attributes[attrib]
        else:
            return None

    def message(self, s):
        """Prints `s` to standard output."""
        # Includes erase line ANSI terminal string when using return feed
        # character.
        # (source:http://www.termsys.demon.co.uk/vtansi.htm#cursor)
        EL = '\x1b[2K'
        s = s.replace('\r', '{}\r'.format(EL))
        stdout.write(s)
        stdout.flush()
