#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:50:37 2019

@author: ashubunutu
"""

from imports import get_retransmission_delays,time_sync,reference_ts


# =====================================Function Decleration Startes Here ===========================================


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
      dictionary = {}
      for key, value in enumerate(recv):
            # print(recv_1[key])
            # break
            dictionary[key] = get_retransmission_delays(ref[key], recv[key])
      return dictionary

file=open ('files/ts_logs/time_sync.txt','r')
Sync_log_1 = open('files/ts_logs/time_sync_1.txt','r')
Sync_log_2 = open('files/ts_logs/time_sync_2.txt','r')

line = file.readlines()

reference_map = reference_ts(line) # Passing the reference file to get time Stamps

ref=parse_tf_and_get_ts(reference_map,Sync_log_1) # Time Sync for Recv 1
recv_1=parse_tf_and_get_ts(reference_map,Sync_log_2) # Time Sync for Recv 2


## Please make sure receivers are synchdromnized before calculating receiver delays
receiver_delay=execute_delay_fn_print(ref,recv_1) # Receiver Delay Between Receivers

print(receiver_delay[0])


