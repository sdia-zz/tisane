#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''
Linear tools

This section contains some rather basic implementations of linear 
time series methods which are there just for convenience. If you 
want to embark seriously on linear or spectral analysis of your 
data, you will have to use any one of the statistical or mathematics 
packages around. Please, don't judge us by the level of sophistication 
in this section!

sce: TISEAN

'''


from multivaritate import ar_model


def ar_run():
    '''
    Run autoregressive model

    -l number of iterations (l=0: infinite) 
    -p order of AR-model (default determined from input) 
    -I seed for random numbers 
    -x number of transients discarded (10000) 
    -o output file name, just -o means ar.dat 
    -V verbosity level (0 = only fatal errors) 
    -h show this message

    Prints iterates of an autoregressive model
    xn=a1xn-1+...+apxn-p + noise.
    to stdout. 

    The coefficients are read from file. The format is either one line
    containing the rms amplitude of the increments and one for each of
    the coefficients, or alternatively the output of ar-model.
    '''

    raise NotImplementedError


def corr():
    
    '''
    Autocorrelation function

    This program computes the autocorrelation of a scalar data
    set. Depending on whether the -n flag is set or not, different
    normalizations are applied. With -n not set the definition is:


    http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/docs_c/corr_eq1.gif

    where s is the standard deviation of the data and y its
    average. Else it is

    http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/docs_c/corr_eq2.gif


    Usage:

    Option    Description                     Default
    -------------------------------------------------------
    -l#       number of data to use           whole file
    -x#       number of lines to be ignored   0
    -c#       column to be read               1
    -D#       number of correlations          100

    -n        don't use normalization to      not set
              standard deviation
    -------------------------------------------------------

    Output:
    
    The first two lines contain: 1. the average and 2. the standard
    deviation of the data. The following lines are the
    autocorrelations (first column: delay, second column:
    autocorrelation).

    '''
    raise NotImplementedError


def autocorr():
    '''
    Autocorrelation function

    Usage:

    -v give unnormalised autocovariance 
    -p assume periodic continuation 
    -P assume periodic continuation exactly 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 

    Computes the autocorrelation (or with -v the autocovariance)
    function of a time series. This routine uses the FFT for
    convolution and should thus asymptotically be faster than corr. By
    default, zero padding is used, that is, no periodic continuation
    is assumed. With the option -P, it is assumed that the data is
    exactly one period of a periodic function. If the number of data
    points is not factorisable with factors of 2,3, or 5, a slow
    Fourier transform would have to be used. Therefore, with the
    option -p, approximate periodicity can be imposed by finding the
    largest part of the time series that is thus factorisable.
    '''
    raise NotImplementedError


from spike_trains import spike_auto


def mem_spec():

    '''
    Power spectrum

    This program estimates the power spectrum of a scalar data set on
    the basis of the maximum entropy principle. A description of the
    method is printed in the Numerical Recipes, whereas the present
    implementation is new.

    Usage:

    Option    Description                         Default
    -------------------------------------------------------------
    -l#       number of data to use               whole file
    -x#       number of lines to be ignored       0
    -c#       column to be read                   1
    -p#       number of poles                     128
    -f#       number of frequences to print       number of poles
    -------------------------------------------------------------

    Output:

    The first line shows the average forecast error of the AR-model
    fitted. The following p lines contain the coefficients of the
    fitted AR-model and the last f lines contain the power spectrum.

    '''
    
    raise NotImplementedError


def spectrum():

    '''
    Power spectrum

    Usage:

    -f sampling rate (e.g. in Hz, default 1.) 
    -w frequency resolution (e.g. in Hz, default 1/N) 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 

    Computes a power spectrum by binning adjacent frequencies
    according to the option -w. Output file file_sp (frequency,
    spectrum).

    '''
    
    raise NotImplementedError


from spike_trains import spike_spec


def notch():
    
    '''
    Notch filter

    Usage:

    -X frequency to be cancelled 
    -f sampling rate of data (1) 
    -w width of filter (f/100) 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 

    Simple notch filter in the time domain. Output file file_notch.

    '''

    raise NotImplementedError


def wiener():
    
    '''
    Wiener filter


    Wiener1
    -------

    -f sampling rate (e.g. in Hz, default 1.) 
    -w frequency resolution (e.g. in Hz, default 1/N)> 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 



    Wiener2
    -------

    -f sampling rate (e.g. in Hz, default 1.) 
    -w frequency resolution (e.g. in Hz, default 1/N)> 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -o output file of wiener1, just -o means file_amp 



    Wiener filter. The first call produces the original periodogram on
    stdout (or in file_amp with the -o option). This may then be
    edited to provide the desired periodogram. The second call uses
    file and the output of wiener1 to generate a filtered
    sequence. The final result is written to stdout, or file_wc with
    the -O option). The option setting of -o should be the same for
    both calls. Internally, the series is padded with zeroes in order
    to get a FFT-able number of points. A warning is issued if
    applicable. It is recommended to plot the spectral estimator
    computed by wiener1 in order to adjust the frequency resolution -w
    properly.
    '''
    raise NotImplementedError


def low_121():

    '''
    Simple low pass filter

    This program applies a simple low pass filter in the time
    domain. The filter works as follows: 

    x'n = (xn-1 + 2xn + xn+1) / 4 


    Usage:
    
    Option    Description                     Default
    ----------------------------------------------------
    -l#       number of data to use           whole file
    -x#       number of lines to be ignored   0
    -c#       column to be read               1
    -i#       number of iterations            1
    ----------------------------------------------------


    Output:

    Depending on the the -V flag one or more files are produced. Each
    of the files contains one column, consisting of the filtered time
    series.

    '''

    raise NotImplementedError


from multivariate import sav_gol
