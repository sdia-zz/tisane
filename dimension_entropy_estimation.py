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



def d2():
    "Correlation integral"
    raise NotImplementError


def av_d2():
    "Correlation integral"
    raise NotImplementError


def c2_naive():
    "Correlation integral"
    raise NotImplementError


def c2d():
    "Correlation integral"
    raise NotImplementError


def c2t():
    "Takens estimator"
    raise NotImplementedError


def c1():
    "Fixed mass estimation of D1"
    raise NotImplementedError


def box_count():
    "Renyi Entropies of Qth order"
    raise NotImplementedError
