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

    '''
    Maximal exponent

    The program estimates the largest Lyapunov exponent of a given
    scalar data set using the algorithm of Kantz.


    Output

    Option    Description                    Default
    ------------------------------------------------------------
    -l#       number of data to be used      whole file
    -x#       number of lines to be ignored  0
    -c#       column to be read              1

    -M#       maximal embedding dimension    2
              to use

    -m#       minimal embedding dimension    2
              to use

    -d#       delay to use                   1

    -r#       minimal length scale to        (data interval) / 1000 
              search neighbors
    -R#       maximal length scale to        (data interval) / 100
              search neighbors

    -##       number of length scales        5
              to use

    -n#       number of reference points     all
              to use

    -s#       number of iterations in        50
              time

    -t#       'theiler window'               0
    ------------------------------------------------------------


    Output

    For each embedding dimension and each length scale the file
    contains a block of data consisting of 3 columns

    1. The number of the iteration

    2. The logarithm of the stretching factor (the slope is the
       Lyapunov exponent if it is a straight line)

    3. The number of points for which a neighborhood with enough
       points was found

    '''

    raise NotImplementedError


def lyap_r():
    
    '''
    Maximal exponent

    The program estimates the largest Lyapunov exponent of a given
    scalar data set using the algorithm of Rosenstein et al.


    Usage

    Option    Description                        Default
    ----------------------------------------------------------------
    -l#       number of data to be used          whole file
    -x#       number of lines to be ignored      0
    -c#       column to be read                  1
    -m#       embedding dimension to use         2
    -d#       delay to use                       1

    -t#       window around the reference        0
              point which should be omitted

    -r#       minimal length scale for the       (data interval) / 1000
              neighborhood search

    -s#       number of iterations in time       50
    ----------------------------------------------------------------

    
    Output

    First column: Number of the iteration
    Second column: Logarithm of the stretching factor

    '''

    raise NotImplementedError


# def lyap_spec():
from multivariate import lyap_spec


def fsle():

    '''
    Finite size exponents

    The program estimates the finite size Lyapunov exponents as
    proposed in Aurell et al. [1]

    Remark: I should mention that this program is still in an early
    beta state.  raise NotImplementedError

    [1] http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/chaospaper/citation.html#aurell97


    Usage

    Option    Description                      Default
    --------------------------------------------------------------
    -l#       number of data to be used        whole file
    -x#       number of lines to be ignored    0
    -c#       column to be read                1
    -m#       embedding dimension to use       2
    -d#       delay to use                     1

    -t#       window around the reference      0
              point which should be omitted

    -r#       minimal length scale for the     (std. dev. of data) / 1000
              neighborhood search
    --------------------------------------------------------------


    Output

    First column: length scale in natural (data) units
    Second column: Estimate finite size Lyapunov exponent
    Third column: Number of points used for this length scale
    
    '''

    raise NotImplementedError
