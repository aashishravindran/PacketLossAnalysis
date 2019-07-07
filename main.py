#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:50:37 2019

@author: ashubunutu
"""

from imports import reference_ts,compute_time_sync


file=open("time_sync.txt","r") ##Global Reference File


name=["time_sync_1.txt","time_sync_2.txt","time_sync_3.txt"] # Files to have Time Synchronization wrt Global FIle


#dest="The_Great_gatsBy_logss.txt"

line=file.readlines()

reference_map=reference_ts(line)

for i,num in enumerate(name,1):
      fp=open(num,"r")
      new_file=fp.readlines()
      dest="Independence_dayyyyy"+str(i)+".txt"
      compute_time_sync(reference_map,new_file,dest) #FIle in Inports
      fp.close()
      
      