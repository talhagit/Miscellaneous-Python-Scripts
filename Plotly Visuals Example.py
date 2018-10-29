# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:13:39 2018

@author: Talha.Iftikhar
"""

import plotly
import numpy as np
import plotly.graph_objs as go
import plotly.offline as ply
from IPython.display import Image
import IPython.display

# create sample data
n=201
x=np.linspace(0,2.0*np.pi,n)
y1=np.sin(x)
y2=np.cos(x)
y3=y1+y2

     ## plotly steps
# create traces-data collecitons
trace1=go.Scatter(
        x=x,
        y=y1,
        name="sine Curve",
        line=dict(
                color=("green"),
                width=4,
                dash='dash'
                ))

trace2=go.Scatter(
        x=x,
        y=y2,
        name="Cosine Curve",
        line=dict(
                color=("Red"),
                width=4,
                dash='dot'
                ))

trace3=go.Scatter(
        x=x,
        y=y3,
        name="Sin Cosine Curve",
        line=dict(
                color=("Red"),
                width=4,
                dash='dashdot'
                ))
# create info dictionary
layout=dict(
        title='Sample Curves',
        xaxis=dict(title='Angle in Radian'),
        yaxis=dict(title='Magnitude')
        )
data=[trace1,trace2,trace3]

# create a figure
fig=dict(data=data,layout=layout)

#plot data

ply.plot(fig,filename='scatter.html')

