# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 14:10:16 2017

@author: Talha.Iftikhar
"""

import matplotlib
import pandas
import numpy
import scipy
#import statsmodel
import ggplot
from ggplot import *
import matplotlib as plt

meat.head()

ggplot(aes(x='date',y='beef'),data=meat)+geom_line(size=4)+geom_line(aes(y='veal',color='blue',size=4))+\
geom_vline(xintercept=[1944])
#%matplotlib inline
ggplot(mtcars, aes(x='wt', y='mpg', size='qsec')) + \
geom_line()
theme
red_patch = mpatches.Patch(color='red', label='The red data')
plt.legend("ff")

ggplot(mtcars, aes(x='wt', y='mpg')) +\
geom_point() +\
geom_vline(xintercept=[2, 4, 6])