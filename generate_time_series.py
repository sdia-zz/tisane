#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''

Generating time series
----------------------

A few routines are provided to generate test data from simple equations.
Since there are powerfull packages (for example Dynamics by Helena Nusse
and Jim Yorke) that can generate chaotic data, we have only included a 
minimal selection here.

sce: TISEAN

'''



def henon():
    
    '''
    Makes Henon series

    -l number of points x,y (l=0: infinite) 
    -A parameter a (1.4) 
    -B parameter b (0.3) 
    -X initial x 
    -Y initial y 
    -x number of transients discarded (10000) 


    Prints iterates of the Hénon map to stdout:

    x(n+1) = 1 - a * x(n)^2 + b * y(n)
    y(n+1) = x(n)

    '''

    raise NotImplementedError


def ikeda():

    '''
    Makes Ikeda time series


    -l number of points x,y (l=0: infinite) 
    -A parameter a (0.4) 
    -B parameter b (6.0) 
    -C parameter c (0.9) 
    -R initial Re(z) 
    -I initial Im(z) 
    -x number of transients discarded (10000) 

    Prints iterates of the Ikeda map (Re(z) and Im(z)) to stdout:

                                              i * b   
    z(n+1) = 1 + c * z(n) * exp[ i*a  -  (-------------- )
                                            1 + |z(n)| 

    '''

    raise NotImplementedError


from linear_tools import ar_run

from nonlinear_noise_reduction import makenoise

from nonlinear_noise_reduction import addnoise
