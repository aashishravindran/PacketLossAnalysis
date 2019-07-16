#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:06:11 2019

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

    dsf[str('avg'+str(frame_rate))]=dsf.loc[:, dsf.columns != 'Frame_no'].mean(axis=1).apply(np.floor)
    dsf[str('median'+str(frame_rate))]=dsf.loc[:, dsf.columns != 'Frame_no'].median(axis=1).apply(np.floor)
    dsf[str('min'+str(frame_rate))]=dsf.loc[:, dsf.columns != 'Frame_no'].min(axis=1).apply(np.floor)
    dsf[str('max'+str(frame_rate))]=dsf.loc[:, dsf.columns != 'Frame_no'].max(axis=1).apply(np.floor)
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


res=fe.merge(ft, on='Frame_no', how='left')


km = res[['Frame_no','avg'+str(frame1)]].values



kmeans = KMeans(n_clusters=3)
kmeans.fit(km)

labels = kmeans.predict(km)
centroids = kmeans.cluster_centers_


final_dataf=pd.DataFrame
res['labels']=labels

fig,ax1=plt.subplots(nrows =1, ncols = 2, sharex=False, sharey = False)

ax1[0].scatter(km[labels==0,0],km[labels==0,1],  c = 'red', label = 'Cluster 1')
ax1[0].scatter(km[labels == 1, 0], km[labels == 1, 1],  c = 'blue', label = 'Cluster 2')
ax1[0].scatter(km[labels == 2, 0], km[labels == 2, 1],  c = 'green', label = 'Cluster 3')
ax1[0].set_xlabel(frame1)



km = res[['Frame_no','avg'+str(frame2)]].values


kmeans = KMeans(n_clusters=3)
kmeans.fit(km)

labels = kmeans.predict(km)
centroids = kmeans.cluster_centers_

ax1[1].scatter(km[labels==0,0],km[labels==0,1],  c = 'red', label = 'Cluster 1')
ax1[1].scatter(km[labels == 1, 0], km[labels == 1, 1],  c = 'blue', label = 'Cluster 2')
ax1[1].scatter(km[labels == 2, 0], km[labels == 2, 1],  c = 'green', label = 'Cluster 3')
ax1[1].set_xlabel(frame2)






#arr.append(km[labels==0,0])
#arr.append(km[labels==1,0])
#arr.append(km[labels==2,0])
#print(len(arr))
#for i in km[labels==0,0]:
#    arr.append(i)
#for i in km[labels==1,0]:
#    arr.append(i)
#for i in km[labels==2,0]:
#    arr.append(i)
#
#res['c0']=arr

#corr = res.corr()
#pdist = sch.distance.pdist(corr)
#linkage = sch.linkage(pdist, method='complete')
#idx = sch.fcluster(linkage, 0.5 * pdist.max(), 'distance') 
#
##Calculate the correlation of the above variables
#sns.heatmap(corr, square = True) #Plot the correlation as heat map


#plt.scatter(test['Frame_no'],labels,  c = 'red', label = 'Cluster 1')
#plt.scatter(km[labels==0,0],km[labels==0,1],  c = 'red', label = 'Cluster 1')
#plt.scatter(km[labels == 1, 0], km[labels == 1, 1],  c = 'blue', label = 'Cluster 2')
#plt.scatter(km[labels == 2, 0], km[labels == 2, 1],  c = 'green', label = 'Cluster 3')
#ax1[2][0].scatter(km[labels == 3, 0], km[labels == 3, 1], s = 100, c = 'magenta', label = 'Cluster 4')
#
#ax1[2][0].scatter(km[labels == 4, 0], km[labels == 4, 1], s = 100, c = 'cyan', label = 'Cluster 5')
plt.show()