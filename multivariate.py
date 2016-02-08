#!/usr/bin/env python
#-*- coding:utf-8 -*-




'''
Multivariate time series

TISEAN's multivariate section is still growing - like the research body 
in this area. As a convention, program names for ``cross-'' quantities 
computed between two signals start with x. Those programs that can handle 
scalar as well as multivariate data don't follow any name convention.

Currently, three (cross-) similarity measures are available, a linear and 
two nonlinear ones. Further, there is a zeroth order predictor using 
multivariate embeddings. A few general routines that can handle 
multivariate data are also mentioned below. Note in particular the 
multivariate surrogate data generator, the Grassberger-Procaccia 
correlation sum, and the fixed mass D1 estimator.

The general convention for column selection is as follows. Columns can 
be given as a comma seperated list with the option -c#[,#] . Wherever 
the number of columns is selectable, this can be done with the option 
-m# or the first number in its argument. The precedence of these settings 
are as follows:

-m overrides -c
-c overrides the default only if more columns are specified.

Exceptions to this general convention are possible and mentioned in the 
specific program descriptions.


'''

def ar_model():

    '''
    Multivariate linear model

    This program fits a simple autoregressive (AR) model to the
    possibly multivariate data. The model is given by the equation :

    http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/docs_c/ar-model-eq1.gif

    The matrices Ai are determined by the program.

    The output file contains the coefficients of the model and the
    residuals. Note that now the mean is subtracted first, conforming
    with common practice. If you want to run the resulting model to
    generate a time series, you can either use the -s flag of the
    program or pipe the output to ar-run. Note that no attempt has
    been made to generate a stable model.


    Usage

    Option    Description                     Default
    ---------------------------------------------------------
    -l#       number of data to use           whole file
    -x#       number of lines to be ignored   0
    -m#       dimension of the vectors        1
    -c#       column to be read               1, ..., dimension of the vectors
    -p#       order of the model              5
    -s#       iterate s steps of the model    no iteration
    ---------------------------------------------------------

    Output

    The first line just contains the average forecast errors of the
    model for each component of the vector x, the next p*(dimension of
    the vectors) lines contain the AR coefficients for each of the
    components. The rest of the file are the individual errors
    (residuals) or a iterated time series depending on the flag -s.

    '''

    raise NotImplementedError


# def makenoise():
from nonlinear_noise_reduction import makenoise


def xcor():
    
    '''
    Linear cross-correlations

    This program computes the cross correlations between two time
    series, given as two columns of ONE datafile.


    Usage

    Option    Description                      Default
    -----------------------------------------------------
    -l#       number of data to use            whole file
    -x#       number of lines to be ignored    0

    -c#       columns to be read (numbers      1,2
              have to be separated by commas)

    -D#       number of correlations           100
    -----------------------------------------------------


    Output

    The first four lines contain the average and the standard
    deviation of the two data sets. The last lines are the
    crosscorrelations: <xt*yt+d> devided by the standard deviations of
    both data sets. d ranges from -D to D.

    '''

    raise NotImplementedError


# def extrema():
from phase_space import extrema


def sav_gol():
    
    '''
    Savitzky-Golay filter

    This program performes a Savitzky-Golay filter to either clean the
    data from high frequency noise or to get a better estimate of the
    Dth derivative. It it possible to run it on multivariate data.


    Usage

    Option    Description                                        Default
    --------------------------------------------------------------------------
    -l#       number of data to usewhole file
    -x#       number of lines to be ignored                      0
    -c#       columns to be read                                 1
    -m#       no. of components to be read (dimension)           1

    -n#,#     length of the averaging window back in time,
              length of the averaging window forward in time     2,2

    -p#       order of the fitted polynomial2
    -D#       order of the derivative to be estimated0           (just filter)
    --------------------------------------------------------------------------


    Output

    The output file contains l lines, each of which has m columns. It
    is the filtered data. The first length of the averaging window
    back in time and the last length of the averaging window forward
    in time lines are special. They contain the raw data in case that
    D was set to 0 and zeroes in case D was larger than zero.

    '''

   raise NotImplementedError


# def recurr():
from stationarity import recurr


def xzero():
    '''
    Nonlinear cross-prediction

    This program takes two data sets (i.e. two columns in a single
    datafile) and fits a zeroth order model of data set 1 to predict
    data set 2 (cross prediction). It then computes the error of the
    model. This is done by searching for all neighbors in set 1 of the
    points of set 2 which should be forecasted and taking as their
    images the average of the images of the neighbors. The given
    forecast error is normalized to the variance of data set 2.


    Usage

    Option    Description                               Default
    -------------------------------------------------------------------
    -l#       number of points to use                   whole file
    -x#       number of lines to be ignored             0

    -c#       columns to be read (separated by          1,2
              a comma)

    -m#       embedding dimension                       3
    -d#       delay for the embedding                   1

    -n#       for how many points should the            all
              error be calculated

    -k#       minimal numbers of neighbors              30
              for the fit

    -r#       neighborhood size to start with           (data interval) / 1000

    -f#       factor to increase the neighborhood       1.2
              size if not enough neighbors were
              found

    -s#       steps to be forecasted                    1
              (x2n+steps= av(x1i+steps)
    -------------------------------------------------------------------

    '''

    raise NotImplementedError


def xc2():

    '''
    Cross-correlation integral


    Cross-correlation integral of two data sets (i.e. two columns in a
    ssingle file) in 2 to M embedding dimensions. Together with the
    (auto-)correlation intergrals of each of the two sets, this gives
    an impression of their similarity or dissimilarity. If the minimal
    number of centers n is small, the program is fast but the results
    suffer from large statistical fluctuations on the large length
    scales. Apart from statistical fluctuations, the results are
    invariant under the exchange of the sequence of the two files.

    As a special case, it is possible (but somewhat inefficient) to
    compute an ordinary correlation integral by taking the two sets to
    be the same. This can be done by selecting the same column twice,
    for example -c1,1 .


    Usage

    Option    Description                      Default
    ---------------------------------------------------------------------
    -M#       maximal embedding dimension      to be specified!
    -n#       minimal number of centers        to be specified!
    -t#       minimal time separation          to be specified!
    -d#       delay for the embedding          1
    -N#       maximal number of pairs          1000
    -##       number of length scale values    2 per octave

    -r#       minimal length scale             smallest distance of points
                                               in 2 dimensions

    -R#       maximal length scale             MAX(xmax - xmin, ymax - ymin)

    -l#       maximal number of values to      read whole file
              read from files

    -x#       number of lines to be skipped    0
              at the beginning

    -c#[,#]   columns to be read               1,2
    ----------------------------------------------------------------------


    Output

    Output: files outfile_mm for each embedding dimension between mm=2
    and mm=M, containing in the second column the fraction of pairs of
    points with distance smaller than the value reportet in the first
    column.

    '''

    raise NotImplementedError


def d2():
    '''
    Correlation integral, also for multivariate data

    This program estimates the correlation sum, the correlation
    dimension and the correlation entropy of a given, possibly
    multivariate, data set. It uses the box assisted search algorithm and
    is quite fast as long as one is not interested in large length
    scales. All length scales are computed simultaneously and the output
    is written every 2 min (real time, not cpu time). It is possible to
    set a maximum number of pairs. If this number is reached for a given
    length scale, the length scale will no longer be treated for the rest
    of the estimate.  Please consult the introduction paper for initial
    material on dimension estimation. If you are serious, you will need to
    study some of the literature cited there as well.

    In extension to what is described there, the simultaneous use of
    multivariate data and temporal embedding is possible using
    d2. Thus one has to give two numbers in order to specify the
    embedding dimension. The first is the number of multivariate
    components, the second the number of lags in the temporal
    embedding. This is realized by giving two numbers to the option
    -M, seperated by a comma. For a standard scalar time series, set
    the first number to 1. If your multivariate data spans the whole
    phase space and no further temporal embedding is desired, set the
    second value to 1. In any case, the total embedding dimension in
    the sense of the embedding theorems is the product of the two
    numbers.

    In order to be able to assess the convergence with increasing
    embedding dimension, results are reported for several such
    values. The inner loop steps through the number of components
    until the first argument of M is reached. The outer loop increases
    the number of time lags until the second argument of M is reached.


    Usage of the -c and -M flags

    Suppose, the option -M x,y has been specified. By default, the
    first x columns of a file are used. This behaviour can be modified
    by means of the -c flag. It takes a series of numbers separated by
    commas. The numbers represent the colomns. For instance -M 3,1 -c
    3,5,7 means, use three components with no additional temporal
    embedding, reading columns 3, 5 and 7. It is not necessary to give
    the full number of components to the -c flag. If numbers are
    missing, the string is filled up starting with the smallest
    number, larger than the largest given. For instance, -M 3,1 -c 3
    would result in reading columns 3, 4 and 5.


    Usage

    Option    Description                             Default
    --------------------------------------------------------------------
    -l#       number of data points to be used        whole file
    -x#       number of lines to be ignored           0
    -d#       delay for the delay vectors             1

    -M#       # of components,maximal embedding       1,10
              dimension

    -c#       columns to be read                      1,...,# of components
    -t#       theiler window                          0
    -R#       maximal length scale                    (max data interval)
    -r#       minimal length scale                    (max data interval)/1000
    -##       number of epsilon values                100

    -N#       maximal number of pairs to be used      1000
              (0 means all possible pairs)

    -E        use data that is normalized to [0,1]    not set (use natural units of the data)
              for all components
    --------------------------------------------------------------------


    Output

    The files with the extensions c2, d2 and h2 contain for each
    embedding dimension and each length scale two columns:

    first column: epsilon (in units chosen)
    second column: the estimated quantity (correlation sum, dimension, entropy)

    * extension .c2: This file contains the correlation sums for all
      treated length scales and embedding dimensions.

    * extension .d2: This file contains the local slopes of the
      logarithm of the correlation sum, the correlation dimension.


    * extension .h2: This file contains the correlation entropies.

    * extension .stat: This file shows the current status of the estimate.


    The output is written every two minutes (real time, not cpu
    time). So, you can see preliminary results even if the program is
    still running. Post-processing can be done in the following
    ways. Either of the output sequences can be smoothed by
    av-d2. Takens' estimator can be obtained from the correlation sum
    (extension .c2) using c2t and then plotted versus upper cut-off
    length. The Gaussian kernel correlation integral can be obtained
    from the standard correlation sum (extension .c2) using c2g.

    ...

    http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/index.html

    '''

    raise NotImplementedError


def c1():
    
    '''
    Fixed mass estimation of C1 (information dimension)

    
    -d delay 
    -m minimal embedding dimension 
    -M maximal embedding dimension (at least 2) 
    -t minimal time separation 
    -n minimal number of center points 
    -# resolution, values per octave (2) 
    -K maximal number of neighbours (100) 
    -l number of values to be read (all) 
    -x number of values to be skipped (0) 
    -c column(s) to be read (1 or file,#) 
    -o output file name, just -o means file_c1 
    -V verbosity level (0 = only fatal errors) 
    -h show this message


    Computes curves for the fixed mass computation of the information
    dimension. The output is written to a file named file_c1,
    containing as two columns the necessary radius and the
    `mass'. Although the `mass' is the independent quantity here, this
    is to conform with the output of c2naive and d2.  A logarithmic
    range of masses between 1/N and 1 is realised by varying the
    neighbour order k as well as the subsequence length n. For a given
    mass k/n, n is chosen as small is possible as long as k is not
    smaller than the value specified by -K .

    The number of reference points has to be selected by specifying -n
    . That number of points are selected at random from all time
    indices.

    It is possible to use multivariate data, also with mixed
    embeddings. Contrary to the convention, the embedding dimension
    here specifies the total number of phase space coordinates. The
    number of components of the time series to be considered can only
    be given by explicit enumeration with the option -c .

    Note: You will probably use the auxiliary programs c2d or c2t to
    process the output further. The formula used for the Gaussian
    kernel correlation sum does not apply to the information
    dimension. See also the example below.

    '''

    raise NotImplementedError


def lyap_spec():

    '''
    Lyapunov spectra

    This program estimates the whole spectrum of Lyapunov exponents
    for a given, possibly multivariate, time series. Whole spectrum
    means: If d components are given and the embedding dimension is m
    than m*d exponents will be determined. The method is based on the
    work of Sano and Sawada [1].

    http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/chaospaper/citation.html#sasa


    Usage

    Option    Description                           Default
    --------------------------------------------------------------------
    -l#       number of points to use               whole file
    -x#       number of lines to be ignored         0
    -c#       column to be read                     1
    -m#       no. of components, embedding          1,2
              dimension

    -d#       delay for the delay vectors           1

    -r#       initial size of the neighborhoods     (data interval)/1000
              is dynamically changed during the
              run

    -f#       factor to increase the size of        1.2
              the neighborhood if not enough
              neighbors were found

    -k#       number of neighbors to use (this      30
              version uses exactly the number
              of neighbors specified. If found
              more, only the # nearest will be
              used)

    -n#       number of iterations                  number of points

    -I        invert the order of the time series.  no inversion
              Is supposed to help finding spurious
              exponents.
    --------------------------------------------------------------------


    Output

    The output consists of d*m+1 columns. The first one shows the
    actual iteration, the next d*m ones the estimates of the Lyapunov
    exponents in decreasing order. The last lines show the average
    forecast error(s) of the local linear model, the average
    neighborhood size used for fitting the model and the last one the
    estimated Kaplan-Yorke dimension.

    Output is written every 10 seconds (real time), approximately.

    '''

    raise NotImplementedError


def box_count():

    '''
    Renyi entropies

    This program estimates the Renyi entopy of Qth order using a
    partition of the phase space instead of using the
    Grassberger-Procaccia scheme. The program also can handle
    multivariate data, so that the phase space is build of the
    components of the time series plus a temporal embedding, if
    desired. I should mention that the memory requirement does not
    increase exponentially like 1/epsilonM but only like M*(length of
    series). So it can also be used for small epsilon and large M.

    No finite sample corrections are implemented so far.


    Usage

    Option    Description                             Default
    -----------------------------------------------------------------------
    -l#       number of data points to be used        whole file
    -x#       number of lines to be ignored           0
    -c#       columns to be read                      1, ..., # of components
    -d#       delay for the delay vectors             1

    -M#       # of components, maximal embedding      1,10
              dimension

    -Q#       Order of the entropy                    2.0
    -R#       maximal length scale                    whole data range
    -r#       minimal length scale                    (data range) / 1000
    -##       number of epsilon values                20
    -----------------------------------------------------------------------


    Output

    The output file contains three columns for each dimension and for
    each epsilon value:

      1. epsilon
      2. Qth order entropy (HQ(dimension,epsilon))
      3. Qth order differential entropy (
         HQ(dimension,epsilon)-HQ(dimension-1,epsilon))

    The slope of the second line gives an estimate of DQ(m,epsilon).

    '''

    raise NotImplementedError


# def zeroth():
from nonlinear_prediction import zeroth


def nstep():

    '''
    Locally linear prediction on multivariate time series

    This program makes depending on whether -0 is set either a local
    linear ansatz or a zeroth order ansatz for a possibly multivariate
    time series and iterates a artificial trajectory. The initial
    values for the trajectory are the last points of the original time
    series. Thus it actually forecasts the time series.


    Usage

    Option    Description                         Default
    ----------------------------------------------------------------------
    -l#       number of points to use             whole file
    -x#       number of lines to be ignored       0

    -m#       # of components,embedding           1,2
              dimension

    -c#       columns to be read                  1,...,# of components
    -d#       delay for the embedding             1
    -L#       length of prediction                1000

    -k#       minimal numbers of neighbors        30
              for the fit

    -r#       neighborhood size to start with     (interval of data)/1000

    -f#       factor to increase the              1.2
              neighborhood size if not enough
              neighbors were found

    -0        perform a zeroth order fit           not set (local linear)
              instead of a local linear one
    ----------------------------------------------------------------------
    '''

    raise NotImplementedError


# def compare():
from nonlinear_noise_reduction import compare


# def choose():
from utils import choose


# def surrogates():
from surrogate import surrogates


# def end_to_end():
from surrogate import end_to_end


