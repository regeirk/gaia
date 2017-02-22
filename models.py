# -*- coding: utf-8 -*-
"""Gaia

Gaia is a Python library for Lagrangian modelling.

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

    @property
    def x(self):
        """Zonal coordinate."""
        return self._get_attribute('x')
    @x.setter
    def x(self, a):
        self._set_attribute('x', a)

    @property
    def y(self):
        """Meridional coordinate."""
        return self._get_attribute('y')
    @y.setter
    def y(self, a):
        self._set_attribute('y', a)

    @property
    def z(self):
        """Depth coordinate."""
        return self._get_attribute('z')
    @z.setter
    def z(self, a):
        self._set_attribute('z', a)
