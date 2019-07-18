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
from sklearn.datasets.samples_generator import make_blobs
from sklearn import metrics
from collections import Counter

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
   
#    x=dsf.iloc[:,1:count]
#    
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


frame1=54
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

##res=fe.merge(ft, on='Frame_no', how='left').replace(np.nan, 0)
#
#r=res.transpose()
#
#
#data =r.corr()
#
#size = 7
#fig, ax = plt.subplots(figsize=(size, size))
#ax.matshow(data,cmap=cm.get_cmap('coolwarm'), vmin=0,vmax=1)
#
#
#ax = sns.heatmap(
#    data, 
#    vmin=-1, vmax=1, center=0,
#    cmap=sns.diverging_palette(20, 220, n=200),
#    square=True
#)
#ax.set_xticklabels(
#    ax.get_xticklabels(),
#    rotation=45,
#    horizontalalignment='right'
#);

##K mEans
res=fe


val_bc=res[['Run_no154','Run_no254']]
val_bc_1=val_bc.values
km=val_bc_1
hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
labels=hc.fit_predict(km)

#labels = kmeans.predict(km)
#centroids = kmeans.cluster_centers_
dick={}
#arr=[]
#arr.append(km[labels==0,0])
#arr.append(km[labels==1,0])
#arr.append(km[labels==2,0])
val_bc['Frame_no']=val_bc.index
brr=[]
crr=[]
drr=[]
for index,i in enumerate(labels):
    if i == 0:
        brr.append(index)
    elif i==1 :
         crr.append(index)
    elif i==2 :
        drr.append(index)

dick['0']=brr
dick['1']=crr
dick['2']=drr

    

#fig,ax1=plt.subplots(nrows =1, ncols = 2, sharex=False, sharey = False)
#plt.scatter(dick['0'],km[labels==0,0], c = 'red', label = 'Cluster 1')
#plt.scatter(dick['1'],km[labels == 1, 0],  c = 'blue', label = 'Cluster 2')
#plt.scatter(dick['2'],km[labels == 2, 0],  c = 'green', label = 'Cluster 3')
#plt.legend()


## DBSCAN Implementation Starts here 

x=res.iloc[:,res.columns!='Frame_no']
x=x.replace(np.nan,0)
model =DBSCAN(eps=30,min_samples=6).fit(x)
outliers_df=pd.DataFrame(x)
c=Counter(model.labels_)
outliers_df=outliers_df[model.labels_==-1]
outliers_df['Frame_no']=outliers_df.index


plt.scatter(outliers_df['Frame_no'],outliers_df['Run_no2054'],c='red',s=100)
plt.show()


#z=fe[['Run_no154','Run_no2054','Frame_no']]
##z=z.replace(np.nan, 0)
#X=StandardScaler().fit_transform(z)
#db = DBSCAN(eps=0.3, min_samples=3).fit(X)
#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True
#labels = db.labels_
#
#n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
#n_noise_ = list(labels).count(-1)
#
#
#unique_labels = set(labels)
#colors = [plt.cm.Spectral(each)
#          for each in np.linspace(0, 1, len(unique_labels))]
#
#
#for k, col in zip(unique_labels, colors):
#    if k == -1:
#        # Black used for noise.
#        col = [0, 0, 0, 1]
#
#    class_member_mask = (labels == k)
#
#    xy = X[class_member_mask & core_samples_mask]
#    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
#             markeredgecolor='k', markersize=14)
#
#    xy = X[class_member_mask & ~core_samples_mask]
#    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
#             markeredgecolor='k', markersize=6)
#
#plt.title('Estimated number of clusters: %d' % n_clusters_)
#plt.show()





#
#ax1[1].scatter(dick['0'],km[labels==0,1], c = 'red', label = 'Cluster 1')
#ax1[1].scatter(dick['1'],km[labels == 1, 1],  c = 'blue', label = 'Cluster 2')
#ax1[1].scatter(dick['2'],km[labels == 2, 1],  c = 'green', label = 'Cluster 3')


#ax1[0].set_xlabel('BestCase 48')
#ax1[0].set_ylabel('Best Case 65')


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



