#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:38:11 2019

@author: ashubunutu
"""


import pandas as pd;
import numpy as np;


df=pd.read_csv('48Mbps_1.txt',header=None,names=['val'])
df2=pd.read_csv('48Mbps_2.txt',header=None,names=['val'])

for df in (df,df2):
    print(df['val'],df['val'])
