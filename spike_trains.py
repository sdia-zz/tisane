#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''
Spike trains

Sequences of times of singular events (heart beats, neuronal spikes etc.), 
or sequences of intervals between such events (RR-intervals etc.) require 
specialised techniques, even for their linear analysis. Below find a list 
of routines that may proove useful for this type of data.

'''


# def intervals():
from utils import intervals 


# def events():
from utils import events


def spike_auto():

    '''
    Spike train autocorrelation function

    -d time span of one bin 
    -D total time spanned 
    -i expect intervals rather than times 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -o output file name, just -o means file_co 
    -V verbosity level (0 = only fatal errors) 
    -h show this message

    Computes the binned autocorrelation function of a series of event
    times (With the flag -i set, the data is taken to be inter-event
    intervals rather than event times.) The data is assumed to
    represent a sum of delta functions centered at the times
    given. The autocorrelation function is then a double sum of delta
    functions which must be binned to be representable. Therfore, you
    have to choose the duration of a single bin -d and the maximal
    time lag -D considered.

    '''

    raise NotImplementedError


def spike_spec():

    '''
    Power spectrum of inter-event intervals

    -F maximal frequency (2*l / total time) 
    -# number of frequencies (F* total time /2) 
    -w frequency resolution (0) 
    -i expect intervals rather than times 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -o output file name, just -o means file_sp 
    -V verbosity level (0 = only fatal errors) 
    -h show this message

    Computes a power spectrum assuming that the data are the times of
    singular events, e.g. heart beats. With the flag -i set, the data
    is taken to be inter-event intervals rather than event times. If
    the event times are t(n), n=1,...,l, the spectrum is defined by :

              l                     2
           | ---                  |
           | \     -i 2 pi f t(n) |
    S(f) = |  |  e                |
           | /                    |
           | ---                  |
             n=1

 
    that is, the signal is taken to be a sum of delta functions at the t(n). 
    S(f) is computed for # frequencies between 0 and -F . The result is binned 
    down to a frequency resolution -w . Output file file_ss (frequency, spectrum).

    '''

    raise NotImplementedError


'''
General constrained randomization:
Nonlinearity test for event time series

There are two specific calling sequence to generate surrogates with
the same inter-event interval correlations (or spectrum) and the same
distribution of inter-event intervals as the data. The corresponding
null hypothesis is that all the serial correlations in the data are
represented by the autocorrelation function (resp. the power spectrum)
and the histogram of inter-event intervals. For the definition of the
inter-event interval autocorrelation function (resp. the power
spectrum) see spikeauto (resp. spikespec).
'''

def randomize_spike_auto_exp_random():

    '''
    Spike train autocorrelations
    Read somewhere : Surrogates data preserving event time autocorrelation

    The recommended calling sequence uses the inter-event time
    autocorelation function, binned to a given resolution and computed
    up to a given lag:


    -d time span of one bin 
    -D total time spanned 
    -i expect intervals rather than times 
    -W type of average: 0=max(c), 1=|c|/lag, 2=(c/lag)**2 (default 0) 
    -n number of surrogates (default 1) 
    -u improvement factor before write (default 0.9 = if 10% better) 
    -I seed for random numbers (0) 
    -l maximal number of points to be processed (default all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -T initial temperature (default: automatic melting) 
    -a cooling factor (default automatic) 
    -S total steps before cooling (default 20000) 
    -s successful steps before cooling (default 2000) 
    -z minimal successful steps (default 200) 
    -C goal value of cost function (default zero)

    '''

    raise NotImplementedError


def randomize_spike_spec_exp_event():

    '''
    Spike train spectra
    Also: Surrogates data preserving event time power spectrum

    -F maximal frequency (2*l / total time) 
    -# number of frequencies (F* total time /2) 
    -i expect intervals rather than times 
    -W type of average: 0=max(s) 1=|s|/f 2=(s/f)**2 3=|s| (default 0) 
    -n number of surrogates (default 1) 
    -u improvement factor before write (default 0.9 = if 10% better) 
    -I seed for random numbers (0) 
    -l maximal number of points to be processed (default all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -T initial temperature (default: automatic melting) 
    -a cooling factor (default automatic) 
    -S total steps before cooling (default 20000) 
    -s successful steps before cooling (default 2000) 
    -z minimal successful steps (default 200) 
    -C goal value of cost function (default zero)

    Note: if neither -a nor -C are given, the annealing will keep
    starting over with slower cooling rates. This may be necessary if
    good guesses are not available but of course, multiple surrogates
    will have to be made by further separate calls.

    '''

    raise NotImplementedError

