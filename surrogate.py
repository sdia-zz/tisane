#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''

Surrogate data

Before attempting any sophisticated nonlinear time series analysis, 
one should try to establish that nonlinearity is indeed present. 
The most suitable method for this is the approach of surrogate data. 
We present two schemes for the generation of surrogate time series, 
one using iterative adjustments of spectrum and distribution, and a 
very general framework for constrained randomization that is based on 
combinatorial minimization of a cost function. The latter approach is 
more like a toolbox, a starting point for your own ideas on suitable 
null hypotheses etc. A few basic discriminating statistics are also 
provided.

There is a short overview page for nonlinearity tests. There is also a 
section in the introduction paper.

'''


def surrogates():

    '''
    Make surrogate data, also multivariate

    -n number of surrogates (1) 
    -i number of iterations (until no change) 
    -S make spectrum exact rather than distribution 
    -I seed for random numbers 
    -o output file name, just -o means file_surr(_nnn) 
    -l number of points (whole file) 
    -x number of values to be skipped (0) 
    -m number of columns to be read (1) 
    -c columns to be read (1) 


    Reads data from a file and creates surrogate data with the same
    Fourier amplitudes and the same distribution of values. If more than
    one columns are specified by either giving their number with -m or a
    comma seperated list with -c, multivariate surrogates are prepared. In
    that case, also the relative Fourier phases of the channels are
    matched to those of the data. Since for finite length, distribution
    and spectral properties cannot be guaranteed exactly at the same time,
    the default output contains the iteration stage with the exact
    amplitudes. With the option -S set, the stage with the exact spectrum
    (resp. relative phases) is given. Asymptotically, the difference
    between both should converge to zero.  The setting -i0 yields a random
    permutation, or, if the option -S set, an unrescaled FFT
    surrogate. The setting -i1 yields a surrogate that is close to the
    result of the AAFT procedure, but not quite the same.

    Surrogates are written to stdout by default. With the -o option to
    file_surr_n, n=1...number. For each surrogate, the iteration count
    and the rms discrepancy between the exact spectrum and exact
    amplitude stages (normalised to the rms amplitude of the data) are
    printed.

    Note: The length of the sequence will be truncated to the largest
    sub-sequence factorizable with factors 2,3, and 5. This is
    necessary in order to use an efficient FFT.

    Note: It is advisable to select a suitable sub-sequence to
    minimize end effects by using endtoend before preparing
    surrogates. By no means should the data be zero-padded.

    Note: Successive identical calls to this routine will always yield
    the same surrogates, since "random" numbers on a computer are
    deterministic. It is, however, possible to set the seed of the random
    number generator explicitly by using the option -I , so that calls
    with different seeds yield different surogates.

    See also the page on nonlinearity testing.
    
    This routine is based on:

        T. Schreiber and A. Schmitz 
        Improved surrogate data for nonlinearity tests 
        Phys. Rev. Lett. 77, 635 (1996).

    '''

    raise NotImplementedError


def end_to_end():

    '''
    Determine end-to-end mismatch before making surrogate data

    -o output file name, just -o means file_end 
    -l number of points (whole file) 
    -x number of values to be skipped (0) 
    -m number of columns to be read (1) 
    -c columns to be read (1) 

    Determine the effect of an end-to-end mismatch on the
    autocorrelation structure for various sub-sequence lenths. It is
    important to avoid jumps and phase slips that occur when the data
    is periodically continued when making Fourier based surrogates,
    e.g. with surrogates.  The mismatch in value is measured by

              /           \ 2
              | x(1)-x(N) |
              \           /
    d     = __________________
     jump     __
             \   /      _ \ 2
              |  | x(n)-x | 
             /__ \        /
        
    and the phase slip by

             /                           \ 2
             | (x(2)-x(1))-(x(N)-x(N-1)) |
             \                           /
    d     = _________________________________
     slip       __                         .
               \   /      _ \ 2
                |  | x(n)-x | 
               /__ \        /
    
    The weighted mismatch is then

      j*d     + (1-j)*d     .
         jump          slip

    In the multivariate case, the values of d are computed for each
    channel seperately and then averaged.  

    The sub-sequence length is successively decreased, only
    considering lengths which can be factorized with factors 2, 3 and
    5 (that is what surrogates can handle). For each length, the
    optimal time offset is determined and a result is printed whenever
    an improvement was found. You can then use the -x and -l options
    to choose that sub-sequence for surrogates.
    
    '''

    raise NotImplementedError


def randomize():

    '''
    General constrained randomization

    TODO: move to specific RANDOM package.

    See the paper for an introduction to general constrained
    randomization of time series. This page describes an extendable
    family of routines for the generation of annealed surrogate data.


    Current members of the family:

    1. Standard nonlinearity tests
       * randomize_auto_exp_random
       * randomize_autop_exp_random
    2. Nonlinearity test for unevenly sampled time series
       * randomize_uneven_exp_random

    3. Nonlinearity test for event time sequences
       * randomize_spikeauto_exp_random
       * randomize_spikespec_exp_event

    Generic calling sequence

    randomize_cost_cool_perm [-n# -u# -I# -o outfile -l# -x# -c#[,#] -m# -V# -h] 
    [cost function options] [cooling options] [permutation options] file

    -n number of surrogates (default 1) 
    -u improvement factor before write (default 0.9 = if 10% better) 
    -I seed for random numbers (0) 
    -l maximal number of points to be processed (default all) 
    -x number of values to be skipped (0) 
    -c columns to be read (1 or file,#) 
    -m number of components (ignored for scalar data) 
    -o output file name, just -o means file_rnd(_nnn) 

    The variables cost, cool, and perm expand to one of the
    implemented cost functions, cooling schemes, and permutation
    schemes. Each of these may have their specific options which are
    described under each module. In general, a one-column file is read
    and the values are permuted randomly under certain
    constraints. These constraints are usually (but not necessarily)
    derived from the data and implemented in the form of a cost
    function which is minimized by the method of simulated annealing.

    Output is written to file_rnd_nnn, n=1...number, also at
    intermediate stages specified by -u.

    This family of routines is based on

    T. Schreiber 
    Constrained randomization of time series data 
    Phys. Rev. Lett. 80, 2105 (1998).

    '''

    raise NotImplementedError


def timerev():

    '''
    Time reversal asymmetry statistic

    -d delay (1) 
    -l number of points (whole file) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -V verbosity level (0 = only fatal errors) 
    -h show this message

    Computes the time reversal asymmetry statistic:
                     3
        < (y  - y   )  >
            n    n-d
       ------------------
                     2
        < (y  - y   )  >
            n    n-d

    '''

    raise NotImplementedError


def predict():
    
    '''
    Simple nonlinear prediction

    -d delay 
    -m embedding dimension 
    -r absolute radius of neighbourhoods 
    -v same as fraction of standard deviation 
    -s time steps ahead forecast (one step) 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -o output file name, just -o means file_pred 
    -V verbosity level (0 = only fatal errors) 
    -h show this message

    Performs locally constant predictions on scalar time series and
    prints the root mean squared prediction error. Predictions are
    made a time ahead given by -s. Either -r or -v must be
    present. Predictions are written to file_pred.

    Note: A version of fclazy is used that implements fast neighbour
    search (not like in the book).

    See also zeroth which does essentially the same but has some
    different options, including multivariate data, and xzero, which
    does cross-predictions.

    '''

    raise NotImplementedError
