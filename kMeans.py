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



for i in range(1,23):
         #print(i)
         s=str("Run_no"+str(i))
         dsf[s]=dsf[i]
         dsf.drop(columns =[i], inplace = True)

#df1 = df[['a','b']]
dsf['avg']=dsf.mean(axis=1)
dsf['median']=dsf.median(axis=1).apply(np.floor)
  
X=dsf[['Frame_no', 'Run_no2']].values
#
#dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
#plt.title('Dendogram')
#plt.xlabel('Run No 1')
#plt.ylabel('Euclidean Distacne')
#plt.show()




hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

##
###X[y_hc == 0, 0], X[y_hc == 0, ]
##        
plt.scatter(X[y_hc==0,0],X[y_hc==0,1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.show()
#    
#
#x=dsf['Frame_no']
#=dsf['Run_no3']
# plt.scatter(y,x)

#
# dt=pd.DataFrame({
#         'x':dsf['Frame_no'],
#         'y':dsf[dsf.columns.difference(['Frame_no'])]
#          })
#
#


