# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:57:34 2019

@author: Aashish Ravindran
"""

import pandas as pd 
from get_count import get_count
import matplotlib.pyplot as plt
import numpy as np
from probabily_mass_function import *



def plot_data_master(recv,path_to_file,anatype):
    ## anatype =1 for ray data
    if anatype==1:
        for i in range(0,len(recv)):
            plt.bar(get_frame_value(recv[i])[0],get_frame_value(recv[i])[1])
            plt.xlabel('SeqNo', fontsize=18)
            plt.ylabel('Frame_received/Lost', fontsize=16)
            plt.title(str(path_to_file.split('/')[1])+str(path_to_file)+'Run_no'+str(i))
            plt.savefig(str(path_to_file)+'Run_no'+str(i)+'.png')
            plt.clf()
    elif anatype==2: ## anatype =2 for pmf implementation
        for i in range(0,len(recv)):
            fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,sharey=False,squeeze=False)
            retrun =get_frame_value(recv[i])[1]
            burst_len= loss_burst_pmf(retrun)
            lists=burst_len.items()
            x, y = zip(*lists)
            ax[0][0].bar(x,y)
            ax[0][0].set_xlabel('Loss Burst Len')
            ax[0][0].set_ylabel('Pmf')

            interval= loss_burst_interval(retrun)
            lists=interval.items()
            x, y = zip(*lists)
            ax[0][1].bar(x,y)
            ax[0][1].set_xlabel('Interval')
            ax[0][1].set_ylabel('Pmf')
            fig.suptitle(str(path_to_file.split('/')[1])+path_to_file[path_to_file.index('Node'):path_to_file.rfind('/')]+':'+'Pmf for Loss Burst Len and Interval for Run_no'+str(i))
            fig.savefig(str(path_to_file)+'Pmf_Run_no'+str(i)+'.png')
            fig.clf()
            plt.close(fig)
         
        
    return 0;

def plot_consolidated_run_master(arr,path):
    ## Aggragated Pmf Master
    nrows=4
    ncols =2

    fig,ax=plt.subplots(nrows,ncols,figsize=(20,10))
    i=0
    while i < nrows:
        j=0
        while j < ncols:
            recv=get_allruns(arr[i])
            ret=consolidated_pmf(recv,1)[0]
            lists=ret.items()
            x,y=zip(*lists)
            ax[i][j].bar(x,y)
            ax[i][j].set_title('Burst Len  Vs Pmf across all runs Node'+str(i+1),fontsize=10,pad=-10)  
            j+=1
            ret=consolidated_pmf(recv,2)[0]
            lists=ret.items()
            x,y=zip(*lists)
            ax[i][j].bar(x,y)
            ax[i][j].set_title('Interval Vs Pmf across all runs Node'+str(i+1),fontsize=10,pad=-10)
            j+=1
    
        i+=1

    fig.suptitle('Plot Recv wise aggregation of Burse size and Interval for'+path.split('/')[1])
    fig.savefig(path+'/Aggregared.png')
    plt.close(fig)
    return 0






