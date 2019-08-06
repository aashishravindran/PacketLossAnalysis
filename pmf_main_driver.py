#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:43:14 2019

@author: ashubunutu
"""


################### Driver Code for Pmf Starts Here=================================================


import pandas as pd 
import os
from global_functions import get_count
import matplotlib.pyplot as plt
import numpy as np
from probabily_mass_function import *
from vizualization_master import *
import statistics
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering



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
        print("Directory " , st ,  "Created")
    except FileExistsError:
        print("Directory " , st ,  " already exists")

st='img/'+str(frame1)+'Mbps'+'/Node_1/Run_no'

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
    
for i,value in enumerate(arr):
    if i == 0:
        st=dirName+'/Node_1/Run_no'
    elif i ==1:
         st=dirName+'/Node_2/Run_no'
    elif i==2:
        st=dirName+'/Node_3/Run_no'
    elif i==3:
        st=dirName+'/Node_4/Run_no'
    
    plot_data_master(value,st,1) 


path=dirName
plot_consolidated_run_master(arr,path) 
## Needs to be call with an array containg all receivers
#==================================Get All Runs and  plot  top n values================================
plot_most_commom_pmf(arr,path,frame1,10)

#====================Plot bad runs=============================================
plot_bad_runs(arr,path,frame1)


##================Statistical Highlights=======================================
plot_statistical_highlights(arr,path,frame1,1)
plot_statistical_highlights(arr,path,frame1,0)


#=======================================Loss Aggregation 2,3,4 recv plot=======
loss_aggregation_file_opne=open('files/'+str(frame1)+'MbpsData_Aggregation_Logs.txt')
l_a_values=loss_Aggr_file_read(loss_aggregation_file_opne,get_count(str(frame1))[1])


plot_recv_loss_combination(l_a_values,4,path,frame1,get_count(str(frame1))[1])

plot_recv_loss_combination(l_a_values,3,path,frame1,get_count(str(frame1))[1])

plot_recv_loss_combination(l_a_values,2,path,frame1,get_count(str(frame1))[1])
#==============================================================================


d={}

shor_duration=open('files/65_1.txt')

shor_duration1=open('files/65_2.txt')

shor_duration2=open('files/65_3.txt')

shor_duration3=open('files/65_4.txt')



recv_arr=[]
path='img/'
recv_arr.extend([bad_runs_across_runs(get_allruns(file_read(shor_duration))),
                 bad_runs_across_runs(get_allruns(file_read(shor_duration1))),
                 bad_runs_across_runs(get_allruns(file_read(shor_duration2))),
                 bad_runs_across_runs(get_allruns(file_read(shor_duration3)))])
plot_loss_percentage_cluster(recv_arr,3,path,65)