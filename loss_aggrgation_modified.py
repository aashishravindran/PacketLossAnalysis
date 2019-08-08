#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:19:22 2019

@author: ashubunutu
"""

from global_functions import get_count
import matplotlib.pyplot as plt
import numpy as np
from probabily_mass_function import *


def finite_sm_master(fin1,fin2,fin3,fin4):
     run=[]
     for i in range(0,500):
           #================================Append appropriate values based on the condition==========================       
            if  (i in fin1 and i  in fin2  and i  in fin3 and i  in fin4):
                run.append(1)
            elif  (i in fin1 and i  in fin2  and i  in fin3 and i  not in fin4):
                run.append(2)
            elif  (i in fin1 and i  in fin2  and i  not in fin3 and i  in fin4):
                run.append(3)
            elif  (i in fin1 and i not in fin2  and i  in fin3 and i  in fin4):
                run.append(4)
            elif  (i in fin1 and i  in fin2  and i not in fin3 and i  not in fin4):
                run.append(5)
            elif  (i in fin1 and i not in fin2  and i  in fin3 and i  not in fin4):
                run.append(6)
            elif  (i in fin1 and i  not in fin2  and i not in fin3 and i  in fin4):
                run.append(7)
            elif  (i not in fin1 and i  in fin2  and i  in fin3 and i  in fin4):
                 run.append(8)
            elif  (i not in fin1 and i  in fin2  and i  not in fin3 and i  in fin4):
                 run.append(9)
            elif  (i not in fin1 and i  in fin2  and i  in fin3 and i  not in fin4):
                 run.append(10)
            elif  (i not in fin1 and i  not in fin2  and i  in fin3 and i  in fin4):
                 run.append(11)
            elif  (i not in fin1 and i  not in fin2  and i  in fin3 and i  not in fin4):
                 run.append(12)
            elif  (i not in fin1 and i  not in fin2  and i  not in fin3 and i  in fin4):
                 run.append(13)
            elif  (i not in fin1 and i  in fin2  and i  not in fin3 and i  not in fin4):
                 run.append(14)
            elif  (i in fin1 and i not in fin2  and i  not in fin3 and i  not in fin4):
                run.append(15)
            elif  (i not in fin1 and i  not in fin2  and i  not in fin3 and i  not in fin4):
                run.append(16)
            
            
     return run



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
loss_Aggr={}
get_len=[]
get_len.extend([len(recv_1),len(recv_2),len(recv_3),len(recv_4)])
result = all(elem == get_len[0] for elem in get_len)

if result == True:
    print("Number of Runs is the same")
    print("Number Of Runs:"+str(get_len))
    count=get_len[0]
else:
    count=0


for i in range(0,count):
    
    recv1=get_frame_value(recv_1[i])[3]
    
    recv2=get_frame_value(recv_2[i])[3]
    
    recv3=get_frame_value(recv_3[i])[3]
       
    recv4=get_frame_value(recv_4[i])[3]
    
    loss_Aggr[i]=finite_sm_master(recv1,recv2,recv3,recv4)
    
    




