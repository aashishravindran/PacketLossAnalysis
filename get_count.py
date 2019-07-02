#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:07:17 2019

@author: ashubunutu
"""
get_frame_rate=input('Enter Desired Mbps Rate')
## Enter frame rate as follows  for 48Mbps please enter 48 
new_count_1=1
nc=[]
#print(new_count_1)

for i in range(1,5):
    makestting=str(get_frame_rate+'Mbps_'+str(i)+'.txt')
    makestting=makestting.lstrip()
    ## makestring is added to generate the text file to be read dynamically 
    
    try: #Adding try except block to handle "File Not found Exception"
        with open(makestting) as f: #File Open Statement
            for line in f: #Iterate through All the lines in the file and look for the Phrase Starting
                new_count_1+= line.count("Starting") #Count the number of times Starting occurs since each Starting is a new Run 
        nc.append(new_count_1) # After the entire file is read, append the count to the final array 
        new_count_1=1
    except (OSError, IOError) as e: #Any exception raised in try block will be handled here 
        print(str(e))

result = False;
if len(nc) > 0 :
    result = all(elem == nc[0] for elem in nc)
# To check if all the elements in the array are same  
if result :
    print("Number of Runs is the same")
    print("Number Of Runs:"+str(nc)) #Print array with number of runs
elif OSError or IOError :        
    print("Some error Occurred")
else:
    print("Number of Runs is the diffrent")



