#!/usr/bin/env python
#-*- coding:utf-8 -*-




'''
Multivariate time series

TISEAN's multivariate section is still growing - like the research body 
in this area. As a convention, program names for ``cross-'' quantities 
computed between two signals start with x. Those programs that can handle 
scalar as well as multivariate data don't follow any name convention.

Currently, three (cross-) similarity measures are available, a linear and 
two nonlinear ones. Further, there is a zeroth order predictor using 
multivariate embeddings. A few general routines that can handle 
multivariate data are also mentioned below. Note in particular the 
multivariate surrogate data generator, the Grassberger-Procaccia 
correlation sum, and the fixed mass D1 estimator.

The general convention for column selection is as follows. Columns can 
be given as a comma seperated list with the option -c#[,#] . Wherever 
the number of columns is selectable, this can be done with the option 
-m# or the first number in its argument. The precedence of these settings 
are as follows:

-m overrides -c
-c overrides the default only if more columns are specified.

Exceptions to this general convention are possible and mentioned in the 
specific program descriptions.


'''

def ar_model():
    "Multivariate linear model"
    raise NotImplementedError


def makenoise():
    "Multivariate noise generation"
    raise NotImplementedError


def xcor():
    "Linear cross-correlations"
    raise NotImplementedError


def extrema():
    "Extrema of a multivariate signal"
    raise NotImplementedError


def sav_gol():
    "Savitzky-Golay filter"
    raise NotImplementedError


def recurr():
    "Recurrence plot"
    raise NotImplementedError


def xzero():
    "Nonlinear cross-prediction"
    raise NotImplementedError


def xc2():
    "Cross-correlation integral"
    raise NotImplementedError


def d2():
    "Correlation integral, also for multivariate data"
    raise NotImplementedError


def c1():
    "Fixed mass approach to D1, also for multivariate data"
    raise NotImplementedError


def lyap_spec():
    "Lyapunov spectra"
    raise NotImplementedError


def box_count():
    "Renyi entropies"
    raise NotImplementedError


def zeroth():
    "Zeroth order prediction on multivariate time series"
    raise NotImplementedError


def nstep():
    "Locally linear prediction on multivariate time series"
    raise NotImplementedError


def compare():
    "Compare two signals"
    raise NotImplementedError


def choose():
    "Choose sub-sequence or columns"
    raise NotImplementedError


def surrogates():
    "Make surrogate data, also multivariate"
    raise NotImplementedError


def end_to_end():
    "Determine end-to-end mismatch, also multivariate"
    raise NotImplementedError

