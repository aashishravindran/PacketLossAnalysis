#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:50:37 2019
@author: Aashish Ravindran
"""

"""
Driver code for computing time Sync and receiver delay calculation
For simpler calculations and increased modularity, the driver code parses the text 
file while syncing timestamps at a run level

The same is repeated for Recevier delay calculations

"""

from global_functions import *


# =====================================Function Decleration Startes Here ===========================================
def reference_params(file_to_sync):
    """
    input: File Object- Please pass the reference file here
    rtype:dict{runNo:[[seq],[timestamps]]}
    In the reference file For each run, the funcrtion return seq no and timestamps
    """
    
    ##Parses a text file and calls the time sync function which sync wrt to the reference ts
    line=file_to_sync.readlines()
    print(line)
    seq = []
    times = []
    val = []
    SyncLog = {}
    count = 0;
    for i in range(0, len(line)):

        if "Starting" in line[i] or i == len(line)-1:
            val = [seq, times] ## 2D Array containing seq and synchronized time Stamps
            SyncLog[count] = val #Appending the value to the dictionary for delay calculation
            seq = [];
            times = [];
            count += 1

        else:
            times.append(float(line[i].split(',@')[1]))
            seq.append(int(line[i].split('and')[0].split('=')[1]))

    return SyncLog
    


def time_sync_driver(reference_map, file_to_sync):
    """
     Drive code to get sync time stamps per run on a particualr receiver
     Input arr,file_obj arr->reference time stamps, file->file to sync
     rtype:haspmap {runO:[[seq],[Sync Time Stamps]]}
     
    """
    ##Parses a text file and calls the time sync function which sync wrt to the reference ts
    ls = file_to_sync.readlines()
    seq = []
    times = []
    val = []
    SyncLog = {}
    count = 0;
    for i in range(0, len(ls)):

        if "Starting" in ls[i] or i == len(ls)-1:
            ### pass the value per run into ts func and get sync time time stamps
            reference = reference_map[count]
            sync = time_sync(reference, times)
            val = [seq, sync] ## 2D Array containing seq and synchronized time Stamps
            SyncLog[count] = val #Appending the value to the dictionary for delay calculation
            seq = [];
            times = [];
            count += 1

        else:
            times.append(float(ls[i].split(',@')[1]))
            seq.append(int(ls[i].split('and')[0].split('=')[1]))

    return SyncLog
# ==================Call Transmission Delay====================================

def recv_delay_calucaltion_driver(ref,recv):
    """
    compute per run the receiver delay wrt to the ref node and one receiver
    input=dict{},dict{}
    rtype=dict{}
    """
      ## This function for each run caluclates a dictionary and return the retransmisison delay value 
    dictionary = {}
    for key, value in enumerate(recv):
             ## ref[key] ==[seq,timestamp]
             ##recv[key]==[seq,timestamp]
            dictionary[key] = get_retransmission_delays(ref[key], recv[key])
            
    return dictionary


#=============================Execution========================================

file=open('files/ts_logs/time_sync_10_54_3.txt','r')
Sync_log_1 = open('files/ts_logs/time_sync_10_54_4.txt','r')
Sync_log_2 = open('files/ts_logs/time_sync_10_54_5.txt','r')


reference_map = reference_ts(file) ## Get first timestamps after each run 
file.close()
# Passing the reference file to get time Stamps
file=open('files/ts_logs/time_sync_10_54_3.txt','r')
ref=reference_params(file) # Reference file for recevier delay calculation
sl1=time_sync_driver(reference_map,Sync_log_1) # Time Sync for Recv 1
sl2=time_sync_driver(reference_map,Sync_log_2) # Time Sync for Recv 2


## Please make sure receivers are synchdromnized before calculating receiver delays
receiver_delay=recv_delay_calucaltion_driver(ref,sl1)  ## Receiver 





