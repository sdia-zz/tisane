#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''
Nonlinear prediction


A number of phase space based prediction techniques are 
implemented in TISEAN. They differ in the way in which 
the dynamics is approximated. The very similar programs 
zeroth and predict use locally constant fits. This is the 
most robust approach for short, noisy signals, easy 
handling and quick answers. Further, local linear models, 
radial basis functions, and polynomial fits are provided.

For a discussion of these methods and examples see the 
corresponding section of the introduction paper.

Ref: http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/chaospaper/node16.html

'''


def zeroth():

    '''
    Simple nonlinear prediction

    This program makes a zeroth order ansatz and estimates the one
    step prediction errors of the model on a multivariate time
    series. This is done by searching for all neighbors of the point
    to be forecasted and taking as its image the average of the images
    of the neighbors. The given forecast errors are normalized to the
    standard deviations of each component. In addition to using a
    multicomponent time series a temporal embedding is possible. Thus
    one has to give two dimensions. The first is the number of
    components, the second the temporal embedding. This is realized by
    giving two numbers to the option m seperated by a comma.


    Usage of the -c and -m flags

    By default the first m columns of a file are used. This behaviour
    can by modified by means of the -c flag. It takes a series of
    numbers separated by commas. The numbers represent the
    colomns. For instance -m 3,1 -c 3,5,7 means, use three components
    with no additional temporal embedding, reading columns 3, 5 and
    7. It is not necessary to give the full number of components to
    the -c flag. If numbers are missing, the string is filled up
    starting with the smallest number, larger than the largest
    given. For instance, -m 3,1 -c 3 would result in reading columns
    3, 4 and 5.


    Usage:

    Option    Description                            Default
    ----------------------------------------------------------------------------
    -l#       number of points to use                whole file
    -x#       number of lines to be ignored          0

    -m#       number of components of the time       1, 2
              series,embedding dimension

    -c#       columns to be read                     1, 2, ..., 'number of components'

    -d#       delay for the embedding                1

    -n#       for how many points should the         all
              error be calculated

    -S#       temporal distance between the          1
              reference points

    -k#       minimal numbers of neighbors           30
              for the fit

    -r#       neighborhood size to start with        (data interval) / 1000

    -f#       factor to increase the neighborhood    1.2
              size if not enough neighbors were
              found

    -s#       steps to be forecasted                 1
              xn+steps=av(xi+steps)

    -C#       width of causality window              steps to be forecasted
    ----------------------------------------------------------------------------


    Output:

    The output consists of s lines, each of which containing the steps
    forecasted (first column) and the relative forecast errors (next
    columns) for each component of the vector seperately. Relative
    means that the forecast error is devided by the standard deviation
    of the vector component.

    If the Verbosity level is larger than 1, the output also contains
    the individual forecast error for each component of each reference
    point.

    '''

    raise NotImplementedError


# def predict():
from surrogate import predict


def ll_ar():

    '''
    Local vs. global linear prediction

    This program makes a local linear ansatz and estimates the one
    step prediction error of the model. The difference to onestep is
    that it does it as a function of the neighborhood size (see
    Casdagli [1]).

    ll-ar means something like local-linear -› AR-model

    [1] http://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/chaospaper/citation.html#casdagli91


    Option    Description                     Default
    ----------------------------------------------------------------------
    -l#       number of points to use         whole file
    -x#       number of lines to be ignored   0
    -c#       column to be read               1
    -m#       embedding dimension             2
    -d#       delay for the embedding         1

    -i#       for how many points should the  all
              error be calculated

    -r#       neighborhood size to start      (data interval) / 1000
              with

    -R#       neighborhood size to end with   data interval

    -f#       factor to increase the          1.2
              neighborhood size if not enough
              neighbors were found

    -s#       steps to be forecasted          1
              (x_{n+steps} = f(\vec{x}_n))

    -C#       width of causality window       steps to be forecasted
    ----------------------------------------------------------------------


    Output

    The output consists of 5 columns for each neighborhood size:
      * neighborhood size (units of the data)
      * relative forecast error ((forecast error)/(variance of the data))
      * fraction of points for which neighbors were found for this neighborhood size
      * average number of neighbors found per point
      * variance of the fraction of points for which neighbors were found

    '''

    raise NotImplementedError


def rbf():

    '''
    Radial basis function fit

    This program models the data using a radial basis function (rbf)
    ansatz. The basis functions used are gaussians, with center points
    chosen to be data from the time series. If the -X option is not
    given, a kind of Coulomb force is applied to them to let them
    drift a bit in order to distribute them more uniformly. The
    variance of the gaussians is set to the average distance between
    the centers.

    This program either tests the ansatz by calculating the average
    forecast error of the model, or makes a i-step prediction using
    the -L flag, additionally. The ansatz made is:

    xn+1 = a0 + SUM aifi(xn),

    where xn is the nth delay vector and fi is a gaussian centered at
    the ith center point.


    Usage:

    Option    Description                              Default
    --------------------------------------------------------------------
    -l#       number of data to use                    whole file
    -x#       number of lines to be ignored            0
    -c#       column to be read                        1
    -m#       embedding dimension                      2
    -d#       delay                                    1
    -p#       number of centers                        10
    -X        deactivate drift (Coulomb force)         activated

    -s#       steps to forecast (for the               1
              forecast error)

    -n#       number of points for the fit;            number of data
              The other points are used to estimate
              the out of sample error

    -L#       determines the length of the             none
              predicted series
    --------------------------------------------------------------------


    Output:

    The output file contains: The coordinates of the center points,
    the variance used for the gaussians, the coefficients (weights) of
    the basis functions used for the model, the forecast errors and if
    the -L flag was set, the predicted points.

    '''

    raise NotImplementedError


def polynom():

    '''
    Polynomial model

    This programs models the data making a polynomial ansatz.


    Usage

    Option    Description                      Default
    ------------------------------------------------------------
    -l#       number of data to use            whole file
    -x#       number of lines to be ignored    0
    -c#       column to be read                1
    -m#       embedding dimension              2
    -d#       delay                            1
    -p#       order of the polynomial          2

    -n#       number of points for the fit;    number of data
              The other points are used to
              estimate the out of sample error

    -L        #determines the length of the    none
              predicted series
    ------------------------------------------------------------


    Output

    The output file contains: The coefficients of the model, the
    forecast errors and if the -L flag was set the predicted points.

    '''

    raise NotImplementedError


def polynomp():

    '''
    Polynomial model

    This programs models the data making a polynomial ansatz. It
    differs from the polynom program in the following way. It reads
    the terms of the polynomial from a parameter file. You can either
    create such a file by hand or by the program polypar (See there
    for a description of how the parameter file has to look like). The
    advantage is that it is possible to select the terms in the
    polynomial either by hand or by a backward elimination.


    Usage

    Option    Description                      Default
    ----------------------------------------------------------
    -l#       number of data to use            whole file
    -x#       number of lines to be ignored    0
    -c#       column to be read                1
    -m#       embedding dimension              2
    -d#       delay                            1

    -n#       length for the insample error    all
              estimation

    -L#       length of the trajectory         1000
              to cast

    -p#       name of the parameter file       parameter.pol
    ----------------------------------------------------------


    Output

    The output file contains:
     * first row: forecasterrors (insample and out of sample)
     * next rows: The parameter of the model
     * last rows: the forecasted trajectory

    '''

    raise NotImplementedError


def polyback():

    '''
    Polynomial model

    This program performs a backward elimination for a given
    polynomial. This means it reads the terms of a polynomial from a
    parameter file (e.g. created by polypar) and removes term by term
    down to a given final number of remaining terms. The terms are
    removed in such a way that the onestep forecast error is increases
    minimally.


    Usage

    Option    Description                     Default
    -----------------------------------------------------------
    -l#       number of data to use           whole file
    -x#       number of lines to be ignored   0
    -c#       column to be read               1
    -m#       embedding dimension             2
    -d#       delay                           1

    -n#       length for the insample         all
              error estimation

    -s#       steps to be forecasted          1
    -##       reduce down to # terms          1
    -p#       name of the input parameter     parameter.pol
              file
    -----------------------------------------------------------


    Output

    It creates a lot of new parameter files. For each term removed
    there is one file which is called parameter_input_file_name.n,
    where n is the number of remaining terms in the polynomial.

    stdout or datafile.pbe contains the following information:
      * first column: number of remaining terms in the polynomial
      * second column: insample error produced by this polynomial
      * third column: out of sample error produced by this polynomial
      * fourth column: the term removed last from the polynomial

    '''

    raise NotImplementedError


def polypar():

    '''
    Polynomial model

    This program creates a parameter file which can be used by the
    programs: polynomp and polyback.


    Usage

    Option    Description                    Default
    ---------------------------------------------------------
    -m#       dimension of the polynomial    2
    -p#       order of the polynomial        3
    -o#       output file name               parameter.pol
    ---------------------------------------------------------

    
    Output

    The output looks something like this:
    Each line looks like:

    i1 i2 ... id 

    These i's define the order of the delay vector entries in the term
    of the polynomial. This means the above line defines a term (let
    xn be the time series element at time n and let the delay be 1):
   
    xni1 xn-1i2... xn-m+1id

    '''

    raise NotImplementedError

