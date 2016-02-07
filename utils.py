#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''

Utilities

Here are some tools for the pre-processing of data which save you
the trouble of writing your own five-line Perl, awk, FORTRAN or C
programs.

'''



def choose():

    '''
    Choose columns and sub-sequences

    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -m number of columns to be read (1) 
    -c columns to be read (1) 
    -o output file name, just -o means file_select 
    -V verbosity level (0 = only fatal errors) 
    -h show this message

    Reads a column from a file starting at -x +1 and writes -l values.
    Output file file_select.

    '''

    raise NotImplementedError


def rescale():

    '''
    This program takes a possibly multivariate time series and rescales 
    it to either a desired interval or to have average zero and/or variance 1.

    Option    Description                         Default
    ----------------------------------------------------------------
    -l#       number of data to use               whole file
    -x#       ignore the first # rows             0
    -m#       # of components to read             1
    -c#       columns to be read                  1,...,# of components
    -z#       Minimum of the rescaled series      0
    -Z#       Maximum of the rescaled series      1
    -a        subtract the average                not set
              (overwrites -Z and -z)

    -v        set the variance to 1               not set
              (overwrites -Z and -z)

    -o[#]     output file name                    without file name: 'datafile'.res
                                                  (or stdin.res if stdin was read)
                                                  If no -o is given stdout is used

    -V#       verbosity level                     1
              0: only panic messages
              1: add input/output messages

    -h        show these options                   none

    '''

    raise NotImplementedError


def rms():

    '''
    Normalise time series and/or compute mean, standard deviation

    -a subtract average 
    -v subtract mean, normalise to unit variance 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -o output file name, just -o means file_a (if -a), file_v (if -v) 
    -V verbosity level (0 = only fatal errors) 
    -h show this message
    
    Prints mean, standard deviation, minimal and maximal value of time series.
    Optionally subtracts mean and normalises to unit variance.

    '''

    raise NotImplementedError


def histogram():

    '''
    This program estimates the scalar distribution of a data set. 
    It computes the distribution at a given number of points in the 
    interval spanned by the data by integrating over a given 
    neighborhood.

    Option    Description                      Default
    ----------------------------------------------------------
    -l#       number of data to use            whole file
    -x#       number of lines to be ignored    0
    -c#       column to be read                1
    -b#       number of base points            50

    -e#       size of the boxes                2/base
              (data are internally 
               rescaled to [0:1])

    Output:
    The first three lines contain 
    1. interval of the data, 
    2. the average of the data and 
    3. the standard deviation of the data.

    The following lines then contain the histogram.

    '''

    raise NotImplementedError


def resample():

    '''
    This program resamples the data with a new sampling time, which 
    can be given as a fraction of the original one via the flag -s. 
    This is achieved by interpolating the data locally by a polynomial 
    of an order given by the -p flag.

    Remark: Of course, this program only makes sense for time continous 
            systems.

    Option    Description                    Default
    -------------------------------------------------------
    -l#       number of data to use          whole file
    -x#       number of lines to be ignored  0
    -c#       column to be read              1

    -s#       new sampling time in units     0.5
              of the original one

    -p#       order of the polynomial for    4
              the interpolation

    Output:
    Just one column: The resampled time series.

    '''

    raise NotImplementedError


def intervals():

    '''
    Convert event times to inter-event intervals

    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -o output file name, just -o means file_ss 
    -V verbosity level (0 = only fatal errors) 
    -h show this message

    Takes a sequence of event times and differences it to give 
    inter-event intervals.

    '''

    raise NotImplementedError


def events():

    '''
    Convert inter-event intervals to event times
    
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -o output file name, just -o means file_st 
    -V verbosity level (0 = only fatal errors) 
    -h show this message

    Takes a sequence if inter-event intervals and accumulates 
    it to give event times. 

    '''

    raise NotImplementedError
