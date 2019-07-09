#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:50:37 2019

@author: ashubunutu
"""

from imports import reference_ts,compute_time_sync


file=open("files/ts_logs/time_sync.txt","r") ##Global Reference File


name=["files/ts_logs/time_sync_1.txt","files/ts_logs/time_sync_2.txt"]


#dest="The_Great_gatsBy_logss.txt"

line=file.readlines()

reference_map=reference_ts(line)

for i,num in enumerate(name,1):
      fp=open(num,"r")
      new_file=fp.readlines()
      dest="files/Sync_logs"+str(i)+".txt"
      compute_time_sync(reference_map,new_file,dest)
      fp.close()
