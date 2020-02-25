#!/usr/bin/python

#import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def getYellowCyanGradientCmap():
	cdict = {'red': ((0.0, 0.0, 0.0),
			   (0.5, 0.0, 0.0),
			   (1.0, 1.0, 1.0)),
		 'green': ((0.0, 1.0, 1.0),
			   (0.5, 0.0, 0.0),
			   (1.0, 1.0, 1.0)),
		 'blue':  ((0.0, 0.1, 1.0),
			   (0.5, 0.0, 0.0),
			   (1.0, 0.0, 0.0))
		 }
	YellowCyanGradient = LinearSegmentedColormap('mycmap', cdict)
	YellowCyanGradient.set_bad('gray',1.)
	return YellowCyanGradient

def getBrickGradientCmap():
    cdict = {'red':   ((0.0, 1.0, 1.0),
                       (0.7, 0.70, 0.70),
                       (1.0, 0.70, 0.70)),
             'green': ((0.0, 1.0, 1.0),
                       (0.7, 0.15, 0.15),
                       (1.0, 0.15, 0.15)),
             'blue':  ((0.0, 1.0, 1.0),
                       (0.7, 0.07, 0.07),
                       (1.0, 0.07, 0.07))
             }
    BrickGradientCmap = LinearSegmentedColormap('mycmap', cdict)
    BrickGradientCmap.set_bad('gray',1.)
    return BrickGradientCmap

def getTealGradientCmap():
    cdict = {'red':   ((0.0, 1.0, 1.0),
                       (0.167, 1.0, 1.0),
                       (1.0, 0.0, 0.0)),
             'green': ((0.0, 1.0, 1.0),
                       (0.167, 1.0, 1.0),
                       (1.0, 0.4, 0.4)),
             'blue':  ((0.0, 1.0, 1.0),
                       (0.167, 1.0, 1.0),
                       (1.0, 0.4, 0.4))
             }
    GradientCmap = LinearSegmentedColormap('mycmap', cdict)
    GradientCmap.set_bad('lightgray',1.)
    return GradientCmap


def assigncolor(l):
	if( 'BREAST_BASAL' in l ):
		return 1
	elif( l=='BREAST_LUMINAL' ):
		return 5 
	elif( l=='BREAST_HER2'):
		return 8 
	elif( (l=='BREAST_UNCLASSIFIED') | (l=='BREAST') |  ( l=='BREAST_IMMORTALIZED') ):
		return 2
	elif( "OVARIAN_E/CC" in l ):
		return 12
	elif( 'OVARIAN_HGS' in l):
		return 16
	elif( 'OVARIAN' in l):
		return 14
	elif( l=='PANCREATIC'):
		return 20
	elif( l=='COLON'):
		return 24


def assigncolor_achilles(l):
	if( l=='BONE'):
		return 1
	elif( l=='BREAST' ):
		return 2 
	elif( l=='COLON'):
		return 3 
	elif( l=='HAEM' ):
		return 4
	elif( l=='KIDNEY'):
		return 5
	elif( l=='LUNG'):
		return 6
	elif( l=='OVARY'):
		return 7
	elif( l=='PANCREAS'):
		return 8
	elif( l=='PROSTATE'):
		return 9
	elif( l=='SKIN'):
		return 10



def clean_axis(ax):
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)


def qnorm(anarray):

        """
        anarray with samples in the columns and probes across the rows
        """
        anarray.dtype = np.float64
        A=anarray

        AA = np.float64( np.zeros_like(A) )

        I = np.argsort(A,axis=0)

        AA[I,np.arange(A.shape[1])] = np.float64( np.mean(A[I,np.arange(A.shape[1])],axis=1)[:,np.newaxis] )

        return AA

