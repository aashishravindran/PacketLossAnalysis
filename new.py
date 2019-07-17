#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:58:03 2019

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
         s=str("Run_no"+str(i)+str(frame_rate))
         dsf[s]=dsf[i]
         dsf.drop(columns =[i], inplace = True)
   
    x=dsf.iloc[:,1:count]
    
#    for i, rows in x.iterrows():
#        #print(rows,i)
#        c=rows.value_counts()
#        if 16 in c:
#           dsf.loc[i,str('WorseCase'+str(frame_rate))]=c[16]
#        if 1 in c:
#               dsf.loc[i,str('BestCase'+str(frame_rate))]=c[1]
    

#    dsf[str('avg'+str(frame_rate))]=dsf.loc[:, dsf.columns != 'Frame_no'].mean(axis=1).apply(np.floor)
#    dsf[str('median'+str(frame_rate))]=dsf.loc[:, dsf.columns != 'Frame_no'].median(axis=1).apply(np.floor)
#    dsf[str('min'+str(frame_rate))]=dsf.loc[:, dsf.columns != 'Frame_no'].min(axis=1).apply(np.floor)
#    dsf[str('max'+str(frame_rate))]=dsf.loc[:, dsf.columns != 'Frame_no'].max(axis=1).apply(np.floor)
    X=dsf
    return X


frame1=48
frame2=65




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
res=fe
#res=fe.merge(ft, on='Frame_no', how='left').replace(np.nan, 0)

r=res.transpose()


data =r.corr()

size = 7
fig, ax = plt.subplots(figsize=(size, size))
ax.matshow(data,cmap=cm.get_cmap('coolwarm'), vmin=0,vmax=1)


ax = sns.heatmap(
    data, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);

###K mEans
#fig,ax1=plt.subplots(nrows =1, ncols = 2, sharex=False, sharey = False)
#
#val_bc=res[['Frame_no','BestCase48','BestCase65']].values
#km=val_bc
#kmeans = KMeans(n_clusters=3)
#kmeans.fit(km)
#
#labels = kmeans.predict(km)
#centroids = kmeans.cluster_centers_
#
#ax1[0].scatter(km[labels==0,0],km[labels==0,1], km[labels==0,2], c = 'red', label = 'Cluster 1')
#ax1[0].scatter(km[labels == 1, 0], km[labels == 1, 1],km[labels==1,1],  c = 'blue', label = 'Cluster 2')
#ax1[0].scatter(km[labels == 2, 0], km[labels == 2, 1],km[labels==2,2],  c = 'green', label = 'Cluster 3')
#ax1[0].set_xlabel('BestCase 48')
#ax1[0].set_ylabel('Best Case 65')
#
#
#val_wcc=res[['Frame_no','WorseCase48','WorseCase65']].values
#km1=val_wcc
#kmeans = KMeans(n_clusters=3)
#kmeans.fit(km1)
#
#labels = kmeans.predict(km)
#centroids = kmeans.cluster_centers_
#
#ax1[1].scatter(km1[labels==0,0],km1[labels==0,1], km1[labels==0,2], c = 'red', label = 'Cluster 1')
#ax1[1].scatter(km1[labels == 1, 0], km1[labels == 1, 1], km1[labels==1,2], c = 'blue', label = 'Cluster 2')
#ax1[1].scatter(km1[labels == 2, 0], km1[labels == 2, 1], km1[labels==2,2], c = 'green', label = 'Cluster 3')
#ax1[1].set_xlabel('Worse Case 48')
#ax1[1].set_ylabel('Worse Case 65')
#
#
#plt.show()



