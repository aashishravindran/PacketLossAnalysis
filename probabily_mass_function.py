#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:06:24 2019

@author: ashubunutu
"""
import pandas as pd 
from pmf import file_read,get_frame_value
from collections import Counter
import matplotlib.pyplot as plt


def loss_burst_pmf(run):
    count=0
    arr=[]
    pmf={}
    for i in range(0,len(run)):
        
        if run[i] == 'Y' and count >1:
            arr.append(count)
            count=0
        if run[i] == 'N':
            count+=1
    loss_burst=Counter(arr)

    
    for key,value in loss_burst.items():
#        print(key,value)
        pmf[key]=(value/len(arr))
        
#    loss_burst=pd.DataFrame(loss_burst[0].value_counts())
#    loss_burst.columns=["Counts"]
#    loss_burst['pmf']=loss_burst['Counts']/length
    return pmf

def loss_burst_interval(run):
    count =0;
    arr=[]
    pmf={}
    for i in range(0,len(run)):
        if (run[i] == 'N' and count >1):
            arr.append(count)
            count=0
        if run[i] == 'Y':
            count+=1
    interval=Counter(arr)
#    print(interval)
    for key,value in interval.items():

        pmf[key]=(value/len(arr))
    
    return pmf

def get_allruns(recv):
    dict={}
    for i in range(0,len(recv)):
        dict[i]=get_frame_value(recv[i])[1]
    
    return dict
    

def consolidated_pmf(recv,val):
    
    arr=[]
    for key,value in recv.items():
            for i in value:
                arr.append(i) 
    if val == 1:
        burstlen=loss_burst_pmf(arr)
        return burstlen
    else:
       interval=loss_burst_interval(arr)
       return interval


def most_frequent_losses_pmf(recv,mf,total_runs):
    ##Please Run 'Get All Runs Befeore Running This'
    count=0
    dict={}
    for key, value in recv.items():
        for idx,val in enumerate(value):
            if val == 'N':
                if idx in dict:
                    count=dict[idx]+1;
                    dict[idx]=count
                else:
                    dict[idx]=1



    for key,value in dict.items():
        dict[key]=value/total_runs
    k=Counter(dict).most_common(mf)  
    return k

    
