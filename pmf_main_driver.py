#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:43:14 2019

@author: ashubunutu
"""

import pandas as pd 
import os
from get_count import get_count
import matplotlib.pyplot as plt
import numpy as np
from pmf import *
from probabily_mass_function import *
from vizualizations import *



frame1=48
dirName='img/'+str(frame1)+'Mbps'

try:
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")


for i in range (1,5):
    try:
        st=dirName+'/Node_'+str(i)
        os.mkdir(st)
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")

st='img/'+str(frame1)+'Mbps'+'/Node_1/Run_no'

interval=1

name= open("files/"+str(frame1)+"Mbps"+"_1.txt")
name_1=open("files/"+str(frame1)+"Mbps"+"_2.txt")
name_2=open("files/"+str(frame1)+"Mbps"+"_3.txt")
name_3=open("files/"+str(frame1)+"Mbps"+"_4.txt")



recv_1=file_read(name)
recv_2=file_read(name_1)
recv_3=file_read(name_2)
recv_4=file_read(name_3)



arr=[recv_1,recv_2,recv_3,recv_4]
st=''


for i,value in enumerate(arr):
    if i == 0:
        st=dirName+'/Node_1/Run_no'
    elif i ==1:
         st=dirName+'/Node_2/Run_no'
    elif i==2:
        st=dirName+'/Node_3/Run_no'
    elif i==3:
        st=dirName+'/Node_4/Run_no'
    
    plot_data_master(value,st,2) ## Needs to be called for each recv
    

path=dirName
plot_consolidated_run_master(arr,path) ## Needs to be call with an array containg all receivers