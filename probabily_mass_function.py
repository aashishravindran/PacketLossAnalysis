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
        count+=1
        if run[i] == 'Y' and count >1:
            arr.append(count)
            count=0
    loss_burst=Counter(arr)
    
    
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
        if run[i] == 'N' and count > 1:
            arr.append(count)
            count=0
        else:
            count+=1
    interval=Counter(arr)
    for key,value in interval.items():
#        print(key,value)
        pmf[key]=(value/sum(interval.values()))
    
    return pmf


def consolidated_run(recv,val):
    if val == 1:
        run={}
        for i in range(0,len(recv)):
            test=get_frame_value(recv[i])[2]         
            d=loss_burst_pmf(test)
#           t=probabilty(d,1)   
            run[i]=d
        
    
        burstlen=pd.DataFrame(run)
        burstlen['Burst_len']=burstlen.index
        burstlen['mean']=burstlen.loc[:, burstlen.columns != 'Burst_len'].mean(axis=1)
   
        return burstlen
    
    else:
        run={}
        for i in range(0,len(recv)):
            test=get_frame_value(recv[i])[2]         
            d=loss_burst_interval(test)
#           t=probabilty(d,1)   
            run[i]=d
        
    
        interval=pd.DataFrame(run)
        interval['Burst_len']=interval.index
        interval['mean']=interval.loc[:, interval.columns != 'Burst_len'].mean(axis=1)
   
        return interval
        
    


frame1=24
#interval=1

name= open("files/"+str(frame1)+"Mbps"+"_1.txt")
name_1=open("files/"+str(frame1)+"Mbps"+"_2.txt")
name_2=open("files/"+str(frame1)+"Mbps"+"_3.txt")
name_3=open("files/"+str(frame1)+"Mbps"+"_4.txt")



recv_1=file_read(name)
recv_2=file_read(name_1)
recv_3=file_read(name_2)
recv_4=file_read(name_3)



nrows = 4
fig, ax = plt.subplots(nrows, 2)

ret=consolidated_run(recv_1,1)
ax[0][0].bar(ret['Burst_len'],ret['mean'])
ax[0][0].set_title('Burst Len Vs Pmf across all runs Node 1',fontsize=10,pad=-10)

ret=consolidated_run(recv_1,2)
ax[0][1].bar(ret['Burst_len'],ret['mean'])
ax[0][1].set_title('Interval Vs Pmf across all runs Node 1',fontsize=10,pad=-10)

ret=consolidated_run(recv_2,1)
ax[1][0].bar(ret['Burst_len'],ret['mean'])
ax[1][0].set_title('Burst Len Vs Pmf across all runs Node 2',fontsize=10,pad=-10)
ret=consolidated_run(recv_2,2)
ax[1][1].bar(ret['Burst_len'],ret['mean'])
ax[1][1].set_title('Interval Vs Pmf across all runs Node 2',fontsize=10,pad=-10)



ret=consolidated_run(recv_3,1)
ax[2][0].bar(ret['Burst_len'],ret['mean'])
ax[2][0].set_title('Burst Len Vs Pmf across all runs Node 3',fontsize=10,pad=-10)
ret=consolidated_run(recv_3,2)
ax[2][1].bar(ret['Burst_len'],ret['mean'])
ax[2][1].set_title('Interval Vs Pmf across all runs Node 3',fontsize=10,pad=-10)


ret=consolidated_run(recv_4,1)
ax[3][0].bar(ret['Burst_len'],ret['mean'])
ax[3][0].set_title('Burst Len Vs Pmf across all runs Node 4',fontsize=10,pad=-10)



ret=consolidated_run(recv_4,2)
ax[3][1].bar(ret['Burst_len'],ret['mean'])
ax[3][1].set_title('Interval Vs Pmf across all runs Node 4',fontsize=10,pad=-10)




#retrun =get_frame_value(recv_1[0])[1]
#ret= loss_burst_pmf(retrun)
#lists=ret.items()
#x, y = zip(*lists)
#plt.bar(x,y)


#
#for i in range(0,len(recv_1)):
#    fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,sharey=False,squeeze=False)
#    retrun =get_frame_value(recv_1[i])[1]
#    burst_len= loss_burst_pmf(retrun)
#    lists=burst_len.items()
#    x, y = zip(*lists)
#    ax[0][0].bar(x,y)
#    ax[0][0].set_xlabel('Loss Burst Len')
#    ax[0][0].set_ylabel('Pmf')
##    retrun =get_frame_value(recv_1[i])[1]
#    interval= loss_burst_interval(retrun)
#    lists=interval.items()
#    x, y = zip(*lists)
#    ax[0][1].bar(x,y)
#    ax[0][1].set_xlabel('Interval')
#    ax[0][1].set_ylabel('Pmf')
#    fig.suptitle('Node1:Pmf for Loss Burst Len and Interval for Run_no'+str(i))
#    fig.savefig('img/Node_1/Pmf_Run_no'+str(i)+'.png')
#    fig.clf()
#    plt.close(fig)
#    
#
#
#for i in range(0,len(recv_2)):
#    fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,sharey=False,squeeze=False)
#    retrun =get_frame_value(recv_2[i])[1]
#    burst_len= loss_burst_pmf(retrun)
#    lists=burst_len.items()
#    x, y = zip(*lists)
#    ax[0][0].bar(x,y)
#    ax[0][0].set_xlabel('Loss Burst Len')
#    ax[0][0].set_ylabel('Pmf')
##    retrun =get_frame_value(recv_1[i])[1]
#    interval= loss_burst_interval(retrun)
#    lists=interval.items()
#    x, y = zip(*lists)
#    ax[0][1].bar(x,y)
#    ax[0][1].set_xlabel('Interval')
#    ax[0][1].set_ylabel('Pmf')
#    fig.suptitle('Node2:Pmf for Loss Burst Len and Interval for Run_no'+str(i))
#    fig.savefig('img/Node_2/Pmf_Run_no'+str(i)+'.png')
#    fig.clf()
#    plt.close(fig)
#    
#
#for i in range(0,len(recv_3)):
#    fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,sharey=False,squeeze=False)
#    retrun =get_frame_value(recv_3[i])[1]
#    burst_len= loss_burst_pmf(retrun)
#    lists=burst_len.items()
#    x, y = zip(*lists)
#    ax[0][0].bar(x,y)
#    ax[0][0].set_xlabel('Loss Burst Len')
#    ax[0][0].set_ylabel('Pmf')
##    retrun =get_frame_value(recv_1[i])[1]
#    interval= loss_burst_interval(retrun)
#    lists=interval.items()
#    x, y = zip(*lists)
#    ax[0][1].bar(x,y)
#    ax[0][1].set_xlabel('Interval')
#    ax[0][1].set_ylabel('Pmf')
#    fig.suptitle('Node3:Pmf for Loss Burst Len and Interval for Run_no'+str(i))
#    fig.savefig('img/Node_3/Pmf_Run_no'+str(i)+'.png')
#    fig.clf()
#    plt.close(fig)
#    
#
#for i in range(0,len(recv_4)):
#    fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,sharey=False,squeeze=False)
#    retrun =get_frame_value(recv_4[i])[1]
#    burst_len= loss_burst_pmf(retrun)
#    lists=burst_len.items()
#    x, y = zip(*lists)
#    ax[0][0].bar(x,y)
#    ax[0][0].set_xlabel('Loss Burst Len')
#    ax[0][0].set_ylabel('Pmf')
##    retrun =get_frame_value(recv_1[i])[1]
#    interval= loss_burst_interval(retrun)
#    lists=interval.items()
#    x, y = zip(*lists)
#    ax[0][1].bar(x,y)
#    ax[0][1].set_xlabel('Interval')
#    ax[0][1].set_ylabel('Pmf')
#    fig.suptitle('Node4:Pmf for Loss Burst Len and Interval for Run_no'+str(i))
#    fig.savefig('img/Node_4/Pmf_Run_no'+str(i)+'.png')
#    fig.clf()
#    plt.close(fig)
#    



