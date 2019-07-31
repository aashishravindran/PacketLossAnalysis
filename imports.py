#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:52:50 2019

@author: ashubunutu
"""
# Created for Time Synchronization and Delay

def reference_ts(file):
    """
    Input file object
    rtype: list[reference Time Stammps]
    reference time stamps give the first value of frame reception after a new run 
    Used for time sync delay calclualtion 
    """
    line=file.readlines()
    reference_timestamps = [];
    for i in range(0, len(line)):
        # print(i,line[i])
        if i == 0:
            reference_timestamps.append(float(line[i].split(',@')[1]))  # Get all time Stamps from the reference file
        elif "Starting" in line[i]:
            i += 1;  # skip the line with "Starting new line"
            reference_timestamps.append(float(line[i].split(',@')[1]))
    return reference_timestamps


def get_retransmission_delays(ref,sync):
    """ Calculate the retransmision delay per run for a receiver wrt to a reference,
    Input type 1= 2D Array containing seq and time stamp for reference
    Input type 2= 2D Array containing seq and time stamp for receiver to be synced
    rtype d{seq,delay}
    """
    difference = []
    delay = {}
#    print(sync[1][1])
#    return 0
    for i in range(0, len(sync)):
        
        for j in range(0, len(sync[i])):
            
            # check if seq no exist  in ref sync[i][j] ->seq  ,ref[0] is seq No of reference
            if sync[i][j] in ref[0]:
                print(sync[1][j])
                ## diff = first timestamp
                diff =  abs(ref[1][ref[0].index(sync[i][j])]-sync[1][j])
                # print(diff)
                difference.append(diff)
                delay[sync[i][j]] = diff ##Append to dictionary with seqnece Number and Delay
    return delay


def time_sync(reference, time_stamps):
    """
    Input reference time stamps[arr], time Stamps per run[arr] 
    rtype: sync time stamps
    """
    synchronied_timestamp = []
    for index,timestamp in enumerate(time_stamps):
        if index == 0: # if first value the compute the sync count->sync_count
            count=timestamp-reference
            sync_count = timestamp-count
            synchronied_timestamp.append(sync_count) #Time Sync Logic
        else: #else used previously calculated count
            next_time_stamp = timestamp-sync_count #Time Sync Logic
            final_count = timestamp+next_time_stamp
            synchronied_timestamp.append(final_count)
    return synchronied_timestamp #Retrun the timestamp for each sequence no





