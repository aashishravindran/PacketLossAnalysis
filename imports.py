#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:52:50 2019

@author: ashubunutu
"""


def reference_ts(line):
    reference_timestamps=[];
    for i in range(0,len(line)):
    #print(i,line[i])
        if i==0:
           reference_timestamps.append(float(line[i].split(',@')[1])) #Get all time Stamps from the reference file
        elif "Starting" in line[i]:
            i+=1; #skip the line with "Starting new line"
            reference_timestamps.append(float(line[i].split(',@')[1]))
    return reference_timestamps
       
   
 
def compute_time_sync(reference_timestamps,new_file,dest_pt):
     test=open(dest_pt,"w")
     
     ref_index=0;
     #k=0;
     j=0;
     length=int(len(new_file)) #Get length of New_file
     print(length)

     while j < length:
                        
              if j==0:
                  #print("I came Here")
                  #Time Sync Calcualtion Starts here
                  new_val=new_file[0].split(",@") #Split to get the time Stamp
                  count=float("{0:.3f}".format(float(new_val[1])-reference_timestamps[ref_index]))
                  sync_count=float("{0:.3f}".format(float(new_val[1])-count))
                  fin_out=str(new_val[0])+", @"+str(sync_count)
                  test.write(fin_out+"\n")
                       
              elif (new_file[j].strip() =="=================Starting New Run========="):
                          
                          j+=1;
                          ref_index+=1
                          new_val=new_file[j].split(",@")
                          count=float("{0:.3f}".format(float(new_val[1])-reference_timestamps[ref_index]))
                          sync_count=float("{0:.3f}".format(float(new_val[1])-count))
                          fin_out=str(new_val[0])+", @"+str(sync_count)
                          test.write("=========================Starting New Run==================\n")
                          test.write(fin_out+"\n")
                          print(fin_out)
                          
                          
                          
              else:
                          #Calculating for other frames from the second frame to "Starting new Run"
                          new_val_1=new_file[j].split(",@")
                          final_count=float("{0:.3f}".format(float(new_val_1[1])-sync_count))
                          T_count=float("{0:.3f}".format(float(new_val_1[1])+final_count))
                          fin_out_1=str(new_val_1[0])+", @"+str(T_count)
                          test.write(fin_out_1+"\n")
                          print("s"+fin_out_1+","+str(j))

              j+=1 
              
     test.close() #Close the file
     return 0;




         
        
     
         



        
