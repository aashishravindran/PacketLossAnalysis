#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:09:03 2019

@author: ashubunutu
"""
import pandas as pd ;
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
import seaborn as sns; sns.set()
import numpy as np
from get_count import get_count
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
import matplotlib.cm as cm
from sklearn.datasets.samples_generator import make_blobs
from sklearn import metrics
from collections import Counter
from random import randint
  
import plotly.graph_objects as go

import plotly.express as px


def get_data_fram(line,count,frame_rate):
    lits={}
    dict={}
    get_val=0;

    

    for i in range(0,len(line)):

        if "Run No" in line[i]:
            new_str=int(line[i].split("Run No========")[1])
            get_val=i+1;
            while 'Run No' not in line[get_val] and get_val+1 <len(line):
                get_line=line[get_val].split(",")
                frame_no=int(get_line[0].split(":")[1])
                loss_aggr_val=int(get_line[1].split(":")[1])
                get_val+=1
                lits[frame_no]=loss_aggr_val

            dict[new_str]=lits
            lits={}
    dsf=pd.DataFrame(dict)
    dsf['Frame_no']=dsf.index



    for i in range(1,count):
         #print(i)
         s=str("Run_no"+str(i))
         dsf[s]=dsf[i]
         dsf.drop(columns =[i], inplace = True)
   
    x=dsf.iloc[:,1:count]
    
    for i, rows in x.iterrows():
        #print(rows,i)
        c=rows.value_counts()
        if 16 in c:
           dsf.loc[i,'WorseCase']=c[16]
        if 1 in c:
               dsf.loc[i,'BestCase']=c[1]
    

#    dsf[str('avg'+str(frame_rate))]=dsf.loc[:, dsf.columns != 'Frame_no'].mean(axis=1).apply(np.floor)
#    dsf[str('median'+str(frame_rate))]=dsf.loc[:, dsf.columns != 'Frame_no'].median(axis=1).apply(np.floor)
#    dsf[str('min'+str(frame_rate))]=dsf.loc[:, dsf.columns != 'Frame_no'].min(axis=1).apply(np.floor)
#    dsf[str('max'+str(frame_rate))]=dsf.loc[:, dsf.columns != 'Frame_no'].max(axis=1).apply(np.floor)
    X=dsf
    return X






frame1=24
frame2=54


file =open("files/"+str(frame1)+"MbpsData_Aggregation_Logs.txt","r")
fp=open("files/"+str(frame2)+"MbpsData_Aggregation_Logs.txt","r")

line=file.readlines()
ls=fp.readlines()
t=[]
t.append(line.pop(0))
t.append(ls.pop(0))


count=get_count(str(frame1))
count=count[0]
fe=get_data_fram(line,count,frame1)

count=get_count(str(frame2))
count=count[0]
ft=get_data_fram(ls,count,frame2)


##Implemetation Of DBSCAN
fig,ax=plt.subplots(nrows=2,ncols=1,sharex=False,sharey=False,squeeze=False)
res=fe
x=res.iloc[:,(res.columns!='Frame_no') &(res.columns!='BestCase')&(res.columns!='WorseCase')]
x=x.replace(np.nan,0)
model =DBSCAN(eps=30,min_samples=22).fit(x)
outliers_df=pd.DataFrame(x)
c=Counter(model.labels_)
outliers_df=outliers_df[model.labels_==0]
outliers_df['Frame_no']=outliers_df.index

#lostFrames=res[['Frame_no','BestCase','WorseCase']]
##plt.plot(lostFrames['Frame_no'],lostFrames['BestCase'],label='Frame Recv Across All receivers')
#
#plt.plot(lostFrames['Frame_no'],lostFrames['WorseCase'],label='lost Freames')
#plt.show()
#plt.legend()

#ax[0][0].scatter(outliers_df['Frame_no'].head(50),outliers_df['Run_no20'].head(50),c='green',label='Run_no20')
#ax[0][0].scatter(outliers_df['Frame_no'].head(50),outliers_df['Run_no19'].head(50),c='red',label='Run_no19')
#ax[0][0].scatter(outliers_df['Frame_no'].head(50),outliers_df['Run_no18'].head(50),c='blue',label='Run_no18')
#ax[0][0].set_xlabel('Seq No')
#ax[0][0].set_ylabel('Loss Aggregation Value')
#ax[0][0].set_title('A DBSCAN Algorithm for Identifying Outliers for '+str(frame1)+' Mbps')
#ax[0][0].legend()
#
#
fig = go.Figure()
for col in outliers_df.iloc[:,(outliers_df.columns!='Frame_no') &(outliers_df.columns!='BestCase')&(outliers_df.columns!='WorseCase')].columns:
    fig.add_trace(go.Scatter(x=outliers_df['Frame_no'], y=outliers_df[col],
                    mode='markers',
                    name=str(col)))


fig.update_layout(title='A DBSCAN Algorithm for Identifying Outliers for '+str(frame1)+' Mbps')
fig.write_html('first_figure.html', auto_open=True)

#np.random.rand(3,)

res=ft
x=res.iloc[:,res.columns!='Frame_no']
x=x.replace(np.nan,0)
model =DBSCAN(eps=30,min_samples=22).fit(x)
outliers_df=pd.DataFrame(x)
c=Counter(model.labels_)
outliers_df=outliers_df[model.labels_==0]
outliers_df['Frame_no']=outliers_df.index
val=outliers_df.iloc[:,outliers_df.columns!='Frame_no'].columns
#ax[1][0].scatter(outliers_df['Frame_no'].head(50),outliers_df['Run_no20'].head(50),c='green',label='Run_no20')
#ax[1][0].scatter(outliers_df['Frame_no'].head(50),outliers_df['Run_no19'].head(50),c='red',label='Run_no19')
#ax[1][0].scatter(outliers_df['Frame_no'].head(50),outliers_df['Run_no18'].head(50),c='blue',label='Run_no18')
#ax[1][0].legend()
##plt.scatter(outliers_df['Frame_no'],outliers_df['Run_no154'],c='blue',s=100)
#
#
#ax[1][0].set_xlabel('Seq No')
#ax[1][0].set_ylabel('Loss Aggregation Value')
#ax[1][0].set_title('A DBSCAN Algorithm for Identifying Outliers for '+str(frame1)+' Mbps')



fig1 = go.Figure()
for col in outliers_df.iloc[:,(outliers_df.columns!='Frame_no') &(outliers_df.columns!='BestCase')&(outliers_df.columns!='WorseCase')].columns:
    fig1.add_trace(go.Scatter(x=outliers_df['Frame_no'], y=outliers_df[col],
                    mode='markers',
                    name=str(col)))


fig1.update_layout(title='A DBSCAN Algorithm for Identifying Outliers for '+str(frame2)+' Mbps')
fig1.write_html('first_figure_2.html', auto_open=True)


#lostFrames=res[['Frame_no','BestCase','WorseCase']]
##plt.plot(lostFrames['Frame_no'],lostFrames['BestCase'],label='Frame Recv Across All receivers')
#
#plt.plot(lostFrames['Frame_no'],lostFrames['WorseCase'],label='lost Freames')
#plt.show()
#plt.legend()
##val={}
##t=[]
#
#
#r=res[(res['Run_no1']==6) |(res['Run_no1']==5) |(res['Run_no1']==10)|(res['Run_no1']==14)]

#fig,ax=plt.subplots(nrows=2,ncols=1,sharex=False,sharey=False,squeeze=False)
#
#
#    
#ax[0][0].scatter(outliers_df['Frame_no'],outliers_df['Run_no20'],c=np.random.rand(3,),label='Run_no5')
##plt.scatter(outliers_df['Frame_no'],outliers_df['Run_no154'],c='blue',s=100)
#
#ax[0][0].set_xlabel('Seq No')
#ax[0][0].set_ylabel('Loss Aggregation Value')
#ax[0][0].set_title('A DBSCAN Algorithm for Identifying Outliers for '+str(frame1)+' Mbps')
#ax[0][0].legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#           ncol=10, mode="expand", borderaxespad=0.)



#res=ft
#x=res.iloc[:,res.columns!='Frame_no']
#x=x.replace(np.nan,0)
#model =DBSCAN(eps=30,min_samples=22).fit(x)
#outliers_df=pd.DataFrame(x)
#c=Counter(model.labels_)
#outliers_df=outliers_df[model.labels_==0]
#outliers_df['Frame_no']=outliers_df.index
#val=outliers_df.iloc[:,outliers_df.columns!='Frame_no'].columns
#ax[1][0].scatter(outliers_df['Frame_no'],outliers_df['Run_no20'],c=np.random.rand(3,),label='Run_no5')
##plt.scatter(outliers_df['Frame_no'],outliers_df['Run_no154'],c='blue',s=100)
#
#
#ax[1][0].set_xlabel('Seq No')
#ax[1][0].set_ylabel('Loss Aggregation Value')
#ax[1][0].set_title('A DBSCAN Algorithm for Identifying Outliers for '+str(frame2)+' Mbps')

#ax[1][0].legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#           ncol=10, mode="expand", borderaxespad=0.)





#plt.show()
#plt.legend(bbox_to_anchor=(1, 1),
#           bbox_transform=plt.gcf().transFigure)
#plt.xlabel('Seq No')
#plt.ylabel('Loss Aggregation No')
#plt.title('A DBSCAN Algorithm for Identifying Outliers for '+str(frame1)+' Mbps')




