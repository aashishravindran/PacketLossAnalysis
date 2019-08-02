# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 16:10:49 2019

@author: Aashish Ravindran
"""

import pandas as pd 
import os
from get_count import get_count
import matplotlib.pyplot as plt
import numpy as np
from probabily_mass_function import *
from vizualizations import *
import statistics





frame1=24

s_name= open("files/"+str(frame1)+'_1.txt')
s_name_1=open("files/"+str(frame1)+'_2.txt')
s_name_2=open("files/"+str(frame1)+'_3.txt')
s_name_3=open("files/"+str(frame1)+'_4.txt')



r_1=file_read(s_name)
r_2=file_read(s_name_1)
r_3=file_read(s_name_2)
r_4=file_read(s_name_3)

dirName='img/'+str(frame1)+'Mbps_short'

try:
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

arr=[r_1,r_2,r_3,r_4]
path=dirName
plot_consolidated_run_master(arr,path) 


k=10;
c=get_count(str(frame1))[1]


rec1=get_allruns(r_1)
rec2=get_allruns(r_2)
rec3=get_allruns(r_3)
rec4=get_allruns(r_4)


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
plt.title("Top"+str(k)+" Frames which have the highest probabilty of being lost for_short"+str(frame1)+"Mbps")
plt.savefig(str(dirName)+'/'+'Most_los_short.png')
plt.clf()




arr=[]
aggr_bad_run={}
arr.extend([get_allruns(r_1),get_allruns(r_2),get_allruns(r_3),get_allruns(r_4)])
col=['blue','red','orange','green']
for idx,i in enumerate(arr):
    print(col[idx])
    ret=bad_runs_across_runs(i)   
    x,y=zip(*(ret.items()))            
    plt.plot(x,y,label='Recv'+str(idx+1),color=col[idx])
    plt.legend()
    aggr_bad_run['Recv'+str(idx+1)]=statistics.mean(y) ## Run Avg gives recv Value


plt.title("% of frames lost per Run per Recv for"+str(frame1)+" Mbps")
plt.savefig(str(dirName)+'/'+'Frame_loss_percentage_short'+str(frame1)+'Mbps.png')
plt.clf()


x,y=zip(*(aggr_bad_run.items()))
plt.bar(x,y)
plt.title("Avg Frame_loss per Recv"+str(frame1)+" Mbps")
plt.savefig(str(dirName)+'/'+'Avg Frame_loss_short'+str(frame1)+'Mbps.png')
plt.clf()

