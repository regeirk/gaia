# -*- coding: utf-8 -*-
"""Gaia

Gaia is a Python library for ecological modelling.

AUTHOR
    Sebastian Krieger
    email: sebastian.krieger@usp.br

REVISION
    1 (2014-12-16 18:37 -0300 DST)

"""
from __future__ import division

__version__ = '$Revision: 1 $'
# $Source$

from gaia.base import BaseClass

###############################################################################
# CLASSES
###############################################################################
class Model(BaseClass):
    """Model class."""
    # Default properties (attributes) for each model.
    @property
    def t(self):
        """Time (age)."""
        return self._get_attribute('t')
    @t.setter
    def t(self, a):
        self._set_attribute('t', a)
    
    @property
    def dt(self):
        """Time step."""
        return self._get_attribute('dt')
    @dt.setter
    def dt(self, a):
        self._set_attribute('dt', a)


class Environment(BaseClass):
    """Environmental pools for models."""
    def read(self, t, z, y, x):
        """Read data."""
        return None

    
    @property
    def name(self):
        """Name."""
        return self._get_attribute('name')
    @name.setter
    def name(self, a):
        self._set_attribute('name', a)
    
    @property
    def description(self):
        """Description."""
        return self._get_attribute('description')
    @description.setter
    def description(self, a):
        self._set_attribute('description', a)

    @property
    def units(self):
        """Units."""
        return self._get_attribute('units')
    @units.setter
    def units(self, a):
        self._set_attribute('units', a)
