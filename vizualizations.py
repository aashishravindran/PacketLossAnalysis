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
    aggr_frame_loss=identify_loss_burst_intervals(loss_burst)
    probability=probabilty(aggr_frame_loss,interval)
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
    aggr_frame_loss=identify_loss_burst_intervals(loss_burst)
    probability=probabilty(aggr_frame_loss,interval)
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
    aggr_frame_loss=identify_loss_burst_intervals(loss_burst)
    probability=probabilty(aggr_frame_loss,interval)
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
    aggr_frame_loss=identify_loss_burst_intervals(loss_burst)
    probability=probabilty(aggr_frame_loss,interval)
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

#========================Loss Burst Plot==============
for i in range(0,len(recv_1)):
    loss_burst=get_frame_value(recv_1[i])[2]
    aggr_frame_loss=identify_loss_burst_intervals(loss_burst)
#    probability=probabilty(aggr_frame_loss)
    lists=aggr_frame_loss.items()
    x, y = zip(*lists)
    plt.bar(x,y)
    plt.xlabel('Interval', fontsize=18)
    plt.ylabel('Loss Burst', fontsize=16)
    plt.title('Node1:Loss BurstRun_No'+str(i))
    plt.savefig('img/Node_1/Loss BurstRun_No'+str(i)+'.png')
    plt.clf()
for i in range(0,len(recv_2)):
    loss_burst=get_frame_value(recv_2[i])[2]
    aggr_frame_loss=identify_loss_burst_intervals(loss_burst)
    lists=aggr_frame_loss.items()
    x, y = zip(*lists)
    plt.bar(x,y)
    plt.xlabel('Interval', fontsize=18)
    plt.ylabel('Loss Burst', fontsize=16)
    plt.title('Node2:Loss BurstRun_No'+str(i))
    plt.savefig('img/Node_2/Loss BurstRun_No'+str(i)+'.png')
    plt.clf()
for i in range(0,len(recv_3)):
    loss_burst=get_frame_value(recv_3[i])[2]
    aggr_frame_loss=identify_loss_burst_intervals(loss_burst)
#    probability=probabilty(aggr_frame_loss)
    lists=aggr_frame_loss.items()
    x, y = zip(*lists)
    plt.bar(x,y)
    plt.xlabel('Interval', fontsize=18)
    plt.ylabel('Loss Burst', fontsize=16)
    plt.title('Node3:Loss BurstRun_No'+str(i))
    plt.savefig('img/Node_3/Loss BurstRun_No'+str(i)+'.png')
    plt.clf()
for i in range(0,len(recv_4)):
    loss_burst=get_frame_value(recv_4[i])[2]
    aggr_frame_loss=identify_loss_burst_intervals(loss_burst)
#    probability=probabilty(aggr_frame_loss)
    lists=aggr_frame_loss.items()
    x, y = zip(*lists)
    plt.bar(x,y)
    plt.xlabel('Interval', fontsize=18)
    plt.ylabel('Loss Burst', fontsize=16)
    plt.title('Node4:Loss BurstRun_No'+str(i))
    plt.savefig('img/Node_4/Loss BurstRun_No'+str(i)+'.png')
    plt.clf()





