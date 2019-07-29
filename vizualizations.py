# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:57:34 2019

@author: Aashish Ravindran
"""

import pandas as pd 
from get_count import get_count
import matplotlib.pyplot as plt
import numpy as np
from pmf import *
from probabily_mass_function import *

frame1=24
interval=1

name= open("files/"+str(frame1)+"Mbps"+"_1.txt")
name_1=open("files/"+str(frame1)+"Mbps"+"_2.txt")
name_2=open("files/"+str(frame1)+"Mbps"+"_3.txt")
name_3=open("files/"+str(frame1)+"Mbps"+"_4.txt")



recv_1=file_read(name)
recv_2=file_read(name_1)
recv_3=file_read(name_2)
recv_4=file_read(name_3)



#============= Raw Data from All Receivers==================#
for i in range(0,len(recv_1)):
      plt.bar(get_frame_value(recv_1[i])[0],get_frame_value(recv_1[i])[1])
      plt.xlabel('SeqNo', fontsize=18)
      plt.ylabel('Frame_received/Lost', fontsize=16)
      plt.title('img/Node_1/Run_no'+str(i))
      plt.savefig('img/Node_1/Run_no'+str(i)+'.png')
      plt.clf()

for i in range(0,len(recv_2)):
      plt.bar(get_frame_value(recv_2[i])[0],get_frame_value(recv_2[i])[1])
      plt.xlabel('SeqNo', fontsize=18)
      plt.ylabel('Frame_received/Lost', fontsize=16)
      plt.title('img/Node_2/Run_no'+str(i))
      plt.savefig('img/Node_2/Run_no'+str(i)+'.png')
      plt.clf()


for i in range(0,len(recv_3)):
      plt.bar(get_frame_value(recv_3[i])[0],get_frame_value(recv_3[i])[1])
      plt.xlabel('SeqNo', fontsize=18)
      plt.ylabel('Frame_received/Lost', fontsize=16)
      plt.title('img/Node_3/Run_no'+str(i))
      plt.savefig('img/Node_3/Run_no'+str(i)+'.png')
      plt.clf()



for i in range(0,len(recv_4)):
      plt.bar(get_frame_value(recv_4[i])[0],get_frame_value(recv_4[i])[1])
      plt.xlabel('SeqNo', fontsize=18)
      plt.ylabel('Frame_received/Lost', fontsize=16)
      plt.title('img/Node_4/Run_no'+str(i))
      plt.savefig('img/Node_4/Run_no'+str(i)+'.png')
      plt.clf()
#========================================Pmf for All Runs per receiver==================##     
for i in range(0,len(recv_1)):
    loss_burst=get_frame_value(recv_1[i])[2]
    probability=probabilty_mass_function(loss_burst)
#    probability=probabilty(aggr_frame_loss,interval)
    lists=probability.items()
    x, y = zip(*lists)
    plt.bar(x,y)
    plt.xlabel('Interval', fontsize=18)
    plt.ylabel('PMF of Lost Frames', fontsize=16)
    plt.title('Node1:PMF_of_lost_frames_for_Run_No'+str(i))
    plt.savefig('img/Node_1/PMF_of_lost_frames_for_Run_N0'+str(i)+'.png')
    plt.clf()
for i in range(0,len(recv_2)):
    loss_burst=get_frame_value(recv_2[i])[2]
    probability=probabilty_mass_function(loss_burst)
    lists=probability.items()
    x, y = zip(*lists)
    plt.bar(x,y)
    plt.xlabel('Interval', fontsize=18)
    plt.ylabel('PMF of Lost Frames', fontsize=16)
    plt.title('Node2:PMF_of_lost_frames_for_Run_No'+str(i))
    plt.savefig('img/Node_2/PMF_of_lost_frames_for_Run_N0'+str(i)+'.png')
    plt.clf()
for i in range(0,len(recv_3)):
    loss_burst=get_frame_value(recv_3[i])[2]
    probability=probabilty_mass_function(loss_burst)
    lists=probability.items()
    x, y = zip(*lists)
    plt.bar(x,y)
    plt.xlabel('Interval', fontsize=18)
    plt.ylabel('PMF of Lost Frames', fontsize=16)
    plt.title('Node3:PMF_of_lost_frames_for_Run_No'+str(i))
    plt.savefig('img/Node_3/PMF_of_lost_frames_for_Run_N0'+str(i)+'.png')
    plt.clf()
for i in range(0,len(recv_4)):
    loss_burst=get_frame_value(recv_4[i])[2]
    probability=probabilty_mass_function(loss_burst)
    lists=probability.items()
    x, y = zip(*lists)
    plt.bar(x,y)
    plt.xlabel('Interval', fontsize=18)
    plt.ylabel('PMF of Lost Frames', fontsize=16)
    plt.title('Node3:PMF_of_lost_frames_for_Run_No'+str(i))
    plt.savefig('img/Node_4/PMF_of_lost_frames_for_Run_N0'+str(i)+'.png')
    plt.clf()
#========================================Get Consolidate Runs=============
ret=consolidated_run(recv_1)
lists=ret.items()
x, y = zip(*lists)
plt.bar(x,y)
plt.xlabel('Interval', fontsize=18)
plt.ylabel('PMF of Lost Frames Across All Runs', fontsize=16)
plt.title('Node1:Aggregated_Pmf')
plt.savefig('img/Node_1/Aggregated_pmf.png')

plt.clf()

ret=consolidated_run(recv_2)
lists=ret.items()
x, y = zip(*lists)
plt.bar(x,y)
plt.xlabel('Interval', fontsize=18)
plt.ylabel('PMF of Lost Frames Across All Runs', fontsize=16)
plt.title('Node2:Aggregated_Pmf')
plt.savefig('img/Node_2/Aggregated_pmf.png')

plt.clf()

ret=consolidated_run(recv_3)
lists=ret.items()
x, y = zip(*lists)
plt.bar(x,y)
plt.xlabel('Interval', fontsize=18)
plt.ylabel('PMF of Lost Frames Across All Runs', fontsize=16)
plt.title('Node3:Aggregated_Pmf')
plt.savefig('img/Node_3/Aggregated_pmf.png')

plt.clf()

ret=consolidated_run(recv_4)
lists=ret.items()
x, y = zip(*lists)
plt.bar(x,y)
plt.xlabel('Interval', fontsize=18)
plt.ylabel('PMF of Lost Frames Across All Runs', fontsize=16)
plt.title('Node4:Aggregated_Pmf')
plt.savefig('img/Node_4/Aggregated_pmf.png')
plt.clf()




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
    





