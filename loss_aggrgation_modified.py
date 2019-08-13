#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:19:22 2019
@author: Aashish Ravindran
"""

from global_functions import *
import matplotlib.pyplot as plt
import numpy as np

frame1=54
name= open("files/"+str(frame1)+"Mbps"+"_1.txt")
name_1=open("files/"+str(frame1)+"Mbps"+"_2.txt")
name_2=open("files/"+str(frame1)+"Mbps"+"_3.txt")
name_3=open("files/"+str(frame1)+"Mbps"+"_4.txt")

#
#count=get_count(str(frame1))
#count=count[0]

recv_1=file_read(name)
recv_2=file_read(name_1)
recv_3=file_read(name_2)
recv_4=file_read(name_3)

count=get_count_master(recv_1,recv_2,recv_3,recv_4)
loss_Aggr={}

for i in range(0,count):
    
    recv1=get_frame_value(recv_1[i])[3]
    
    recv2=get_frame_value(recv_2[i])[3]
    
    recv3=get_frame_value(recv_3[i])[3]
       
    recv4=get_frame_value(recv_4[i])[3]
    
    loss_Aggr[i]=finite_sm_master(recv1,recv2,recv3,recv4)
    
    
file=open("files/"+frame1+"Mbps"+"Data_Aggregation_Logs.txt","w")
file.write(frame1+"MbpsLogs\n")

for i, k in enumerate(loss_Aggr):
    print("==============Run No========",k)
    file.write("==============Run No========"+str(k)+"\n")
    new=loss_Aggr[k];
    for i in range(0,500):
        print("Index: "+str(i)+" Value:"+str(new[i]))
        file.write("Index:"+str(i)+","+"Value:"+str(new[i])+"\n")

file.close()




