# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 20:33:43 2018

@author: Talha.Iftikhar
"""
import numpy as np

a=np.array([2,3,4])

a=np.arange(1,12,2)
a

a=np.linspace(1,12,6)
a=a.reshape(3,2)
a
a.size

a.shape

a.dtype

a.itemsize

b=np.array([(1.2,2,3),(2,3.4,5)])
b.shape

a<4
b<6

a*3

a*=3

a=np.zeros((3,4))
a
a.dtype


a=np.ones((4,3))
a=np.array([2.3,3,4],dtype=np.int16)

a.dtype

a*=4.2

a.size

a=np.random.random((2,3))
a.sum()
a.avg()
a.std()


a=np.random.randint(1,10,6)

a=a.reshape(2,3)
a
a.sum(axis=0)

np.random.shuffle(a)
a
np.random.choice(a)
a=np.arange(1,10,2)