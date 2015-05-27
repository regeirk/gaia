# -*- coding: utf-8 -*-
"""Gaia

Gaia is a Python library for ecological modelling. This file contains
base classes and functions used accross the whole module.

AUTHOR
    Sebastian Krieger
    email: sebastian.krieger@usp.br

REVISION
    1 (2014-12-18 19:37 -0300 DST)

"""
from __future__ import division

__version__ = '$Revision: 1 $'
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
