# -*- coding: utf-8 -*-
"""Gaia

Gaia is a Python library for ecological modelling.

This module implements tests for class of individuals.

AUTHOR
    Sebastian Krieger
    email: sebastian.krieger@usp.br

REVISION
    1 (2014-12-16 18:37 -0300 DST)

"""
from __future__ import division

__version__ = '$Revision: 1 $'
# $Source$

import unittest

import gaia

class TestData(unittest.TestCase):
    def setUp(self):
        args = dict(t=0, x=-45.71605, y=-23.77226, z=0)
        self.individual = gaia.individuals.Individual(**args)
        self.plankton = gaia.individuals.Plankton(P=0., N_P=0., C_Chla=6.,
            r=0.1, mu_m=0.58, E_0_cp=1.0, E_0_inb=40, d_r=0.1,
            phi_m=0.0833, Q_m_N=0.29, K_Q_N=0.18, K_s_NO3=0.1, K_s_NH4=0.05,
            Psi=1000., gamma=0.1, **args)


    #def tearDown(self):
    #    del self.individual


    def test_individual_set_properties(self):
        self.individual.t = 0
        self.individual.x = -45.71605
        self.individual.y = -23.77226
        self.individual.z = 0


    def test_individual_get_properties(self):
        self.assertEqual(self.individual.t, 0)
        self.assertEqual(self.individual.x, -45.71605)
        self.assertEqual(self.individual.y, -23.77226)
        self.assertEqual(self.individual.z, 0)


    def test_plankton_get_properties(self):
        self.assertEqual(self.plankton.t, 0)
        self.assertEqual(self.plankton.x, -45.71605)
        self.assertEqual(self.plankton.y, -23.77226)
        self.assertEqual(self.plankton.z, 0)
        #
        self.assertEqual(self.plankton.P, 0.)
        self.assertEqual(self.plankton.N_P, 0.)
        self.assertEqual(self.plankton.C_Chla, 6.)
        #
        self.assertEqual(self.plankton.r, 0.1)
        self.assertEqual(self.plankton.mu_m, 0.58)
        self.assertEqual(self.plankton.E_0_cp, 1.0)
        self.assertEqual(self.plankton.E_0_inb, 40)
        self.assertEqual(self.plankton.d_r, 0.1)
        self.assertEqual(self.plankton.phi_m, 0.0833)
        self.assertEqual(self.plankton.Q_m_N, 0.29)
        self.assertEqual(self.plankton.K_Q_N, 0.18)
        self.assertEqual(self.plankton.K_s_NO3, 0.1)
        self.assertEqual(self.plankton.K_s_NH4, 0.05)
        self.assertEqual(self.plankton.Psi, 1000.)
        self.assertEqual(self.plankton.gamma, 0.1)

    def test_plankton_mu_mt(self):
        self.assertEqual(self.plankton.mu_mt(27.), self.plankton.mu_m)
    

def main():
    unittest.main()


if __name__ == '__main__':
    main()
