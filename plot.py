#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:07:16 2019

@author: ashubunutu
"""
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import plotly.plotly as py
import plotly
import sys
import plotly.graph_objs as go

import numpy as np


x0 = np.random.randn(6000)
plotly.tools.set_credentials_file(username='CryptoMatrix', api_key='XsGTHDyBIR0PiXmYqeI4')


def pie_plot(type,duration,totalDuration):
    data=0;
    mgmy=0;
    ctrl=0;
    for i,val in enumerate(type):
        if val== 0:
            data+=duration[i]
        elif val== 1:
            mgmy+=duration[i]
        elif val == 2:
            ctrl+=duration[i]
        else:
            continue

    total_duration=totalDuration-(data+mgmy+ctrl)
    sizes = [data,mgmy,ctrl,total_duration]
    labels = ['Data', 'Control', 'Managemt', 'Empty']
    trace = go.Pie(labels=labels, values=sizes)
    py.plot([trace], filename='basic_pie_chart')


    return 0


type=[0,0,1,2,0,1] ##Driver Code
duration=[-1,100,200,300,400,500]
totalDuration=1500
d=pie_plot(type,duration,totalDuration)




