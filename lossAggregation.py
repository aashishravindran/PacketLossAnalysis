#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:00:26 2019

@author: ashubunutu
"""
# =============================================================================
# 
# import pandas as pd;
# import numpy as np;
# 
# 
# df=pd.read_csv('48Mbps_1.txt',header=None,names=['val'])
# 
# print(df['val'])
# 
# new= df['val'].str.split("and",n=1,expand=True)
# print(new[0])
# df['seq']=new[0]
# df['count']=new[1]
# 
# nr=df[df['val']=="=================Starting New Run========="].index
# print(nr)
# df.loc[nr,'New_Run']="New Run"
# 
# dict={}
# df.drop(columns =["val"], inplace = True) 
# df[df['seq']=="=================Starting New Run========="]="New Run"
# 
# nc1=[];
# 
# 
# df.set_index('seq')
# i=0;
# for index,row in df.iterrows():
#     if row['seq']=="New Run":
#         dict[i]=nc1;
#         nc1=[];
#         i+=1
#     else:
#         new= row['seq'].split('=')
#         nc1.append(int(new[1]))
# 
# =============================================================================


     
            
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