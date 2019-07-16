#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:10:10 2019

@author: ashubunutu
"""

import pandas as pd ;
import math
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
import seaborn as sns; sns.set()
import numpy as np

# =============================================================================
# df= pd.read_csv("Data_Aggregation_Logs.txt",sep="\n",header=None,names=['val'])
# mod=df['val'].str.split(",",n=1,expand=True)
# df['Frame_no']=mod[0]
# df['value']=mod[1]
#
# df.drop(columns =["val"], inplace = True)
#
# for row in df.iterrows():
#     print(row['Frame_no'])
#
# =============================================================================


fp =open("files/Data_Aggregation_Logs.txt","r") ## Open the File

dict={}
get_val=0;
lits={}


line=fp.readlines()
t=line[0]
line.pop(0)
#print(line)

#       break;
frame=[]
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
value=[]
run=[]
dsf=pd.DataFrame(dict)

dsf['Frame_no']=dsf.index



for i in range(1,24):
         #print(i)
         s=str("Run_no"+str(i))
         dsf[s]=dsf[i]
         dsf.drop(columns =[i], inplace = True)

#df1 = df[['a','b']]




dsf['avg']=dsf.loc[:, dsf.columns != 'Frame_no'].mean(axis=1).apply(np.floor)
dsf['median']=dsf.loc[:, dsf.columns != 'Frame_no'].median(axis=1).apply(np.floor)
dsf['min']=dsf.loc[:, dsf.columns != 'Frame_no'].min(axis=1).apply(np.floor)
dsf['max']=dsf.loc[:, dsf.columns != 'Frame_no'].max(axis=1).apply(np.floor)
  

X=dsf[['Frame_no', 'median']].values


hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

##
###X[y_hc == 0, 0], X[y_hc == 0, ]
##        


## Subplots
  
f, axes = plt.subplots(nrows =6, ncols = 3, sharex=True, sharey = True)

X=dsf[['Frame_no', 'Run_no1']].values

count=1;

for i in range(0,6):
    co=0
    while co<3:
      nre=str('Run_no'+str(count))
      print(nre)
      X=dsf[['Frame_no',nre]].values
      hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
      y_hc = hc.fit_predict(X)
      
      axes[i][co].scatter(X[y_hc==0,0],X[y_hc==0,1], s = 100, c = 'red', label = 'Cluster 1',marker = "x")
      axes[i][co].scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2',marker = "o")
      axes[i][co].scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3',marker = "*")
      
      axes[i][co].set_xlabel(nre, labelpad = 5)
      count+=1
      co+=1



fig,ax1=plt.subplots(nrows =3, ncols = 2, sharex=False, sharey = False)

X=dsf[['Frame_no','avg']].values
hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

ax1[0][0].scatter(X[y_hc==0,0],X[y_hc==0,1], s = 100, c = 'red', label = 'Cluster 1',marker = "x")
ax1[0][0].scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2',marker = "o")
ax1[0][0].scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3',marker = "*")
ax1[0][0].set_ylabel('Average')
ax1[0][0].set_xlabel('Frame_no')



X=dsf[['Frame_no','median']].values
hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

ax1[0][1].scatter(X[y_hc==0,0],X[y_hc==0,1], s = 100, c = 'red', label = 'Cluster 1',marker = "x")
ax1[0][1].scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2',marker = "o")
ax1[0][1].scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3',marker = "*")
ax1[0][1].set_ylabel('Median')
ax1[0][1].set_xlabel('Frame_no')





X=dsf[['Frame_no','min']].values
hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

ax1[1][0].scatter(X[y_hc==0,0],X[y_hc==0,1], s = 100, c = 'red', label = 'Cluster 1',marker = "x")
ax1[1][0].scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2',marker = "o")
ax1[1][0].scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3',marker = "*")
ax1[1][0].set_ylabel('Min')
ax1[1][0].set_xlabel('Frame_no')




X=dsf[['Frame_no','max']].values
hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

ax1[1][1].scatter(X[y_hc==0,0],X[y_hc==0,1], s = 100, c = 'red', label = 'Cluster 1',marker = "x")
ax1[1][1].scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2',marker = "o")
ax1[1][1].scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3',marker = "*")
ax1[1][1].set_ylabel('Max')
ax1[1][1].set_xlabel('Frame_no')




km = dsf[['Frame_no','avg']].values

kmeans = KMeans(n_clusters=3)
kmeans.fit(km)

labels = kmeans.predict(km)
centroids = kmeans.cluster_centers_




#colmap = {1: 'r', 2: 'g', 3: 'b'}
#colors = map(lambda x: colmap[x+1], labels)

ax1[2][0].scatter(km[labels==0,0],km[labels==0,1], s = 100, c = 'red', label = 'Cluster 1',marker = "x")
ax1[2][0].scatter(km[labels == 1, 0], km[labels == 1, 1], s = 100, c = 'blue', label = 'Cluster 2',marker = "o")
ax1[2][0].scatter(km[labels == 2, 0], km[labels == 2, 1], s = 100, c = 'green', label = 'Cluster 3',marker = "*")
#ax1[2][0].scatter(km[labels == 3, 0], km[labels == 3, 1], s = 100, c = 'magenta', label = 'Cluster 4')
#
#ax1[2][0].scatter(km[labels == 4, 0], km[labels == 4, 1], s = 100, c = 'cyan', label = 'Cluster 5')
ax1[2][0].set_ylabel('KMeans')
ax1[2][0].set_xlabel('Frame_no')
