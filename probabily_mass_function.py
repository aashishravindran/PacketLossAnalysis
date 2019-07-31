#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:06:24 2019

@author: ashubunutu
"""
import pandas as pd 
from collections import Counter
import matplotlib.pyplot as plt
import statistics

def loss_Aggr_file_read(file,noofruns):
    """
    Reads the results of loss aggregation and computes at a frame level across runs and across receivers, the number of frames
    lost across any 2 any 3 and all 4 receivers. 
    Note: It is imperative to run loss aggration before running this
    Note: Number of runs must be same across all receivers
    input: file object, Number of runs    
    rtype: Pandas Data Frame
    """
    
    ## Read and format the file
    line=file.readlines() 
    lits={}
    dict={}
    get_val=0;       
    for i in range(0,len(line)):
        
        #parsing the text file
        if "Run No" in line[i]:
            new_str=int(line[i].split("Run No========")[1])
            get_val=i+1;
            while 'Run No' not in line[get_val] and get_val+1 <len(line):
                get_line=line[get_val].split(",")
                frame_no=int(get_line[0].split(":")[1])
                loss_aggr_val=int(get_line[1].split(":")[1])
                get_val+=1
                lits[frame_no]=loss_aggr_val

            dict[new_str]=lits
            lits={}
    dsf=pd.DataFrame(dict)
    dsf['Frame_no']=dsf.index



    for i in range(1,noofruns):
         #print(i)
         s=str("Run_no"+str(i))
         dsf[s]=dsf[i]
         dsf.drop(columns =[i], inplace = True)
   
    x=dsf.iloc[:,1:noofruns]
    
    Tw_Recv=[5,6,7,9,10,11]
    Three_Recv=[12,13,14,15]
    
    for i, rows in x.iterrows():
        sum=0
        #print(rows,i)
        c=rows.value_counts()
#        print(c)
#        break
#        print(c)                    
        if 16 in c:
           dsf.loc[i,'WorseCase']=c[16]
        if 1 in c:
               dsf.loc[i,'BestCase']=c[1]
         
        for k in range(0,len(Tw_Recv)):
            if Tw_Recv[k] in c:
#                print(c[Tw_Recv[k]])
                sum+=c[Tw_Recv[k]]
        dsf.loc[i,'Two_Recv']=sum
        sum=0
       
        for k in range(0,len(Three_Recv)):
            if Three_Recv[k] in c:
#                print(c[Tw_Recv[k]])
                sum+=c[Three_Recv[k]]
        dsf.loc[i,'Three_Recv']=sum
        sum=0
        
    X=dsf
    return X

### Two Recv 5,6,7,9,10,11
### Three recv -12,13,1,4,1,15    
def recv_combination_loss(datafra,combination,NoOfRuns):
    
    """
    Calcualates percentage for two three and four receivers cases
    it is imperate to run loss_Aggr_file_read before runnting this function
    Input: DataFrame from loss Aggregation, combination->type of analysts to perform 2Recv loss,3 RecvLoss 4 Recv Loss
    ,no of runs
    rtype:dataframe
    """
    ## Pmf Receiver Combination
    if combination == 4:
        #s=datafra['WorseCase'].sum()
        datafra['Pmf_worse_case']=(datafra['WorseCase']/NoOfRuns)*100
        return datafra['Pmf_worse_case']
        ## Add Logic here 
    elif combination == 2 :
       #s=datafra['Two_Recv'].sum()
       datafra['Pmf_Two_Recv']=(datafra['Two_Recv']/NoOfRuns)*100
       return datafra['Pmf_Two_Recv']
       
        ## Add Logic here 
    elif combination == 3 :
       # s=datafra['Three_Recv'].sum()
        datafra['Pmf_Three_Recv']=(datafra['Three_Recv']/NoOfRuns)*100
        return datafra['Pmf_Three_Recv']
        

def file_read(file):
    """
    Reads a file and returns a dictionaary containgin run No and seqNo received for each run
    """
    #Receiver Level
    line=file.readlines()
    count=0;
    dict={}
    seqNo=[]
    for i in range(0,len(line)):
        if "Starting" in line[i]:
            dict[count]=seqNo
            seqNo=[]
            count+=1
        else:
            val=int((line[i].split('and')[0]).split('=')[1])
            seqNo.append(val)
    return dict
            
def get_frame_value(run):
    """
    get_frame_value retruns a dictionary of raw values
    Run Level
    This function gets the raw data value, append 'Y' if recevied else 'N' if not received
    """   
   
    x_axsi=[]
    bm=[]
    val={}
    for i in range(0,500):
        if i not in run:
            bm.append('N')
            val[i]='N'
            x_axsi.append(i)
            
        else:
            bm.append('Y')
            val[i]='Y'
            x_axsi.append(i)
    
         
    
    return [x_axsi,bm,val]  ## returns index,value and hashmap. Should change this to return only hashmap


def loss_burst_pmf(run):
    
    ###Run Level
    #Computes the pmf of loss burst len
    count=0
    arr=[]
    pmf={}
    for i in range(0,len(run)):
        
        if run[i] == 'Y':
            arr.append(count)
            count=0
        if run[i] == 'N':
            count+=1
    loss_burst=Counter(arr)

    
    for key,value in loss_burst.items():
#        print(key,value)
        pmf[key]=(value/len(arr))
        

    return pmf

def loss_burst_interval(run):
    #Run level
     # Computes the pmf of interval
    count =0;
    arr=[]
    pmf={}
    for i in range(0,len(run)):
        if (run[i] == 'N'):
            arr.append(count)
            count=0
        if run[i] == 'Y':
            count+=1
    interval=Counter(arr)
#    print(interval)
    for key,value in interval.items():

        pmf[key]=(value/len(arr))
    
    
    return pmf

def get_allruns(recv):
    dict={}
    for i in range(0,len(recv)):
        dict[i]=get_frame_value(recv[i])[1]
    
    return dict
    

def consolidated_pmf(recv,val):
    """
    Used to compute the pmf and interval for all runs per receiver
    """
    #Receiver level
    # used to compuet pmf and interval across all runs
    arr=[]
    stats=[]
    for key,value in recv.items():
            for i in value:
                arr.append(i) 
    if val == 1:
        burstlen=loss_burst_pmf(arr)
        b=burstlen.values()
        stats.extend([max(b),min(b),statistics.median(b),statistics.mean(b)]) #some statistical implementaiton used later
        print(stats)
        return [burstlen,stats]  #some statistical implementaiton
    else:
        interval=loss_burst_interval(arr)
        b=interval.values()
        stats.extend([max(b),min(b),statistics.median(b),statistics.mean(b)])
        return [interval,stats]

def across_all_recv(recv_arr,val):
    """
    This function computest the loss burst pmf and intervals across all recveicvers
    """
    ##Frame rate Level
    #consolidetd pmf and interval for all runs across all receivers
    arr=[]
    for recv in recv_arr:
        for key,value in recv.items():
            for i in value:
                arr.append(i)
    if val ==1:
        return loss_burst_pmf(arr) 
    else:
        return loss_burst_interval(arr)
                                         

def most_frequent_losses_pmf(recv,top_n_value,total_runs):
    ## Recevier Level
    ##Please Run 'Get All Runs Befeore Running This'
    ## this function can help identify the Frames which have the highest probabilty of being lost for a frame rate/ receiver
    count=0
    dict={}
    for key, value in recv.items():
        for idx,val in enumerate(value):
            if val == 'N':
                if idx in dict:
                    count=dict[idx]+1;
                    dict[idx]=count
                else:
                    dict[idx]=1



    for key,value in dict.items():
        dict[key]=value/total_runs
    k=Counter(dict).most_common(top_n_value)  
    return k


def bad_runs(recv):
    """
    Function to computer percentage of bad Runs per Recv
    """
    
    arr=[]
    dict={}
    for key,value in recv.items():
        for i,val in enumerate(value):
            if val =='N':
#            st=str(i)+str(val)
                arr.append(i)
    dict[key]=(len(arr)/500)*100
    arr=[]
    return dict
    
