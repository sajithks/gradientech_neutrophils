# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:35:28 2015

@author: Sajith
"""



import scipy as sp
import time
import sys
import os
sys.path.append('/Users/sajithks/Documents/project_cell_tracking/phase images from elf')
sys.path.append('/Users/sajithks/Documents/project_cell_tracking/phase images from elf/ecoli_det_seg')
import createbacteria  as cb
import numpy as np
from matplotlib import pyplot as plt
import skimage.morphology as skmorph
import cv2
from scipy.ndimage import label
import fiteli
from multiprocessing import Pool
#from multiprocessing.pool import ThreadPool as Pool
#from numba import jit, double
#import cmath
from skimage import transform
import scipy.ndimage
import pymeanshift as pms
import morphsnakes
import criticalpoints as cr
import skimage


#%%
orimg = cv2.imread('/Users/sajithks/Documents/project_cell_tracking/data/gradientech/data_20140402/Gradientech/Testsekvens_1_Cancerceller/aligned/Aligned0000.png',cv2.CV_LOAD_IMAGE_UNCHANGED)


lbpimg = cb.lbpLike(orimg,5)



bila = skimage.filter.rank.bilateral
bilaimg = bila.pop_bilateral(orimg, np.ones((3,3)))
entroimg = skimage.filter.rank.entropy(orimg, np.ones((3,3)))
tophatimg = skimage.filter.rank.tophat(orimg, np.ones((3,3)))
bothatimg = skimage.filter.rank.bottomhat(orimg, np.ones((3,3)))


outimg = bilaimg+ entroimg + tophatimg + bothatimg


cb.myshow2(outimg)




