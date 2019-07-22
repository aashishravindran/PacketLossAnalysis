# -*- coding: utf-8 -
"""
Created on Sun Jul 21 21:10:17 2019

@author: Aashish Ravindran
"""

#8,9,10,11,12,13,14,16
import pandas as pd 
from get_count import get_count
import matplotlib.pyplot as plt

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
#frame2=54
arr=[8,9,10,11,12,13,14,16]

fp =open("files/"+str(frame1)+"Mbps_1.txt","r")
line =fp.readlines()
seqNo=[]
dict={}
count=0
for i in range(0,len(line)):
    if "Starting" in line[i]:
         dict[count]=seqNo
         seqNo=[]
         count+=1
    else:
        val=int((line[i].split('and')[0]).split('=')[1])
        seqNo.append(val)
    
def get_lb(run):  

    x_axsi=[]
    bm=[]
    val={}
    for i in range(0,500):
        if i in run:
            bm.append('Y')
            val[i]='Y'
            
        else:
            bm.append('N')
            val[i]='N'
        x_axsi.append(i)
    
    return [x_axsi,bm,val]


       

fig,ax=plt.subplots(nrows=2,ncols=1,sharex=False,sharey=True,squeeze=False)
i=0;
j=0;
count=20
length=len(dict)
while i < 2 and count<length:
        
    while j < 1 and count<length:
            ax[i][j].bar(get_lb(dict[count])[0],get_lb(dict[count])[1])
            ax[i][j].set_title('Run_no'+str(count))
            j+=1
            count+=1
    i+=1
    j=0



fig.suptitle("'Loss Burst Vs Interval for The run 20 and 21 runs Node 1'", fontsize=16)



##==================Stattistical Implementation Starts Here =================

x=get_lb(dict[0])[2]
plt.bar(get_lb(dict[0])[0],get_lb(dict[0])[1])
c=0
d={}
for key,value in x.items():
    print(key,value)
    if value =='N':
        c+=1
        if key%50 == 0:
            d[key]=c;
            c=0;
 
x_axis_new=[] 
y_axis_new=[]      
for key,value in d.items(): 
    x_axis_new.append(key)
    y_axis_new.append(value)      

plt.bar(x_axis_new,y_axis_new)
#ax[0][0].bar(get_lb(dict[0])[0],get_lb(dict[0])[1])
#
#ax[0][1].bar(get_lb(dict[1])[0],get_lb(dict[1])[1])
#
#ax[1][0].bar(get_lb(dict[2])[0],get_lb(dict[2])[1])
#
#ax[1][1].bar(get_lb(dict[3])[0],get_lb(dict[3])[1])
    
#    
#    

    
#
#
#file =open("files/"+str(frame1)+"MbpsData_Aggregation_Logs.txt","r")
#line =file.readlines()
#count=get_count(str(frame1))
#count=count[0]
#fe=get_data_fram(line,count,frame1)
#res=fe[['Frame_no','Run_no1']]
#res=res.query('Run_no1 in [8,9,10,11,12,13,14,16]')   
#res=res['Run_no1'].values
#
#
#count=0;
#loss_burst=[]
#tets=[]
#i=0
#while i < len(res):
#   
#    curr=res[i]
#    if  i+1 <len(res):
#        next=res[i+1]
#    print(curr,next)
#    if next == curr:
#        tets=[]
#        prev=res[i]
##        prev=curr
##        tets.append(prev)
#        while i<len(res) and res[i] == prev:
#           count+=1;
#           i+=1;
#           
#            
#        loss_burst.append(count)
#        count=0
#        print(i,len(res))
#    else :
#         loss_burst.append(0)
#         i+=1
#
#interval=[]
#value=[]
#for index,val in enumerate(loss_burst):
#    interval.append(index)
#    value.append(val)
#
#plt.plot(interval,value)


#for i,j in enumerate(res):
    
#res=res.query('Run_no1 in [8,9,10,11,12,13,14,16]')   
#res=res.values
#plt.scatter(res['Frame_no'],res['Run_no1'])
#plt.show()
##
#for index,row in res.iterrows():
#    

