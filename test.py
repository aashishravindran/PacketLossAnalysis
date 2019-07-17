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
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


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

x=fe.iloc[:,1:23]
y=fe.iloc[:,0]

for i, rows in x.iterrows():
    print(rows,i)
    c=rows.value_counts()
    if 16 in c:
        x.loc[i,'WorseCase']=c[16]
    if 1 in c:
        x.loc[i,'BestCase']=c[1]
   

#z=x['WorseCase'].values
#z=z[~np.isnan(z)]
plt.scatter(y,x['WorseCase'],x['BestCase'])
plt.show()
fe['WorseCase'] = x['WorseCase'].replace(np.nan, 0)
fe['BestCase'] = x['BestCase'].replace(np.nan, 0)
kmeans1=fe[['Frame_no','BestCase','WorseCase']].values
kmeans = KMeans(n_clusters=2)
kmeans.fit(kmeans1)

labels = kmeans.predict(kmeans1)
centroids = kmeans.cluster_centers_


plt.scatter(kmeans1[labels==0,0],kmeans1[labels==0,1],kmeans1[labels==0,2],  c = 'red', label = 'Cluster 1')
plt.scatter(kmeans1[labels == 1, 0], kmeans1[labels == 1, 1], kmeans1[labels==1,2], c = 'blue', label = 'Cluster 2')
plt.scatter(kmeans1[labels == 2, 0], kmeans1[labels == 2, 1], kmeans1[labels==2,2],c = 'green', label = 'Cluster 3')
plt.show()




#count=0
#dict={}

#        
        
#x = StandardScaler().fit_transform(x)
#z=x[~np.isnan(x).any(axis=1)]
#pca = PCA(n_components=2)
#principalComponents = pca.fit_transform(z)
#principalDf = pd.DataFrame(data = principalComponents
#             , columns = ['principal component 1', 'principal component 2'])
#
#finalDf = pd.concat([principalDf, y], axis = 1)
#
#fig = plt.figure(figsize = (8,8))
#ax = fig.add_subplot(1,1,1) 
#ax.set_xlabel('Principal Component 1', fontsize = 15)
#ax.set_ylabel('Principal Component 2', fontsize = 15)
#ax.set_title('2 component PCA', fontsize = 20)
#targets = 
#colors = ['r', 'g', 'b']
#for target, color in zip(targets,colors):
#    indicesToKeep = finalDf['Frame_no'] == target
#    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
#               , finalDf.loc[indicesToKeep, 'principal component 2']
#               , c = color
#               , s = 50)
#ax.legend(targets)
#ax.grid()
#
#plt.show()


count=get_count(str(frame2))
count=count[0]
ft=get_data_fram(ls,count,frame2)


res=fe.merge(ft, on='Frame_no', how='left')


km = res[['Frame_no','Run_no1'+str(frame1)]].values



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



km = res[['Frame_no','Run_no1'+str(frame2)]].values


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