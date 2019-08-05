# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:57:34 2019

@author: Aashish Ravindran
"""

import pandas as pd 
from global_functions import get_count
import matplotlib.pyplot as plt
import numpy as np
from probabily_mass_function import *


def plot_data_master(recv,path_to_file,anatype):
    """
    1) This function plots two types of vizualizations one is the raw data per run
    2) Pmf for burst len and interval for per run
    3) Inputs : receiver{},path to file ->string and type of analysys
    4)rtype 0
    
    """
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

def plot_consolidated_run_master(receivers,path):
    """
    this function plots across all runs the pmf for burst len and interval per receiver
    input: Array of all receivers raw Data 'Y' and 'N'
    rtype= none    
    """ 
    ## Aggragated Pmf Master
    nrows=4
    ncols =2

    fig,ax=plt.subplots(nrows,ncols,figsize=(20,10))
    i=0
    while i < nrows:
        j=0
        while j < ncols:
            receiver=get_allruns(receivers[i])
            ret=consolidated_pmf(receiver,1)[0]
            lists=ret.items()
            x,y=zip(*lists)
            ax[i][j].bar(x,y)
            ax[i][j].set_title('Burst Len  Vs Pmf across all runs Node'+str(i+1),fontsize=10,pad=-10)  
            j+=1
            ret=consolidated_pmf(receiver,2)[0]
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


def plot_most_commom_pmf(recv_arr,path,frame_rate,k):
    """
    This function is used to plot the Top 10 frame NUmbers which have the highest probability of being lost 
    Inputs:array of all receivers,frame rate,path to store fig and k->top k values 
    rtype:0
    
    """
    c=get_count(str(frame_rate))[1]
    count=1
    for receiver in recv_arr:
        recv_all_runs=get_allruns(receiver)
        mf=most_frequent_losses_pmf(recv_all_runs,k,c)
        x,y=zip(*mf)
        plt.bar(x,y,label='Recv'+str(count))
        count+=1
    plt.xlabel('Frames')
    plt.ylabel('Pmf')
    plt.legend()
    plt.title("Top"+str(k)+" Frames which have the highest probabilty of being lost for"+str(frame_rate)+"Mbps")
    plt.savefig(str(path)+'/'+'Most_loss.png')
    plt.clf()
    return 0

def plot_bad_runs(recv_arr,path,frame_rate):
    """
    plot percentage of frames loss per run/per recv 
    plot avg frame loss % across all runs per receivers
    rtype:none
    Input:array of receivers, path to store file and frame rate 
    """
    aggr_bad_run={}
    col=['blue','red','orange','green']
    for idx,receiver in enumerate(recv_arr):
        recv_all_runs=get_allruns(receiver)
        ret=bad_runs_across_runs(recv_all_runs)   
        x,y=zip(*(ret.items()))            
        plt.plot(x,y,label='Recv'+str(idx+1),color=col[idx])
        
        aggr_bad_run['Recv'+str(idx+1)]=statistics.mean(y) ## Run Avg gives recv Value
    plt.title("% of frames lost per Run per Recv for"+str(frame_rate)+" Mbps")
    plt.legend()
    plt.savefig(str(path)+'/'+'Frame_loss_percentage'+str(frame_rate)+'Mbps.png')
   
    plt.clf()


    x,y=zip(*(aggr_bad_run.items()))
    plt.bar(x,y)
    plt.title("Avg Frame_loss per Recv"+str(frame_rate)+" Mbps")
    plt.savefig(str(path)+'/'+'Avg Frame_loss'+str(frame_rate)+'Mbps.png')
    plt.clf()
    return 0

def plot_statistical_highlights(recv_arr,path,frame_rate,analysis_type):
    """
    plot max ,min median and mean for burst len and interval pmfs per receiver
    input analysis_type 1 for burst len, 0 for interval 
    """
    
    
    col=['blue','red','orange','green']
    
    if analysis_type == 1:
        for index,receivers in enumerate(recv_arr):
            recv_all_runs=get_allruns(receivers)
            x=['Max','Min','Median','Average']
            re=consolidated_pmf(recv_all_runs,1)[1]
            plt.bar(x,re,label='recv'+str(index+1),color=col[index])
        
        plt.xlabel('Min,Max,Avg,Median burst len across receivers')
        plt.ylabel('Pmf Of Burst Len')
        plt.title("Statistical Highlights of Pmfs of Burst Len across receivers for"+str(frame_rate)+" Mbps")
        plt.legend()
        plt.savefig(str(path)+'/'+'Burst_len_'+str(frame_rate)+'Mbps.png')
        plt.clf()        
    
    elif analysis_type==0:
        for index,receivers in enumerate(recv_arr):
            recv_all_runs=get_allruns(receivers)
            x=['Max','Min','Median','Average']
            re=consolidated_pmf(recv_all_runs,0)[1]
            plt.bar(x,re,label='recv'+str(index+1),color=col[index])
        
        plt.xlabel('Min,Max,Avg,Median Interval len across receivers')
        plt.ylabel('Pmf Of Burst Len')
        plt.title("Statistical Highlights of Pmfs of Interval across receivers for"+str(frame_rate)+" Mbps")
        plt.legend()
        plt.savefig(str(path)+'/'+'Interval_'+str(frame_rate)+'Mbps.png')
        plt.clf()
    return 0

def plot_recv_loss_combination(loss_aggrgation,combtoplot,path,frame_rate,NoOfRuns):
    df=recv_combination_loss(loss_aggrgation,combtoplot,NoOfRuns)
    data=df.to_dict() 
    x,y=zip(*(data.items()))
    
    if combtoplot==4:
        plt.bar(x,y)
        plt.xlabel('Frame_no')
        plt.ylabel('Percentage')
        plt.title('Worse Case Abalysis for'+str(frame_rate))
        plt.savefig(str(path)+'/'+'Worse_Case'+str(frame_rate)+'Mbps.png')
        plt.clf()
        
    
    elif combtoplot==3:
        plt.bar(x,y)
        plt.xlabel('Frame_no')
        plt.ylabel('Percentage')
        plt.title('Three_Recv Case Abalysis for'+str(frame_rate))
        plt.savefig(str(path)+'/'+'Three_Recv'+str(frame_rate)+'Mbps.png')
        plt.clf()
    else:
        plt.bar(x,y)
        plt.xlabel('Frame_no')
        plt.ylabel('Percentage')
        plt.title('Two_Recv Case Abalysis for'+str(frame_rate))
        plt.savefig(str(path)+'/'+'Two_Recv'+str(frame_rate)+'Mbps.png')
        plt.clf()
    return 0
    
    
        
    