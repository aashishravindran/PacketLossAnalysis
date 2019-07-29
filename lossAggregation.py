#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:00:26 2019

@author: ashubunutu
"""

import pandas as pd;
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
#=============================================================Init======================
frame_rate=str(input("Please Enter The Frame rate:"))
count=get_count(frame_rate)
count=count[0]


name= (str("files/"+frame_rate+"Mbps"+"_1.txt")).lstrip()#'48Mbps_1.txt'
name_1=(str("files/"+frame_rate+"Mbps"+"_2.txt")).lstrip()
name_2=(str("files/"+frame_rate+"Mbps"+"_3.txt")).lstrip()
name_3=(str("files/"+frame_rate+"Mbps"+"_3.txt")).lstrip()

rec_1=format_data(name)
recv_2=format_data(name_1)
recv_3=format_data(name_2)
recv_4=format_data(name_3)


dict={}
dict2={}
dict3={}
dict4={}

i=1;
nc1=[];
nc2=[];
nc3=[];
nc4=[];

#==========Iterate through all the rows of across all text files and obtain sequence Numbers in an Array==================
for index,row in rec_1.iterrows():
     if row['seq']=="New Run":
         dict[i]=nc1; #For each run append Number Of runs and Sequence Number
         nc1=[];
         i+=1
     else:
         new= row['seq'].split('=') #Gets Sequence Number 
         nc1.append(int(new[1]))

i=1;       
for index,row in recv_2.iterrows(): #iterating all the rows for the second receiver
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
#========================================================Loss Aggregation Starts Here================         
loss_Aggregation={}
#numRuns=len(dict)+1
for k,j in  enumerate(dict):
    fin1=dict[j]
    fin2=dict2[j]
    fin3=dict3[j]
    fin4=dict4[j]
    #print(fin4[0],fin3[0],fin2[0],fin1[0])
    run=[]
    for i in range(0,500):
           #================================Append appropriate values based on the condition==========================       
            if  (i in fin1 and i  in fin2  and i  in fin3 and i  in fin4):
                run.append(1)
            elif  (i in fin1 and i  in fin2  and i  in fin3 and i  not in fin4):
                run.append(2)
            elif  (i in fin1 and i  in fin2  and i  not in fin3 and i  in fin4):
                run.append(3)
            elif  (i in fin1 and i not in fin2  and i  in fin3 and i  in fin4):
                run.append(4)
            elif  (i in fin1 and i  in fin2  and i not in fin3 and i  not in fin4):
                run.append(5)
            elif  (i in fin1 and i not in fin2  and i  in fin3 and i  not in fin4):
                run.append(6)
            elif  (i in fin1 and i  not in fin2  and i not in fin3 and i  in fin4):
                run.append(7)
            elif  (i not in fin1 and i  in fin2  and i  in fin3 and i  in fin4):
                 run.append(8)
            elif  (i not in fin1 and i  in fin2  and i  not in fin3 and i  in fin4):
                 run.append(9)
            elif  (i not in fin1 and i  in fin2  and i  in fin3 and i  not in fin4):
                 run.append(10)
            elif  (i not in fin1 and i  not in fin2  and i  in fin3 and i  in fin4):
                 run.append(11)
            elif  (i not in fin1 and i  not in fin2  and i  in fin3 and i  not in fin4):
                 run.append(12)
            elif  (i not in fin1 and i  not in fin2  and i  not in fin3 and i  in fin4):
                 run.append(13)
            elif  (i not in fin1 and i  in fin2  and i  not in fin3 and i  not in fin4):
                 run.append(14)
            elif  (i in fin1 and i not in fin2  and i  not in fin3 and i  not in fin4):
                run.append(15)
            elif  (i not in fin1 and i  not in fin2  and i  not in fin3 and i  not in fin4):
                run.append(16)
            
            
    loss_Aggregation[j]=run; #Assign the array to the Hash Map
    
print(loss_Aggregation)
file=open("files/"+frame_rate+"Mbps"+"Data_Aggregation_Logs.txt","w")
file.write(frame_rate+"MbpsLogs\n")

for i, k in enumerate(loss_Aggregation):
    print("==============Run No========",k)
    file.write("==============Run No========"+str(k)+"\n")
    new=loss_Aggregation[k];
    for i in range(0,500):
        print("Index: "+str(i)+" Value:"+str(new[i]))
        file.write("Index:"+str(i)+","+"Value:"+str(new[i])+"\n")

file.close()
