#!/usr/bin/env python
#-*- coding:utf-8 -*-



'''


Nonlinear noise reduction

This is how the three of us got into this business. Since spectral 
filters are problematic with chaotic, broad band signals, new 
techniques were necessary. All the implementations here use phase 
space projections for noise reduction. The programs nrlazy and 
lazy use locally constant approximations of the dynamics. Rainers 
nrlazy corrects the whole embedding vector, while Thomas' lazy 
corrects only the center point. We haven't quite resolved yet which 
is preferable. The two routines ghkss and project implement locally 
linear projections (very similar). Finally, for testing purposes 
you may want to add noise to data and compare the outcome of your 
cleaning attempts with the true signal.

The introduction paper has a section on nonlinear noise reduction, too.


Ref:
http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/chaospaper/node22.html

'''


def makenoise():

    '''
    Depending on whether the -0 flag is set it either takes (possibly
    multivariate) data and adds a desired amount of noise to it or it
    just creates a series of random numbers with zero mean.


    Usage

    Option    Description                          Default
    ---------------------------------------------------------------
    -l#       number of points to use              whole file
    -x#       number of lines to be ignored        0
    -m#       number of columns to be used         1
    -c#       column(s) to be read                 1
    -%#       noiselevel in percent                5

    -r#       absolute noiselevel (or absolute     not set
              variance if -g is set)

    -g        add gaussian noise instead           uniform
              of uniform

    -I#       change the seed of the random        some fixed value
              number generator
              If # = 0, the seed is taken from
              the time command, which means the
              seed is set to the number of seconds
              since Jan 1st, 1970

    -0        Don't read any data file, just       not set
              generate random numbers with zero
              mean. (Requires -r and -l)
    ---------------------------------------------------------------


    Output

    The output consists of the noisy time series.

    '''

    raise NotImplementedError


def addnoise():

    '''
    Add Gaussian / uniform white noise

    -r absolute noise level 
    -v same as fraction of standard deviation 
    -u add uniform noise (default Gaussian) 
    -0 do not read input, just issue random numbers 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -o output file name, just -o means file_noisy 
    -V verbosity level (0 = only fatal errors) 
    -h show this message


    Adds Gaussian noise of rms amplitude given by -r to data in file(s).
    The amplitude can also be given (-v) as a fraction of the rms amplitude
    of the data. With -u, uniform noise in [0:#] is added, # given by -r or
    -v. Either -r or -v must be present. Output file file_noisy.

    If -0 is given, no input files are read. Instead, -l random numbers of 
    magnitude -r are produced.

    '''

    raise NotImplementedError


def compare():

    '''
    Compare two datasets


    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c columns to be read, comma separated (1,2) 
    -V verbosity level (0 = only fatal errors) 
    -h show this message

    Prints the rms distance between two columns of file.
    
    '''

    raise NotImplementedError


def nr_lazy():

    '''
    Simple nonlinear noise reduction

    This program performs simple nonlinear noise reduction. Each
    embedded point is replaced by the average vector calculated in its
    neighbourhood with a given size. This is different from what is
    described in Schreiber. There and in the program lazy only the
    central component of each vector is corrected. It is advisable to
    give both a try. We found a tendency that lazy performs better on
    map like data while nrlazy is superiour on flow like data.  

    Option    Description                    Default
    -----------------------------------------------------------------------
    -l#       number of points to use        whole file
    -x#       number of lines to be ignored  0
    -c#       column to be read              1
    -m#       embedding dimension            5
    -d#       delay for the embedding        1
    -i#       number of iterations           1
    -r#       neighborhood size              (interval of the data) / 1000

    -v#       neighborhood size in units     not set
              of the std. dev. of the data
              overwrites the -r option
    -----------------------------------------------------------------------


    Output

    Each of the files produced consists of one column being the
    filtered time series. If the verbosity level is set accordingly,
    the second column contains the number of neighbors found for this
    point. If this number is 1, no correction is done at all for this
    point.

    '''
    
    raise NotImplementedError


def lazy():

    '''
    Simple nonlinear noise reduction

    -m embedding dimension 
    -r absolut radius of neighbourhoods 
    -v same as fraction of standard deviation 
    -i number of iterations (1) 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -o output file name, just -o means file_lc, file_lcc (etc.) 
    -V verbosity level (0 = only fatal errors) 
    -h show this message

    Performs nonlinear noise reduction with locally constant
    approximations. Either -r or -v must be present. Output file (the
    cleaned sequence) is file_lc[ccc] (one letter c per iteration).


    This routine is based on

      T. Schreiber, 
      Extremely simple nonlinear noise reduction method, 
      Phys. Rev. E 47, 2401 (1993).


    Note: With already fairly clean data, you can expect superior
    results using project or ghkss.
    
    See also nrlazy which corrects more than just the central
    component. You may want to try both.

    '''

    raise NotImplementedError


def ghkss():

    '''
    Nonlinear noise reduction

    This program performs a noise reduction [0] as proposed in
    Grassberger et al. [1]. In principal, it performs a orthogonal
    projection onto a q-dimensional manifold using a special (tricky)
    metric. In case the -2 parameter is set, an euclidean metric is
    used. This is done in Cawley et al. [2] as well as in Sauer [3]
    and is sometimes useful for flow systems.

    [0] http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/chaospaper/node24.html
    [1] http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/chaospaper/citation.html#on
    [2] http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/chaospaper/citation.html#cawley
    [3] http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/chaospaper/citation.html#sauer


    Usage

    Option    Description                       Default
    ----------------------------------------------------------------------
    -l#       number of points to use           whole file
    -x#       number of lines to be ignored     0
    -c#       column to be read                 1
    -m#       embedding dimension               5
    -d#       delay for the embedding           1

    -q#       dimension of the manifold         3
              to project to

    -k#       minimal number of neighbours      30

    -r#       minimal size of the               (interval of data) / 1000
              neighbourhood

    -i#       number of iterations              1

    -2        use euclidean metric instead of   tricky metric
              the tricky one
    ----------------------------------------------------------------------


    Output

    Each file produced contains the filtered time series as one
    column. The standard error device shows some statistics, namely
    for each iteration (i) the number of vectors corrected up to the
    actual value of the neighborhood size, (ii) the average shift and
    (iii) the average correction. (iv) The next line shows for how
    many points the correction was unreasonably large and the last
    line shows (v) the file, to which the corrected data was written.

    '''

    raise NotImplementedError


def project():

    '''
    Nonlinear noise reduction


    -m embedding dimension 
    -q dimension of manifold 
    -r radius of neighbourhoods 
    -k minimal number of neighbours 
    -i number of iterations (1) 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -o output file name, just -o means file_c, file_cc (etc.) 
    -V verbosity level (0 = only fatal errors) 
    -h show this message


    Performs nonlinear projective noise reduction. Output file (the
    cleaned sequence) is file_c[ccc] (one letter c per iteration). As
    a second column, the difference between original and cleaned
    sequence is printed.

    Note: This routine is largely redundant with ghkss.

    This routine is based on

        P. Grassberger, R. Hegger, H. Kantz, C. Schaffrath, and
        T. Schreiber, On noise reduction methods for chaotic data, Chaos
        3, 127 (1993); Reprinted in: E. Ott, T. Sauer, and J. A. Yorke,
        eds., Coping With Chaos, Wiley, New York (1994)

    '''

    raise NotImplementedError

