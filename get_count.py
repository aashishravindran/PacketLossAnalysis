#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:07:17 2019

@author: ashubunutu
"""


#ata = open('48Mbps_1.txt').read()
#Ecount = data.count('Starting')
get_frame_rate=input('Enter Desired Mbps Rate')
i=0;

new_count_1=1
nc=[]


print(new_count_1)


for i in range(1,5):
    makestting=str(get_frame_rate+'Mbps_'+str(i)+'.txt')
    makestting=makestting.lstrip()
    
    with open(makestting) as f:
        for line in f:
            new_count_1+= line.count("Starting")
    nc.append(new_count_1)
    new_count_1=1;  
    print(makestting.lstrip())
print("Number Of Runs:")
print(nc)

