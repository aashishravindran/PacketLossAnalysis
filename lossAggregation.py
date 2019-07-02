#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:00:26 2019

@author: ashubunutu
"""

import pandas as pd;
import numpy as np;
from get_count import get_count
 
def format_data(data_name):
     
     df=pd.read_csv(data_name,header=None,names=['val'])
 
    # print(df['val'])
 
     new= df['val'].str.split("and",n=1,expand=True)
     #print(new[0])
     df['seq']=new[0]
     df['count']=new[1]
 
     nr=df[df['val']=="=================Starting New Run========="].index
     #print(nr)
     df.loc[nr,'New_Run']="New Run"
 
    
     df.drop(columns =["val"], inplace = True) 
     df[df['seq']=="=================Starting New Run========="]="New Run"
 

 
     return df;

frame_rate=str(input("Please Enter The Frame rate:"))
count=get_count(frame_rate)
count=count[0]

name='48Mbps_1.txt'
name_1='48Mbps_2.txt'
name_2='48Mbps_3.txt'
name_3='48Mbps_4.txt'

rec_1=format_data(name)
recv_2=format_data(name_1)
recv_3=format_data(name_2)
recv_4=format_data(name_3)


rec_1.set_index('seq')
dict={}
dict2={}
dict3={}
dict4={}



i=1;
nc1=[];
nc2=[];
nc3=[];
nc4=[];
for index,row in rec_1.iterrows():
     if row['seq']=="New Run":
         dict[i]=nc1;
         nc1=[];
         i+=1
     else:
         new= row['seq'].split('=')
         nc1.append(int(new[1]))

i=1;       
for index,row in recv_2.iterrows():
     if row['seq']=="New Run":
         dict2[i]=nc2;
         nc2=[];
         i+=1
     else:
         new= row['seq'].split('=')
         nc2.append(int(new[1]))

i=1;
for index,row in recv_3.iterrows():
     if row['seq']=="New Run":
         dict3[i]=nc3;
         nc3=[];
         i+=1
     else:
         new= row['seq'].split('=')
         nc3.append(int(new[1]))
i=1;
for index,row in recv_4.iterrows():
     if row['seq']=="New Run":
         dict4[i]=nc4;
         nc4=[];
         i+=1
     else:
         new= row['seq'].split('=')
         nc4.append(int(new[1]))
         
loss_Aggregation={}
numRuns=len(dict)+1
for j in range(1,numRuns):
    fin1=dict[j]
    fin2=dict2[j]
    fin3=dict3[j]
    fin4=dict4[j]
    print(fin4[0],fin3[0],fin2[0],fin1[0])
    final_run=[]
    for i in range(0,500):
                  
            if  (i in fin1 and i not in fin2  and i not in fin3 and i not in fin4):
                final_run.append(1)
            elif (i not in fin1 and i in fin2  and i not in fin3 and i not in fin4):
                final_run.append(2)
            elif (i not in fin1 and i not in fin2  and i in fin3 and i not in fin4):
                final_run.append(3)
            elif (i not in fin1 and i not in fin2  and i not in fin3 and i in fin4):
                final_run.append(4)
            elif (i in fin1 and i  in fin2  and i not in fin3 and i not in fin4):
                final_run.append(5)
            elif (i in fin1 and i not in fin2  and i  in fin3 and i not in fin4):
                final_run.append(6)
            elif (i in fin1 and i not in fin2  and i not in fin3 and i in fin4):
                final_run.append(7)
            elif (i not in fin1 and i  in fin2  and i in fin3 and i not in fin4):
                 final_run.append(8)
            elif (i not in fin1 and i in fin2  and i not in fin3 and i  in fin4):
                 final_run.append(9)
            elif (i not in fin1 and i not in fin2  and i  in fin3 and i in fin4):
                 final_run.append(10)
            elif (i in fin1 and i not in fin2  and i not in fin3 and i not in fin4):
                 final_run.append(11)
            elif (i in fin1 and i  in fin2  and i  not in fin3 and i  in fin4):
                 final_run.append(12)
            elif (i in fin1 and i not in fin2  and i  in fin3 and i  in fin4):
                 final_run.append(13)
            elif (i in fin1 and i  in fin2  and i  in fin3 and i  in fin4):
                 final_run.append(14)
            else:
                final_run.append(0)
       
            
            
    loss_Aggregation[j]=final_run;
    
#print(loss_Aggregation)
file=open("Final_logs.txt","w")

for i, k in enumerate(loss_Aggregation):
    print("==============Run No========",k)
    file.write("==============Run No========"+str(k)+"\n")
    new=loss_Aggregation[k];
    for i in range(0,500):
        print("Index: "+str(i)+" Value:"+str(new[i]))
        file.write("Index: "+str(i)+" Value:"+str(new[i])+"\n")
    
    
    
        
            
            
        
            
        
    


         




     
            
# =============================================================================
# while df['seq'][i] not in "New Run":
#     
#     new_str='seq'+'='+str(i)
#     #new_str=new_str.lstrip()
#     #print(new_str,i)
#    # nc.append(df[df['seq']!=new_str])
#     if new_str in df['seq'][i]:
#         print("F")
#     else :
#         print("N"+new_str)
#     i+=1;
    
    
    # if(row['seq']=="New Run"):
     #       dict[i]=nc1;
      #      nc1=[];
       #     i+=1;  
            
   # new=row['seq'].split('=')
    #nc1.append(int(new[1]))
# =============================================================================


    
    #print(df['seq'][i])
    
#    df[df['seq'].str.match(new_str)]
#    if df['seq']==
#    


#new_run=df['val'].str.split("=================Starting New Run=========",n=2,expand=True)
#df['NewRun']=new_run[0]