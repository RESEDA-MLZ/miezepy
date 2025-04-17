#  -*- coding: utf-8 -*-
# *****************************************************************************
# Copyright (c) 2017 by the NSE analysis contributors (see AUTHORS)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Module authors:
#   Alexander Schober <alex.schober@mac.com>
#
# *****************************************************************************

from scipy import integrate as integrate
from scipy import constants as co

import iminuit
import numpy as np
import warnings


class CosineMinuit:

    def fitCosine(self, counts, time, freq, error):
        '''
        Creates the minuit fit function and runs
        leastsquarefit.

        Parameters
        ----------
        counts : float array
            The data

        time : float array
            The x abscises so to speak

        freq : float
            The frequency distribution

        error : float array

        Returns
        -------
        fit : iminuit fit structure
        '''
        self.argument_dict = {}
        self.argument_dict['counts'] = counts
        self.argument_dict['time'] = time
        self.argument_dict['freq'] = freq
        self.argument_dict['error'] = error

        minuit_dict = {}
        minuit_dict['phase'] = 0
        minuit_dict['offset'] = np.mean(counts)
        minuit_dict['amplitude'] = np.abs(np.mean(counts) - np.amax(counts))

        fit = iminuit.Minuit(self.cosine, **minuit_dict)
        fit.errordef = iminuit.Minuit.LEAST_SQUARES
        fit.migrad()

        return fit

    def cosine(self, phase, offset, amplitude):
        '''
        Creates the minuit fit function and runs
        leastsquarefit.

        Parameters
        ----------
        phase : float
            Phase of the sinus oscillation

        offset : float
            Offset along the y absice

        amplitude : float
            Amplitude of the sinus oscillation

        Returns
        -------
        fit result : float
        '''
        # with warnings.catch_warnings():
        try:
            return sum((((amplitude*np.cos(self.argument_dict['freq']*t+phase)+offset-c)**2)/e**2 if not e == 0 else np.nan for c, t, e in zip(self.argument_dict['counts'], self.argument_dict['time'], self.argument_dict['error'])))
        except:
            return np.nan


class ExpMinuit:

    def fitExp(self, contrast, SpinEchoTime, contrastError, x_display_axis, input_func):
        '''
        Creates the minuit fit function and runs
        leastsquarefit.

        Parameters
        ----------
        contrast : float array
            The data

        SpinEchoTime : float array
            The x abscises so to speak

        contrastError : float array

        input_func : name of the fitting function

        Returns
        -------
        fit : fit result dictionary
        '''
        self.argument_dict = {}
        self.argument_dict['contrast'] = contrast
        self.argument_dict['SpinEchoTime'] = SpinEchoTime
        self.argument_dict['contrastError'] = contrastError

        self.func_name = input_func

        minuit_dict = {}
        minuit_dict['Gamma'] = 10
        minuit_dict['Amplitude'] = 1
        minuit_dict['Beta'] = 1

        self.fit_functions = {
            'Exp': self.exp,
            'StrExp': self.str_exp,
            'StrExp_Elast': self.str_exp_elast,
            'StrExp_InElast': self.str_exp_inelast,
        }

        fit = iminuit.Minuit(self.cost_func, **minuit_dict)
        if self.func_name == 'Exp': 
            fit.fixed['Amplitude'] = True
            fit.fixed['Beta'] = True
        elif self.func_name == 'StrExp': 
            fit.fixed['Amplitude'] = True
        elif self.func_name == 'StrExp_InElast': 
            fit.fixed['Amplitude'] = True 


        fit.errordef = iminuit.Minuit.LEAST_SQUARES
        fit.migrad()

        params = fit.values
        chi2 = fit.fval

        Gamma = fit.values['Gamma'] if fit.covariance is not None else None
        Amp = fit.values['Amplitude'] if fit.covariance is not None else None
        Beta = fit.values['Beta'] if fit.covariance is not None else None

        cov = fit.covariance
        Cov = np.array(cov).reshape([3, 3]) if fit.covariance is not None else None
        Gammaerr = np.sqrt(Cov[0][0]) if fit.covariance is not None else None
        Amperr = np.sqrt(Cov[1][1]) if fit.covariance is not None else None
        Betaerr = np.sqrt(Cov[2][2]) if fit.covariance is not None else None

        Curve = np.full(len(x_display_axis), np.nan)
        if self.func_name in self.fit_functions:
            Curve = self.fit_functions[self.func_name](Gamma, Amp, Beta, x_display_axis) if fit.covariance is not None else None
        else:
            print(f"Unknown fit function: {self.func_name}")

        return {'Gamma': Gamma,
                'Gamma_error': Gammaerr,
                'Amplitude' : Amp,
                'Amplitude_error' : Amperr,
                'Beta' : Beta,
                'Beta_error' : Betaerr,                
                'Curve': Curve,
                'Curve Axis': x_display_axis}


    def cost_func(self, Gamma, Amplitude, Beta):
        '''
        Gamma exponential fit minimizer function

        Parameters (fitting parameters):
        ----------
        Gamma : float
            Relaxation rate

        Amplitude : float
            Amplitude of the function

        Beta : float
            Stretching parameter

        Returns
        -------
        fit result : float
        '''

        with warnings.catch_warnings():
            try:
                if self.func_name in self.fit_functions:
                    func = self.fit_functions[self.func_name](Gamma, Amplitude, Beta, self.argument_dict['SpinEchoTime'])
                else:
                    print(f"Unknown fit function: {self.func_name}")

                return sum(
                    ((f-c)**2. / e**2.
                     for f, c, e in zip(
                         func,
                         self.argument_dict['contrast'],
                         self.argument_dict['contrastError'])))
            except:
                return np.nan

    def exp(self, Gamma, Amp, Beta, t):
        '''
        Fit function

        Parameters (fitting parameters):
        ----------
        Gamma : float
            Relaxation rate

        Amplitude : float
            Amplitude of the function

        Beta : float
            Stretching parameter

        t : float
            Spin echo time

        Returns
        -------
        fit result : float
        '''
        with warnings.catch_warnings():
            try:
                return (Amp*np.exp(-Gamma*1.e-6*co.e*t*1.e-9/co.hbar))
            except:
                return np.nan
            

    def str_exp(self, Gamma, Amp, Beta, t):
        '''
        Fit function

        Parameters (fitting parameters):
        ----------
        Gamma : float
            Relaxation rate

        Amplitude : float
            Amplitude of the function

        Beta : float
            Stretching parameter

        t : float
            Spin echo time

        Returns
        -------
        fit result : float
        '''
        with warnings.catch_warnings():
            try:
                return (Amp*np.exp(-Gamma*1.e-6*co.e*t*1.e-9/co.hbar)**Beta)
            except:
                return np.nan


    def str_exp_elast(self, Gamma, Amp, Beta, t):
        '''
        Fit function

        Parameters (fitting parameters):
        ----------
        Gamma : float
            Relaxation rate

        Amplitude : float
            Amplitude of the function

        Beta : float
            Stretching parameter

        t : float
            Spin echo time

        Returns
        -------
        fit result : float
        '''
        with warnings.catch_warnings():
            try:
                return (Amp+(1-Amp)*np.exp(-Gamma*1.e-6*co.e*t*1.e-9/co.hbar)**Beta)
            except:
                return np.nan


    def str_exp_inelast(self, Gamma, Amp, Beta, t):
        '''
        Fit function

        Parameters (fitting parameters):
        ----------
        Gamma : float
            Relaxation rate

        Amplitude : float
            Amplitude of the function

        Beta : float
            Stretching parameter

        t : float
            Spin echo time

        Returns
        -------
        fit result : float
        '''
        with warnings.catch_warnings():
            try:
                return (Amp*np.exp(-Gamma*1.e-6*co.e*t*1.e-9/co.hbar)**Beta 
                        * np.cos(-Gamma*1.e-6*co.e*t*1.e-9/co.hbar))
            except:
                return np.nan    





