#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:50:37 2019

@author: ashubunutu
"""

from imports import get_retransmission_delays,time_sync,reference_ts


# =====================================Function Decleration Startes Here ===========================================

def get_seq_and_ts_not(file_to_sync):
    ##Parses a text file and calls the time sync function which sync wrt to the reference ts
    line=file_to_sync.readlines()
    print(line)
    seq = []
    times = []
    val = []
    SyncLog = {}
    count = 0;
    for i in range(0, len(line)):

        if "Starting" in line[i]:
            ### pass the value per run into ts func and get sync time time stamps
#            reference = reference_map[count]
#            sync = time_sync(reference, times)
            val = [seq, times] ## 2D Array containing seq and synchronized time Stamps
            SyncLog[count] = val #Appending the value to the dictionary for delay calculation
            seq = [];
            times = [];
            count += 1

        else:
            times.append(float(line[i].split(',@')[1]))
            seq.append(int(line[i].split('and')[0].split('=')[1]))

    return SyncLog
    


def parse_tf_and_get_ts(reference_map, file_to_sync):
    ##Parses a text file and calls the time sync function which sync wrt to the reference ts
    ls = file_to_sync.readlines()
    seq = []
    times = []
    val = []
    SyncLog = {}
    count = 0;
    for i in range(0, len(ls)):

        if "Starting" in ls[i]:
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
# ==================Call Transmission Delay and Print Value======================================================

def execute_delay_fn_print(ref,recv):
      ## This function for each run caluclates a dictionary and return the retransmisison delay value 
      dictionary = {}
      for key, value in enumerate(recv):
             ## ref[key] ==[seq,timestamp]
             ##recv[key]==[seq,timestamp]
            dictionary[key] = get_retransmission_delays(ref[key], recv[key])
            
      return dictionary

file=open('files/ts_logs/time_sync_10_54_3.txt','r')
Sync_log_1 = open('files/ts_logs/time_sync_10_54_4.txt','r')
Sync_log_2 = open('files/ts_logs/time_sync_10_54_5.txt','r')


reference_map = reference_ts(file) # Passing the reference file to get time Stamps
f=open('files/ts_logs/time_sync_10_54_3.txt','r')
ref=get_seq_and_ts_not(f)
sl1=parse_tf_and_get_ts(reference_map,Sync_log_1) # Time Sync for Recv 1
sl2=parse_tf_and_get_ts(reference_map,Sync_log_2) # Time Sync for Recv 2


## Please make sure receivers are synchdromnized before calculating receiver delays
receiver_delay=execute_delay_fn_print(ref,sl1)  ## Receiver 





