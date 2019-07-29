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







nrows = 4
fig, ax = plt.subplots(nrows, 2,figsize=(20,10))

recv=get_allruns(recv_1,1)


k = Counter(recv) 
print(k.most_common(3))
#ret=consolidated_run(recv,1)
lists=recv.items()
x,y=zip(*lists)
ax[0][0].bar(x,y)
ax[0][0].set_title('Burst Len Vs Pmf across all runs Node 1',fontsize=10,pad=-10)

recv=get_allruns(recv_1,2)
k = Counter(recv) 
print(k.most_common(3))
#ret=consolidated_run(recv,1)
lists=recv.items()
x,y=zip(*lists)
ax[0][1].bar(x,y)
ax[0][1].set_title('Interval Vs Pmf across all runs Node 1',fontsize=10,pad=-10)

recv=get_allruns(recv_2,1)
k = Counter(recv) 
print(k.most_common(3))
#ret=consolidated_run(recv,1)
lists=recv.items()
x,y=zip(*lists)
ax[1][0].bar(x,y)
ax[1][0].set_title('Burst Len Vs Pmf across all runs Node 2',fontsize=10,pad=-10)



recv=get_allruns(recv_2,2)
k = Counter(recv) 
print(k.most_common(3))
#ret=consolidated_run(recv,1)
lists=recv.items()
x,y=zip(*lists)
ax[1][1].bar(x,y)
ax[1][1].set_title('Interval Vs Pmf across all runs Node 2',fontsize=10,pad=-10)



recv=get_allruns(recv_3,1)
k = Counter(recv) 
print(k.most_common(3))
#ret=consolidated_run(recv,1)
lists=recv.items()
x,y=zip(*lists)
ax[2][0].bar(x,y)
ax[2][0].set_title('Burst Len Vs Pmf across all runs Node 3',fontsize=10,pad=-10)

recv=get_allruns(recv_3,2)
k = Counter(recv) 
print(k.most_common(3))
#ret=consolidated_run(recv,1)
lists=recv.items()
x,y=zip(*lists)
ax[2][1].bar(x,y)
ax[2][1].set_title('Interval Vs Pmf across all runs Node 3',fontsize=10,pad=-10)


recv=get_allruns(recv_4,1)
k = Counter(recv) 
print(k.most_common(3))
#ret=consolidated_run(recv,1)
lists=recv.items()
x,y=zip(*lists)
ax[3][0].bar(x,y)
ax[3][0].set_title('Burst Len Vs Pmf across all runs Node 4',fontsize=10,pad=-10)

recv=get_allruns(recv_4,2)

#ret=consolidated_run(recv,1)
lists=recv.items()
x,y=zip(*lists)
ax[3][1].bar(x,y)
ax[3][1].set_title('Interval Vs Pmf across all runs Node 4',fontsize=10,pad=-10)
fig.suptitle('Plot Recv wise aggregation of Burse size and Interval')
fig.savefig('img/Aggregared.png')






for i in range(0,len(recv_1)):
    fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,sharey=False,squeeze=False)
    retrun =get_frame_value(recv_1[i])[1]
    burst_len= loss_burst_pmf(retrun)
    lists=burst_len.items()
    x, y = zip(*lists)
    ax[0][0].bar(x,y)
    ax[0][0].set_xlabel('Loss Burst Len')
    ax[0][0].set_ylabel('Pmf')
#    retrun =get_frame_value(recv_1[i])[1]
    interval= loss_burst_interval(retrun)
    lists=interval.items()
    x, y = zip(*lists)
    ax[0][1].bar(x,y)
    ax[0][1].set_xlabel('Interval')
    ax[0][1].set_ylabel('Pmf')
    fig.suptitle('Node1:Pmf for Loss Burst Len and Interval for Run_no'+str(i))
    fig.savefig('img/Node_1/Pmf_Run_no'+str(i)+'.png')
    fig.clf()
    plt.close(fig)
    


for i in range(0,len(recv_2)):
    fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,sharey=False,squeeze=False)
    retrun =get_frame_value(recv_2[i])[1]
    burst_len= loss_burst_pmf(retrun)
    lists=burst_len.items()
    x, y = zip(*lists)
    ax[0][0].bar(x,y)
    ax[0][0].set_xlabel('Loss Burst Len')
    ax[0][0].set_ylabel('Pmf')
#    retrun =get_frame_value(recv_1[i])[1]
    interval= loss_burst_interval(retrun)
    lists=interval.items()
    x, y = zip(*lists)
    ax[0][1].bar(x,y)
    ax[0][1].set_xlabel('Interval')
    ax[0][1].set_ylabel('Pmf')
    fig.suptitle('Node2:Pmf for Loss Burst Len and Interval for Run_no'+str(i))
    fig.savefig('img/Node_2/Pmf_Run_no'+str(i)+'.png')
    fig.clf()
    plt.close(fig)
    

for i in range(0,len(recv_3)):
    x, y = zip(*lists)
    ax[0][0].bar(x,y)
    ax[0][0].set_xlabel('Loss Burst Len')
    ax[0][0].set_ylabel('Pmf')
#    retrun =get_frame_value(recv_1[i])[1]
    fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,sharey=False,squeeze=False)
    retrun =get_frame_value(recv_3[i])[1]
    burst_len= loss_burst_pmf(retrun)
    lists=burst_len.items()
    x, y = zip(*lists)
    ax[0][0].bar(x,y)
    ax[0][0].set_xlabel('Loss Burst Len')
    ax[0][0].set_ylabel('Pmf')
#    retrun =get_frame_value(recv_1[i])[1]
    interval= loss_burst_interval(retrun)
    lists=interval.items()
    x, y = zip(*lists)
    ax[0][1].bar(x,y)
    ax[0][1].set_xlabel('Interval')
    ax[0][1].set_ylabel('Pmf')
    fig.suptitle('Node3:Pmf for Loss Burst Len and Interval for Run_no'+str(i))
    fig.savefig('img/Node_3/Pmf_Run_no'+str(i)+'.png')
    fig.clf()
    plt.close(fig)
    

for i in range(0,len(recv_4)):
    fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,sharey=False,squeeze=False)
    retrun =get_frame_value(recv_4[i])[1]
    burst_len= loss_burst_pmf(retrun)
    lists=burst_len.items()
    interval= loss_burst_interval(retrun)
    lists=interval.items()
    x, y = zip(*lists)
    ax[0][1].bar(x,y)
    ax[0][1].set_xlabel('Interval')
    ax[0][1].set_ylabel('Pmf')
    fig.suptitle('Node4:Pmf for Loss Burst Len and Interval for Run_no'+str(i))
    fig.savefig('img/Node_4/Pmf_Run_no'+str(i)+'.png')
    fig.clf()
    plt.close(fig)
    



