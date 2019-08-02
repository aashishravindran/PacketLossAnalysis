#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:43:14 2019

@author: ashubunutu
"""


################### Driver Code for Pmf Starts Here=================================================


import pandas as pd 
import os
from get_count import get_count
import matplotlib.pyplot as plt
import numpy as np
from probabily_mass_function import *
from vizualizations import *
import statistics



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
k=10;
c=get_count(str(frame1))[1]


rec1=get_allruns(recv_1)
rec2=get_allruns(recv_2)
rec3=get_allruns(recv_3)
rec4=get_allruns(recv_4)


mf1=most_frequent_losses_pmf(rec1,k,c)
mf2=most_frequent_losses_pmf(rec2,k,c)
mf3=most_frequent_losses_pmf(rec3,k,c)
mf4=most_frequent_losses_pmf(rec4,k,c)

x,y=zip(*mf1)
plt.bar(x,y,label='recv_1')

x,y=zip(*mf2)
plt.bar(x,y,label='recv_2')



x,y=zip(*mf3)
plt.bar(x,y,label='recv_3')


x,y=zip(*mf4)
plt.bar(x,y,label='recv_4')
plt.legend()
plt.xlabel('Frames')
plt.xlabel('Pmf')
plt.title("Top"+str(k)+" Frames which have the highest probabilty of being lost for"+str(frame1)+"Mbps")
plt.savefig(str(dirName)+'/'+'Most_loss.png')
plt.clf()


#==================================================Avergat Burst Leb size======
##Frame Rate Level
x=['Max','Min','Median','Average']
re1=consolidated_pmf(rec1,1)[1]
plt.bar(x,re1,label='recv_1',color='blue')
re2=consolidated_pmf(rec2,1)[1]
plt.bar(x,re2,label='recv_2',color='red')
re3=consolidated_pmf(rec3,1)[1]
plt.bar(x,re3,label='recv_3',color='green')
re4=consolidated_pmf(rec4,1)[1]
plt.bar(x,re4,label='recv_4',color='orange')
plt.legend()
plt.xlabel('Min,Max,Avg,Median burst len across receivers')
plt.xlabel('Pmf')
plt.title("Statistical Highlights of Pmfs of Burst Len across receivers for"+str(frame1)+" Mbps")
plt.savefig(str(dirName)+'/'+'Burst_len_'+str(frame1)+'Mbps.png')
plt.clf()
#=================================================Interval=====================
x=['Max','Min','Median','Average']
re1=consolidated_pmf(rec1,2)[1]
plt.bar(x,re1,label='recv_1',color='blue')
re2=consolidated_pmf(rec2,2)[1]
plt.bar(x,re2,label='recv_2',color='red')
re3=consolidated_pmf(rec3,2)[1]
plt.bar(x,re3,label='recv_3',color='green')
re4=consolidated_pmf(rec4,2)[1]
plt.bar(x,re4,label='recv_4',color='orange')
plt.legend()
plt.xlabel('Min,Max,Avg,Median Interval across receivers')
plt.xlabel('Pmf')
plt.title("Statistical Highlights of Pmfs of Interval across receivers for"+str(frame1)+" Mbps")
plt.savefig(str(dirName)+'/'+'Interval_'+str(frame1)+'Mbps.png')
plt.clf()
#==========================================% Bad Runs==========================
arr=[]
aggr_bad_run={}
arr.extend([get_allruns(recv_1),get_allruns(recv_2),get_allruns(recv_3),get_allruns(recv_4)])
col=['blue','red','orange','green']
for idx,i in enumerate(arr):
    print(col[idx])
    ret=bad_runs_across_runs(i)   
    x,y=zip(*(ret.items()))            
    plt.plot(x,y,label='Recv'+str(idx+1),color=col[idx])
    plt.legend()
    aggr_bad_run['Recv'+str(idx+1)]=statistics.mean(y) ## Run Avg gives recv Value


plt.title("% of frames lost per Run per Recv for"+str(frame1)+" Mbps")
plt.savefig(str(dirName)+'/'+'Frame_loss_percentage'+str(frame1)+'Mbps.png')
plt.clf()


x,y=zip(*(aggr_bad_run.items()))
plt.bar(x,y)
plt.title("Avg Frame_loss per Recv"+str(frame1)+" Mbps")
plt.savefig(str(dirName)+'/'+'Avg Frame_loss'+str(frame1)+'Mbps.png')
plt.clf()
#======================Shortend Duration Analysis==========================================






#====Interval and Burst len consolidated probabiltiy accross all recv===========================================
#Code TBD
#
#rec1=get_allruns(recv_1)
#
#rec2=get_allruns(recv_2)
#
#rec3=get_allruns(recv_3)
#
#rec4=get_allruns(recv_4)
#
#recv_arr.extend([rec1,rec2,rec3,rec4])
#ret=across_all_recv(recv_arr,1)
#x,y=zip(*(ret.items()))
#plt.bar(x,y,label='Bursrt Len',color='blue')
#
#ret=across_all_recv(recv_arr,2)
#x,y=zip(*(ret.items()))
#plt.scatter(x,y,label='Interval',color='orange')
#plt.legend()