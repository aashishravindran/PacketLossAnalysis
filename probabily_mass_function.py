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
    print(loss_burst)
    
    for key,value in loss_burst.items():
#        print(key,value)
        pmf[key]=(value/sum(loss_burst.values()))
        
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
    print(interval)
    for key,value in interval.items():
#        print(key,value)
        pmf[key]=(value/sum(interval.values()))
    
    return pmf

def get_allruns(recv,val):
    dict={}
    for i in range(0,len(recv)):
        dict[i]=get_frame_value(recv[i])[1]
    ret=consolidated_pmf(dict,val)
    return ret
    

def consolidated_pmf(recv,val):
    if val == 1:
        run={}
        arr=[]
        
#       print(recv.items())
        for key,value in recv.items():
            for i in value:
                arr.append(i)
#        print(arr)      
        burstlen=loss_burst_pmf(arr)
        return burstlen
    else:
        run={}
        arr=[]
        
#       print(recv.items())
        for key,value in recv.items():
            for i in value:
                arr.append(i)
#        print(arr)      
        interval=loss_burst_interval(arr)
        
        return interval
        
frame1=24
#interval=1

name= open("files/"+str(frame1)+"Mbps"+"_1.txt")
name_1=open("files/"+str(frame1)+"Mbps"+"_2.txt")
name_2=open("files/"+str(frame1)+"Mbps"+"_3.txt")
name_3=open("files/"+str(frame1)+"Mbps"+"_4.txt")


#
#retrun =get_frame_value(recv_1[18])[1]
#burst_len= loss_burst_pmf(retrun)
#lists=burst_len.items()
#x, y = zip(*lists)
#plt.bar(x,y,data=x)



recv_1=file_read(name)
recv_2=file_read(name_1)
recv_3=file_read(name_2)
recv_4=file_read(name_3)
##Tets

#retrun =get_frame_value(recv_4[0])[1]
#burst_len= loss_burst_interval(retrun)
#lists=burst_len.items()
#x, y = zip(*lists)
#plt.bar(x,y)
#





