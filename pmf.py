# -*- coding: utf-8 -
"""
Created on Sun Jul 21 21:10:17 2019

@author: Aashish Ravindran
"""
import pandas as pd 
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
data= format_data('files/24Mbps_1.txt')
for i,rows in data.iterrows():
    
    if rows['count'] not in "New Run":
        data.loc[i,'loss']=(499-(int(rows['count'].split('=')[1])))/499
        #int(rows['count'].split('=')[1])
    