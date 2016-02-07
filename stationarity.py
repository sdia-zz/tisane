#!/usr/bin/env python
#-*- coding:utf-8 -*-



'''
Stationarity

This section contains two important tools for the visualization 
of time series properties and another stationarity test as proposed
by Schreiber. The recurrence plot and the space time separation 
plot are of great value for the detection of nonstationarity, 
selection of relevant time scales, selection of stationary episodes
 and so forth.

There is a short corresponding section in the introduction paper.

'''


def recurr():

    '''
    This program produces a recurrence plot of the, possibly
    multivariate, data set. That means, for each point in the data set
    it looks for all points, such that the distance between these two
    points is smaller than a given size in a given embedding space.
    Be careful! Choosing the value for the -r flag too large can lead
    to really big files.

    Option    Description                      Default
    ------------------------------------------------------------------
    -l#       number of data to use            whole file
    -x#       number of lines to be ignored    0
    -c#       columns to be read               1

    -m#       no. of components,               1,2
              embedding dimension

    -d#       delay                            1
    -r#       size of the neighbourhood        (data interval)/1000

    -%#       print only the percentage # of   100.0
              all points found; should help 
              to keep the file size reasonably
              small

    Output:

    Pairs of integers representing the indexes of the pairs of points
    having a distance smaller than r.

    '''

    raise NotImplementedError


def stp():

    '''
    Computes a space time separation plot as discussed by Provenzale
    et al.

    -d delay 
    -m embedding dimension 
    -# time resolution (1) 
    -t time steps (100, at most 500) 
    -% fraction at wich to create levels (0.05, at least 0.01) 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -o output file name, just -o means file_stp 

    This routine is based on

        A. Provenzale, L.A. Smith, R. Vio, and G. Murante, 
        Distinguishing between low-dimensional dynamics and randomness in 
        measured time series, 
        Physica D 58, 31 (1992).

    '''

    raise NotImplementedError


def nstat_z():

    '''
    Stationarity test

    This program seeks for nonstationarity in a time series by
    dividing it into a number of segments and calculating the
    cross-forecast errors between the different segments. The model
    used for the forecast is zeroth order model as proposed by
    Schreiber.

    Since the usage of some (two) of the flags of this program is a
    bit peculiar, here some more detailed information about them. Say,
    the number of segments chosen is N. Then for all possible
    combinations of the N segments the forecast errors are
    calculated. Means for N2 combinations. Since this can be a large
    number and one might be only interested in some of all possible
    combinations, the combinations can be reduced with the -1 and the
    -2 flags. The values these options can take are either single
    numbers, or ranges separated by commas. A range looks like n1-n2
    or like +n. To give some examples:

    a. nstat_z file -# 10 -1 1
       means: Divide the data into 10 segments and use the first segment 
       to forecast all segments.

    b. nstat_z file -# 10 -1 1,3,7-9
       means: Divide the data into 10 segments and use the first, the
       third and the seventh to the ninth segments to forecast all 
       segments

    c. nstat_z file -# 10 -1 +2
       means: Divide the data into 10 segments and forecast all segments I
       using segments I-2 to I+2.

    In other words the +n defines a time window around to segment to
    be forecasted and only segments lying in this window are used for
    the forecast. If the +n syntax is chosen, it can not be combined
    with other ranges or a number. The same works for the -2 flag,
    which specifies which segments are forecasted.

    Usage:

    Option    Description                      Default
    -------------------------------------------------------------------------
    -##       number of segments the data      no default. has to be given
              should be divided into

    -l#       number of points to use          whole file
    -x#       number of lines to be ignored    0
    -c#       column to be read                1
    -m#       embedding dimension              3
    -d#       delay for the embedding          1

    -1#       which segments should be used    1 - (# of segments) (all)
              to forecast the others

    -2#       which segments should be         1 - (# of segments) (all)
              forecasted by the others

    -n#       for how many reference points    all
              should the error be calculated

    -k#       minimal numbers of neighbors     30
              for the fit

    -r#       neighborhood size to start with  (data interval)/1000

    -f#       factor to increase the           1.2
              neighborhood size if not enough
              neighbors were found

    -s#       step to be forecasted            1
               xn+step=av(xi+step)

    -C#       width of causality window        steps to be forecasted


    Output:

    The output consists of a number of lines each of which consists of
    three columns:

    * first column: The index of the segment used for the forecast 
    * second column: The index of the segment that was forecasted
    * third column: The cross-forecast error normalized to the standard
      deviation of the segment that was forecasted.


    Before increasing the first index, an empty line is added to the
    file. Thus the file has a block structure which can be used to
    make 3d plots in gnuplot. Furthermore, the output format is
    suitable for clustering by cluster.

    '''

    raise NotImplementedError
