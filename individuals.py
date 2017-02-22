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

from numpy import append, array, bool_, exp, tanh, ndarray, ones, nan, inf
from numpy.core.records import fromrecords

from gaia.base import BaseClass

__version__ = '$Revision: 1 $'
# $Source$


###############################################################################
# FUNCTIONS
###############################################################################
def only_positive(y):
    return y * (y >= 0) + 0 * (y < 0)


###############################################################################
# CLASSES
#############################################################################
class Individual(BaseClass):
    """
    Class that characterizes an individual in an individual-based model.
    """

    def __init__(self, **kwargs):
        # Runs BaseClass.__init__ for default object initialization.
        super(Individual, self).__init__(**kwargs)
        # Ressets state parameters
        self._attributes['history'] = dict()
        self.state_parameters = []

    def set_state_parameters(self, params):
        """Sets the state parameters of the individual."""
        self.state_parameters = params

    def append_history(self, extra=None, nmax=inf):
        """
        Appends current status to individuum's history. Note that the
        list of variables is given in state_parameters.

        Parameters
        ----------
        extra : dictionary, optional
            Dictionary containing extra values to append.
        nmax : int, optional
            Number of maximum history items to be stored.

        Returns
        -------
        Nothing.

        Example
        -------
        append_history()

        """
        for key in self.state_parameters:
            try:
                if nmax == inf:
                    start = -self._attributes['history'][key].shape[0]
                else:
                    start = -nmax
                self._attributes['history'][key] = (
                    append(
                        self._attributes['history'][key][start:, ],
                        [self._attributes[key]],
                        axis=0
                    )
                )
            except:
                self._attributes['history'][key] = array(
                    [self._attributes[key]])

        # Walks through every entry in extra parameter and append to history.
        if isinstance(extra, dict):
            for key, value in extra.items():
                try:
                    self._attributes['history'][key] = (
                        append(
                            self._attributes['history'][key],
                            [value],
                            axis=0
                        )
                    )
                except:
                    self._attributes['history'][key] = array([value])
        elif extra is not None:
            raise ValueError('Invalid data for extra values.')

    def history(self, id=None, keys=None):
        """
        Returns history according to individual id and variable key.

        Parameters
        ----------
        id : int, optional
            Array index for tracking a specific individual.
        keys : list, optional
            List of keys to return, if not set returns all monitored
            parameters.

        Returns
        -------
        H : dictionary
            Dictionary with arrays of each selected parameter in
            individual's history.

        """
        H = self._get_attribute('history')
        if (keys is None) & (id is None):
            return self._get_attribute('history')
        elif keys is None:
            keys = H.keys()
        elif isinstance(keys, basestring):
            keys = [keys]
        #
        if id is None:
            return dict((key, value) for (key, value) in H.iteritems()
                        if key in keys)
        else:
            return dict((key, value[:, 0]) for (key, value) in H.iteritems()
                        if key in keys)

    def size(self):
        """Returns the size of the community."""
        return len(self.t)

    # Default properties (attributes) for each individual.
    @property
    def group(self):
        """Group to which the individual belongs to."""
        return self._get_attribute('group')

    @group.setter
    def group(self, a):
        self._set_attribute('group', a)

    @property
    def birthday(self):
        """Birthday."""
        return self._get_attribute('birthday')

    @birthday.setter
    def birthday(self, a):
        self._set_attribute('birthday', a)

    @property
    def birthplace(self):
        """Birthplace."""
        return self._get_attribute('birthplace')

    @birthplace.setter
    def birthplace(self, a):
        self._set_attribute('birthplace', a)

    @property
    def t(self):
        """Time (age)."""
        return self._get_attribute('t')

    @t.setter
    def t(self, a):
        self._set_attribute('t', a)

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
        """Vertical coordinate."""
        return self._get_attribute('z')

    @z.setter
    def z(self, a):
        self._set_attribute('z', a)

    @property
    def domain(self):
        """Domain."""
        return self._get_attribute('domain')

    @domain.setter
    def domain(self, a):
        self._set_attribute('domain', a)

    @property
    def u(self):
        """Zonal velocity."""
        return self._get_attribute('u')

    @u.setter
    def u(self, a):
        self._set_attribute('u', a)

    @property
    def v(self):
        """Meridional velocity."""
        return self._get_attribute('v')

    @u.setter
    def v(self, a):
        self._set_attribute('v', a)

    @property
    def w(self):
        """Vertical velocity."""
        return self._get_attribute('w')

    @w.setter
    def w(self, a):
        self._set_attribute('w', a)

    @property
    def in_domain(self):
        """Boolean to check if individual is inside the domain."""
        return self._get_attribute('in_domain')

    @in_domain.setter
    def in_domain(self, a):
        self._set_attribute('in_domain', a)

    @property
    def id(self):
        """Helper attribute to identify individuals."""
        return self._get_attribute('id')

    @id.setter
    def id(self, a):
        self._set_attribute('id', a)


class Plankton(Individual):
    """
    Class that characterizes a group of individual plankton cells from
    a specific specias.

    Formulation is base on the phytoplankton growth model by Bisset
    et al. (1999).

    References
    ----------
    Bissett, W. P.; Walsh, J. J.; Dieterle, D. A. & Carder, K. L.
    Carbon cycling in the upper waters of the Sargasso Sea: I.
    Numerical simulation of dif ferential carbon and nitrogen fluxes
    Deep Sea Research, 1999, 46, 205-269.

    Bissett, W. P.; DeBra, S. & Dye, D. Ecological Simulation
    (EcoSim) 2.0 Technical Description Florida Environmental
    Research Institute -- FERI, FERI-2004-0002-U-D, 2004.

    """
    def __init__(self, log_parameters=[], **kwargs):
        # Runs Individual.__init__ for default object initialization.
        super(Plankton, self).__init__(**kwargs)
        # Some parameters and initializations
        self.state_parameters = ['t', 'x', 'y', 'z', 'P', 'N_P']
        # ... history list
        self._attributes['history'] = dict()
        # ... log list
        n = self.size()
        extra = {key: [nan] * n for key in log_parameters}
        # Start history log
        self.append_history(extra=extra)
        # Assumes every individual is inside the model domain
        self.in_domain = bool_(self.x) | bool_(self.y)

    ###########################################################################
    # Some functions
    ###########################################################################
    def alpha(self):
        """Calculates the photosynthetic efficiency of the individual."""
        return 0.1 * ones(self.size())

    def mu(self, mu_mt, E_0, alpha, mask=True):
        """
        Calculates the effective growth rate.

        Parameters
        ----------
        T : float, array like
            Water temperature (in degrees Celsius).
        E_0 : float, array like
            Scalar irradiance.
        alpha : float, array like
            Photosynthetic efficiency.
        mask : boolean, array like
            Data mask.

        Returns
        -------
        mu, mu_ll, mu_nl : float, array like
            Effective, light-limited and nutrient-limited growth rates.

        """
        # Calculates light limited growth rate according to Jassby and
        # Platt (1976).
        mu_ll = self.mu_ll(mu_mt, E_0, alpha)
        mu_nl = self.mu_nl(mu_mt)
        #
        mu = mu_ll * (mu_ll < mu_nl) + mu_nl * (mu_ll >= mu_nl)
        #
        return mu * mask, mu_ll * mask, mu_nl * mask

    def mu_mt(self, T):
        """Calculates maximum carbon specific growth rate"""
        return self.mu_m * exp(0.0633 * (T - 27.))

    def mu_ll(self, mu_mt, E_0, alpha):
        """Calculates light-limited growth rate."""
        # 1. Calculates the light-limited growthrate according to Jassby &
        #    Platt (1976). Considers only E_0 > E_0_cp.
        _JP76 = tanh(alpha * only_positive(E_0 - self.E_0_cp) / mu_mt)
        # 2. Make sure that photoinhibition only occurs when E_0 > E_0_inb
        _photoinhibition = exp(-self.d_r * only_positive(E_0 - self.E_0_inb))
        # 3. The light limited growth-rate.
        mu_ll = mu_mt * _JP76 * _photoinhibition
        return mu_ll

    def mu_nl(self, mu_mt):
        """Calculates nutrient-limited growth rate."""
        # 1. Maximum nutrient-limited growth rate as a function of the maximum
        #    carbon specific growth rate, subsistence N:C ratio and maximum
        #    N:C ratio.
        mu_nl_max = mu_mt / (1 - self.K_Q_N / self.Q_m_N)
        # 2. Nutrient-limited growth rate as a function of maximum
        # nutrient-limited growth rate, current particulate nitrogen to carbon
        # ratio (N_P:C) and subsistence N:C ratio.
        return mu_nl_max * only_positive(1 - self.K_Q_N / self.Q_N())

    def Q_N(self):
        """Returns current particulate nitrogen to carbon ratio."""
        return self.N_P / self.P

    def rho_NO3(self, mu_mt, NO3, NH4):
        """Calculates nitrate transport flux."""
        return (mu_mt * self.N_P * (NO3 / (self.K_s_NO3 + NO3)) *
                exp(-self.Psi * NH4))

    def rho_NH4(self, mu_mt, NH4):
        """Calculates ammonium transport flux."""
        return mu_mt * self.N_P * (NH4 / (self.K_s_NH4 + NH4))

    ###########################################################################
    # Plankton properties (attributes)
    ###########################################################################
    @property
    def P(self):
        """Plankton biomass."""
        return self._get_attribute('P')

    @P.setter
    def P(self, a):
        self._set_attribute('P', a)

    @property
    def N_P(self):
        """Particulate nitrogen."""
        return self._get_attribute('N_P')

    @N_P.setter
    def N_P(self, a):
        self._set_attribute('N_P', a)

    @property
    def C_Chla(self):
        """Carbon to chlorophyll-a ratio."""
        return self._get_attribute('C_Chla')

    @C_Chla.setter
    def C_Chla(self, a):
        self._set_attribute('C_Chla', a)

    @property
    def r(self):
        """Respiration rate."""
        return self._get_attribute('r')

    @r.setter
    def r(self, a):
        self._set_attribute('r', a)

    @property
    def mu_m(self):
        """Maximum carbon specific growth rate."""
        return self._get_attribute('mu_m')

    @mu_m.setter
    def mu_m(self, a):
        self._set_attribute('mu_m', a)

    @property
    def E_0_cp(self):
        """Compensation irradiance."""
        return self._get_attribute('E_0_cp')

    @E_0_cp.setter
    def E_0_cp(self, a):
        self._set_attribute('E_0_cp', a)

    @property
    def E_0_inb(self):
        """Photo-inhibition irradiance."""
        return self._get_attribute('E_0_inb')

    @E_0_inb.setter
    def E_0_inb(self, a):
        self._set_attribute('E_0_inb', a)

    @property
    def d_r(self):
        """
        Exponential decay coefficient of light-limited growth rate from
        light inhibition.

        """
        return self._get_attribute('d_r')

    @d_r.setter
    def d_r(self, a):
        self._set_attribute('d_r', a)

    @property
    def phi_m(self):
        """Maximum quantum yield."""
        return self._get_attribute('phi_m')

    @phi_m.setter
    def phi_m(self, a):
        self._set_attribute('phi_m', a)

    @property
    def Q_m_N(self):
        """Maximum nitrogen to carbon ratio."""
        return self._get_attribute('Q_m_N')

    @Q_m_N.setter
    def Q_m_N(self, a):
        self._set_attribute('Q_m_N', a)

    @property
    def K_Q_N(self):
        """Subsistence nitrogen to carbon ratio."""
        return self._get_attribute('K_Q_N')

    @K_Q_N.setter
    def K_Q_N(self, a):
        self._set_attribute('K_Q_N', a)

    @property
    def K_s_NO3(self):
        """Half saturation constant for nitrate uptake."""
        return self._get_attribute('K_s_NO3')

    @K_s_NO3.setter
    def K_s_NO3(self, a):
        self._set_attribute('K_s_NO3', a)

    @property
    def K_s_NH4(self):
        """Half saturation constant for ammonium uptake."""
        return self._get_attribute('K_s_NH4')

    @K_s_NH4.setter
    def K_s_NH4(self, a):
        self._set_attribute('K_s_NH4', a)

    @property
    def Psi(self):
        """Nitrate uptake repression exponent."""
        return self._get_attribute('Psi')

    @Psi.setter
    def Psi(self, a):
        self._set_attribute('Psi', a)

    @property
    def gamma(self):
        """Nitrogen consumption ratio from plankton growth."""
        return self._get_attribute('gamma')

    @gamma.setter
    def gamma(self, a):
        self._set_attribute('gamma', a)
