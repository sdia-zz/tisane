#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Embedding and Poincaré sections

Since the concept of phase space is at the heart of all the
nonlinear methods in this package, phase space reconstruction
plays an important role. Although delay and other embeddings 
are used inside most of the other programs, it is important to 
have these techniques also for data viewing, selection of 
parameters, etc. For delay embeddings, use delay. For principal 
components, svd and pc do almost the same thing.

Phase space reconstruction is discussed also in the the introduction paper.


Ref:
http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/chaospaper/node5.html

'''


def delay():

    '''
    Embed using delay coordinates

    -d delay (1) 
    -m embedding dimension (2) 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 

    Reads one column from a file and writes m delay coordinates as
    columns

    '''

    raise NotImplementedError


def svd():

    '''
    Embed using principal components

    This program performs a global SVD. It gives the singular values
    of the covariance matrix and if the -q flag is set either the data
    in the basis of the eigenvectors or, if a the parameter of the -q
    flag is smaller than the embedding dimension, the projected scalar
    time series. Some authors state such a projection to be a noise
    reduction scheme. But this is only true if both, the system and
    the measurement function, are linear.  

    Option    Description                    Default
    ----------------------------------------------------------------
    -l#       number of data to be used      whole file
    -x#       number of lines to be ignored  0
    -c#       column to be read              1
    -m#       dimension of the basis         2
    -d#       delay                          1

    -q#       project down to # dimensions   none (only write eigenvalues)
              and write the projected time
              series
              or if # equals the embedding
              dimension, write the vectors
              in the svd basis
    ----------------------------------------------------------------

    Output:

    The output consists of the singular values and if the -q option
    was used, the vectors in the SVD basis (if the dimension projected
    down to equalled the embedding dimension), or the projected
    (filtered) time series (if the dimension projected down to was
    smaller than the embedding dimension).

    '''

    raise NotImplementError


def pc():

    '''
    Embed using principal components

    -m initial embedding dimension 
    -d delay for initial embedding (1) 
    -q number of principal components (2) 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 

    Reads data from file and writes the projections onto the largest m
    principal components as columns. Output file file_pc. For each
    principal component, the fraction of the variance (not rms
    amplitude) covered and the accumulative fraction of the variance
    covered keeping all components so far are printed on stderr.

    '''

    raise NotImplementedError


def mutual():

    '''
    Mutual information of the data

    Estimates the time delayed mutual information of the data. It is
    the simplest possible realization. It uses a fixed mesh of boxes.

    No finite sample corrections are implemented so far.

    Option   Description                    Default
    ------------------------------------------------------------
    -l#      number of data to use          whole file
    -x#      number of lines to be ignored  0
    -c#      column to be read              1

    -b#      number of boxes for the        16
             partition

    -D#      maximal time delay             20
    ------------------------------------------------------------

    Output:

    The first line contains the number of occupied boxes, the second
    one the shannon entropy (normalized to the number of occupied
    boxes), the last D lines the mutual information (first column:
    delay, second column: mutual information).

    '''

    raise NotImplementedError


def poincare():

    '''
    Poincaré section

    This programs makes a Poincaré section for time continuous scalar
    data sets along one of the coordinates of the embedding vector.
    
    Option    Description                   Default
    -----------------------------------------------------------
    -l#       number of points to use       whole file
    -x#       number of lines to be ignored 0
    -c#       column to be read             1
    -m#       embedding dimension           2
    -d#       delay                         1
    -q#       component for the crossing    last

    -C#       direction of the crossing     0
              (0: from below, 1: from 
              above)

    -a#       position of the crossing      average of the data
    -----------------------------------------------------------

    Output:
    
    The output file contains m components for each cut. The first m-1
    components are the coordinates of the vector at the crossing, the
    last one is the time between the last two crossings 

    (see Hegger, Kantz 
    http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/chaospaper/citation.html#hk).

    '''

    raise NotImplementedError


def extrema():
    
    '''
    This program determines the maxima (minima) of one component of a
    possibly multivariate time series. This corresponds to a Poincaré
    section at the zeros of the derivative. To get a better estimate
    of the extremum, a quadratic interpolation is done.

    Note: Very sensitive to noise!

    Option    Description                    Default
    --------------------------------------------------------------
    -l#       number of points to use        whole file
    -x#       number of lines to be ignored  0
    -m#       # of components                1
    -c#       columns to be read             1,...,# of components
    -w#       which components to            1 
              maxi(mini)mize

    -z        determine minima instead       maxima
              of maxima

    -t#       minimal time required between  0.0
              two extrema
    --------------------------------------------------------------

    Outuput:

    The output consists of m+1 columns:
    * First m columns: The position of the extrema
    * Last column: The time between the last two extrema

    Note that the time given for the first extremum (the first row in
    the output file) is the absolute time from the start of the time
    series (t=0) to the first extremum.

    '''

    raise NotImplementedError


def upo():

    '''
    Unstable periodic orbits


    -m embedding dimension 
    -r absolute kernel bandwidth 
    -v same as fraction of standard deviation 
    -p period of orbit (1) 
    -w minimal separation of trial points (e) 
    -W minimal separation of distinct orbits (e) 
    -a maximal error of orbit to be plotted (all plotted) 
    -s initial separation for stability (e) 
    -n number of trials (all points) 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 


    Find unstable period -p orbits and their stabilitiy (the most
    unstable eigenvalue). The dynamics is approximated using a
    Gaussian kernel estimator of bandwidth -r | -v, where either -r or
    -v must be given. The minimum of

         p
        ---
        \   /                  \ 2
         |  | x    - f(x ,...) |
        /   \  n+1      n      /
        ---
        n=1

    is sought by a Levenberg-Marquardt scheme. The first -n embedded
    points are tried as initial conditions. False minima can be cut
    off by limiting -a, the error at the minimum. Very close trial
    points can be omitted by giving -w. Orbits which are less than -W
    apart are considered identical.

    The stability is computed by iterating forward a small (set by -s
    ) initial perturbation to the orbit.

    Orbits are written to file_upo_pp where pp is the desired
    period. If an orbit is found to have a sub-period, all results are
    given with respect to that. Orbits can be plotted in delay
    coordinates using upoembed.

    Note:
    As you noticed, the UPOs are defined here in a rather loose sense,
    similarly in spirit to the use by So et al. and other
    authors. Thus, the mere detection of such an orbit does not
    constitute evidence for low dimensional dynamics or anything the
    like.

    Note:
    The period is passed to the program in samples. This is different
    from what you may expect, since a "period 2" orbit of the Lorenz
    equations may turn out to have period 137 or whatever. In fact,
    the program has been written for map like, or Poincaré section
    data. It is also fair to say that it hasn't been tested
    extensively.

    Note: 
    While the existence and locations of the orbits seems to be quite
    reliable, the stabilities pose surprising problems. The chief
    reason is that they use information at a single point in phase
    space and no averaging over the whole attractor is
    involved. Values should be fine for comparisons, like in surrogate
    data testing. If absolute quantities are needed (like in cycle
    expansions), extra care has to be taken. The user might consider
    using an alternative approach, for example via the cycle Jacobians
    as obtained from a locally linear fit.

    '''

    raise NotImplementedError


def upo_embed():

    '''
    Embed periodic orbits using delay coordinates

    -d delay 
    -m embedding dimension (2) 
    -p period of orbit (1) 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column to be read (1 or file,#) 
    -o output file name, just -o means file_delay 
    -V verbosity level (0 = only fatal errors) 
    -h show this message

    Reads a file containing the locations of periodic orbits as it is
    produced by upo. These are embedded in m which are written as
    columns.

    '''

    raise NotImplementedError


def false_nearest():

    '''
    False nearest neighbours

    This program looks for the nearest neighbors of all data points in
    m dimensions and iterates these neighbors one step into the
    future. If the ratio of the distance of the iteration and that of
    the nearest neighbor exceeds a given threshold the point is marked
    as a wrong neighbor. The output is the fraction of false neighbors
    for the specified embedding dimensions (see Kennel et al.[1]).

    [1] http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/chaospaper/citation.html#kennel92


    Note: 
    We implemented a new second criterion. If the distance to the
    nearest neighbor becomes smaller than the standard deviation of
    the data devided by the threshold, the point is omitted. This
    turns out to be a stricter criterion, but can show the effect that
    for increasing embedding dimensions the number of points which
    enter the statistics is so small, that the whole statistics is
    meanlingless. Be aware of this!


    Usage:
    
    Option    Description                    Default
    ---------------------------------------------------------------
    -l#       number of data to use          whole file
    -x#       ignore the first # rows        0
    -c#       column to be read              1

    -m#       minimal dimension of the       1
              delay vectors

    -M#       maximal dimension of the       5
              delay vectors

    -d#       delay of the vectors           1
    -f#       ratio factor                   10.0
    -t#       theiler window                 0
    ---------------------------------------------------------------


    Output:

    output on stdout (or in the file):
      * first column:  the embedding dimension
      * second column: the fraction of false nearest neighbors
      * third column:  the average size of the neighborhood
      * fourth column: the average of the squared size of the neighborhood

    output on stderr:
    A statistics on how many points were found up to the given
    neighborhood size.

    '''

    raise NotImplementedError

