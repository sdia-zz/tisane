#!/usr/bin/env python
#-*- coding:utf-8 -*-



'''
Lyapunov exponents

Lyapunov exponents are an important means of quantification for 
unstable systems. They are however difficult to estimate from a 
time series. Unless low dimensional, high quality data is at hand, 
one should not attempt to calculate the full spectrum. Try to 
compute the maximal exponent first. The two implementations differ 
slightly. While lyap_k implements the formula by Kantz, lyap_r uses 
that by Rosenstein et al. which differs only in the definition of 
the neighbourhoods. We recommend to use the former version, lyap_k.

The estimation of Lyapunov exponents is also discussed in the 
introduction paper. A recent addition is a programm to compute 
finite time exponents which are not invariant but contain 
additional information.

'''


def lyap_k():
    "Maximal exponent"
    raise NotImplementedError


def lyap_r():
    "Maximal exponent"
    raise NotImplementedError


def lyap_spec():
    "Lyapunov spectrum"
    raise NotImplementedError


def fsle():
    "Finite size exponents"
    raise NotImplementedError
