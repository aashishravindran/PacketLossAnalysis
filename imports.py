#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:52:50 2019

@author: ashubunutu
"""


def reference_ts(line):
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
    difference = []
    delay = {}
    for i in range(0, len(sync)):
        for j in range(0, len(sync[i])):
            # print(sync[i][j])
            # print(sync[i+1][j])
            if sync[i][j] in ref[0]:
                diff = sync[i + 1][j] - ref[1][ref[0].index(sync[i][j])] #calculate Time Difference
                # print(diff)
                difference.append(diff)
                delay[sync[i][j]] = diff ##Append to dictionary with seqnece Number and Delay
    return delay


def time_sync(reference, time_stamps):
    synchronied_timestamp = []
    for index,timestamp in enumerate(time_stamps):
        if index == 0:
            count=timestamp-reference
            sync_count = timestamp-count
            synchronied_timestamp.append(sync_count) #Time Sync Logic
        else:
            next_time_stamp = timestamp-sync_count #Time Sync Logic
            final_count = timestamp+next_time_stamp
            synchronied_timestamp.append(final_count)
    return synchronied_timestamp #Retrun the timestamp for each sequence no





