#!/usr/bin/env python
#-*- coding:utf-8 -*-




'''

Dimension and entropy estimation

If you are looking for a program that reads your signal and issues 
a number that says "correlation dimension", you got yourself the 
wrong package. We think you are still better off than getting such 
a wrong answer. The programs in this section carry out the 
calculations necessary to detect scaling and self similarity in a 
fractal attractor. You will have to establish scaling and eventually, 
in favourable cases, extract the dimension or entropy by careful 
evaluation of the data produced by these programs.

There are two alternative implementations of the Grassbeger-Procaccia 
correlation integral in this package. The program d2 by Rainer Hegger 
to our knowledge is the fastest and most reliable implementation that 
is currently available. It can also handle multivariate data and mixed 
embeddings. For the very conservative, there is a slow but simple 
alternative called c2naive that works on scalar data only. 
Post-processing can be performed on the output in order to obtain 
Takens' estimator or the Gaussian kernel correlation integral, or just 
for smoothing.

A fixed mass algorithm for the information dimension D1 is available 
which also can handle multivariate data and mixed embeddings, and a 
box-counting implementation of the order Q Renyi entropies for 
multifractal studies.

You may want to consult the introduction paper for initial material 
on dimension estimation. If you are serious, you will need to study 
some of the literature cited there as well.

'''


from multivariate import d2


def av_d2():

    '''
    Correlation integral

    This program takes one of the output files of the d2, c1, or
    c2naive programs as its input and smoothes the content of the file
    by arithmetically averaging over a given interval. Furthermore, it
    is possible to specify a range of embedding dimensions to be
    printed. In the case of d2 output, the application of av-d2 makes
    most sense on the local slopes file (extension .d2).


    Suppose the input file contained values ri and di, then the output
    will be in two columns



                      __ a
                 1    \
        r    ,  ----   |       d
         i      2a+1  /__ j=-a  i-j


    where a is the argument to the -a option. We recommend to
    experiment with the parameter a for optimal results.


    Usage

    Option    Description                    Default
    -------------------------------------------------------
    -m#       minimal dimension to print     1
    -M#       maximal dimension to print     whole file

    -a#       smooth over an interval of     1
              2#+1 points

    -E        show the length scales in      units of the data
              rescaled units [0:1]
    -------------------------------------------------------


    Output

    The output is the same as the one from the d2 and c2naive
    programs. The only difference is that the output is smoothed.

    Other post-processing for correlation sum data is available: c2d
    computes local slopes from correlation sum data (extension .c2) by
    fitting straight lines. This is essentially redundant with the
    present program. Takens' estimator can be obtained using c2t while
    c2g provides Gaussian kernel correlation integrals. Both act on
    the correlation sum data (extension .c2).

    '''

    raise NotImplementedError


def c2_naive():

    '''
    Correlation integral


    Usage

    -d delay 
    -M maximal embedding dimension 
    -t minimal time separation 
    -m minimal embedding dimension (1) 
    -# resolution, values per octave (2) 
    -T for Guido 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 


    Determines the correlation sums of scalar time series in
    file(s). A file named file_c2 is produced containing all the
    embedding dimensions seperated by blank lines. No fast neighbour
    search is applied but all available pairs are evaluated.

    Note: You will probably use one of the auxilliary programs c2d,
    c2t, or c2g to process the output further.
    
    Note: For longer signals, the program is much slower than the
    version d2 that uses fast neighbour search.

    '''

    raise NotImplementedError


def c2d():

    '''
    Correlation integral

    Local slopes from correlation sums


    Usage

    -o output file name, just -o means file_d 
    -a average using -#,...,+# (1) 
    -V verbosity level (0 = only fatal errors) 
    -h show this message

    Reads two columns, r(i), c(i) from file (correlation integral
    output of c2naive, c1, or d2) and computes local slopes by fitting
    straight lines. The range of the fits is specified by the option
    -a . For the local slope at abscissa r(i), the values c(i-a), ...,
    c(i+a) are used, where a is the argument to the -a option.

    Alternatives to local slopes are Takens' estimator c2t or to use
    Gaussian kernel smoothing c2g before computing slopes.

    '''

    raise NotImplementedError


def c2t():

    '''
    Takens estimator

    Maximum likelihood estimator from correlation sums

    Reads two columns, r, c(r) from file (correlation integral output
    of c2naive, c1, or d2) and computes a maximum likelihood estimator
    (Takens' estimator)

                    C(r)
         D (r) = ------------
          T       /r    C(x)
                 |  dx ------
                 /0      x


    as a function of the upper cutoff length scale. The integral is
    computed from the discrete values of C(r) by assuming an exact
    power law between the available points. Output is to stdout, or to
    file file_t if -o is given.

    '''

    raise NotImplementedError

from multivariate import c1

from multivariate import box_count
