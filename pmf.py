# -*- coding: utf-8 -
"""
Created on Sun Jul 21 21:10:17 2019

@author: Aashish Ravindran
"""

#8,9,10,11,12,13,14,16
import pandas as pd 
from get_count import get_count
import matplotlib.pyplot as plt
import numpy as np



#frame2=54
#arr=[8,9,10,11,12,13,14,16]

def file_read(file):
    line=file.readlines()
    count=0;
    dict={}
    seqNo=[]
    for i in range(0,len(line)):
        if "Starting" in line[i]:
            dict[count]=seqNo
            seqNo=[]
            count+=1
        else:
            val=int((line[i].split('and')[0]).split('=')[1])
            seqNo.append(val)
    return dict
        
    
    
def get_frame_value(run):  
    x_axsi=[]
    bm=[]
    val={}
    for i in range(0,500):
        if i not in run:
            bm.append('N')
            val[i]='N'
            x_axsi.append(i)
            
        else:
            bm.append('Y')
            val[i]='Y'
            x_axsi.append(i)
    
         
    
    return [x_axsi,bm,val]


def probabilty_mass_function(run):
    count=0
    total=0
    dict={}
    for key,value in run.items():
        if value == 'N':
            count+=1;
            total+=1
        if (value == 'Y' and count>1) or (key == 499 and count >1):
            dict[key]=count/total;
            count=0;
            total=0
        else: 
            total+=1
    return dict;


#
#fig,ax=plt.subplots(nrows=2,ncols=1,sharex=False,sharey=True,squeeze=False)
def consolidated_run(recv):
    run={}
    for i in range(0,len(recv)):
        test=get_frame_value(recv[i])[2]         
        d=probabilty_mass_function(test)
#       t=probabilty(d,1)   
        run[i]=(sum(d.values())/float(len(d)))
        
    
    result=run
   
    return result  

### 3-Losses across all nodes 
## 2- losses across three nodes 
## 1- losses across two nodes

def loss_Aggr_file_read(file,count):
    line=file.readlines() 
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
    Tw_Recv=[5,6,7,9,10,11]
    Three_Recv=[12,13,14,15]
    for i, rows in x.iterrows():
        sum=0
        #print(rows,i)
        c=rows.value_counts()
#        print(c)
#        break
#        print(c)                    
        if 16 in c:
           dsf.loc[i,'WorseCase']=c[16]
        if 1 in c:
               dsf.loc[i,'BestCase']=c[1]
         
        for k in range(0,len(Tw_Recv)):
            if Tw_Recv[k] in c:
#                print(c[Tw_Recv[k]])
                sum+=c[Tw_Recv[k]]
        dsf.loc[i,'Two_Recv']=sum
        sum=0
       
        for k in range(0,len(Three_Recv)):
            if Three_Recv[k] in c:
#                print(c[Tw_Recv[k]])
                sum+=c[Three_Recv[k]]
        dsf.loc[i,'Three_Recv']=sum
        sum=0
        
    X=dsf
    return X


### Two Recv 5,6,7,9,10,11
### Three recv -12,13,1,4,1,15    
def recv_combination_loss(datafra,combination,count):
    if combination == 4:
        #s=datafra['WorseCase'].sum()
        datafra['Pmf_worse_case']=(datafra['WorseCase']/count)*100
        return datafra['Pmf_worse_case']
        ## Add Logic here 
    elif combination == 2 :
       #s=datafra['Two_Recv'].sum()
       datafra['Pmf_Two_Recv']=(datafra['Two_Recv']/count)*100
       return datafra['Pmf_Two_Recv']
       print('Dumb') 
        ## Add Logic here 
    elif combination == 3 :
       # s=datafra['Three_Recv'].sum()
        datafra['Pmf_Three_Recv']=(datafra['Three_Recv']/count)*100
        return datafra['Pmf_Three_Recv']
        print('Dumb')
        # Add Logic here 
    
    



#
#frame1=24
##interval=1
##
#name=open("files/"+str(frame1)+"Mbps"+"Data_Aggregation_Logs.txt","r")
#
#
#count=get_count(str(frame1))
#count=count[0]
#ret=loss_Aggr_file_read(name,count)
#
#
#result=recv_combination_loss(ret,2,count)
#r=result.mean(axis=0)
#med=result.median(axis=0)
#min=result.min(axis=0)
#max=result.max(axis=0)
#print(r,med,min,max)
##x,y=zip(*(result.items()))
##plt.bar(x,y,color='blue',label='2 Recv')
##plt.xlim([50,60])
##plt.xlabel('Frame No')
##plt.ylabel('% of times the frame was lost across 3 Recv')
#
#
#    
#rettt=recv_combination_loss(ret,3,count)
#r=rettt.mean(axis=0)
#med=rettt.median(axis=0)
#min=rettt.min(axis=0)
#max=rettt.max(axis=0)
#print(r,med,min,max)
#x,y=zip(*(rettt.items()))
#
#plt.bar(x,y)
#plt.xlabel('Frame No')
#plt.ylabel('% of times the frame was lost across 3 Recv')
#
##ret=loss_Aggr_file_read(name,count)     
#ws=recv_combination_loss(ret,4,count)
#x,y=zip(*(ws.items()))
#r=ws.mean(axis=0)
#med=ws.median(axis=0)
#min=ws.min(axis=0)
#max=ws.max(axis=0)
#print(r,med,min,max)
#plt.bar(x,y,color='orange',label='4 Recv')
#plt.xlabel('Frame No')
#plt.ylabel('% of time frame loss across Recv Combo')
#plt.xlim([0,50])
#plt.legend()
#plt.show()
##
#        
#    
#    
#    
#               
#               

#frame1=24
#name= open("files/"+str(frame1)+"Mbps"+"_1.txt")
#recv_1=file_read(name)
#ret=consolidated_run(recv_1)
#    
#    



#loss_burst_len=2
#loss_len=[]
#value=0
#max_len=0;
#string=""
#bm=['Y','Y','N','N','N','Y','Y','N','Y','N','N','N']
#for i in range(0,len(bm)):
#      if 'N'== bm[i]:
#            string+=bm[i]
#            print(string)
#            if len(string)>loss_burst_len:
#                max_len=len(string)
#                loss_len.append(max_len)
#      if 'Y' == bm[i]:
#            loss_burst_len=2
#            max_len=0
#            loss_len.append(0)
#            string=""
#            
#print(loss_len)            
            
#
#i=0;
#j=0;
#count=20
#length=len(dict)
#
#for i in range(0,length):
#    plt.bar(get_lb(dict[i])[0],get_lb(dict[i])[1])
#    plt.savefig('img/Node_1_Run_no'+str(i)+'.png')
#    plt.clf()





#
#while i < 2 and count<length:
#        
#    while j < 1 and count<length:
#            ax[i][j].bar(get_lb(dict[count])[0],get_lb(dict[count])[1])
#            ax[i][j].set_title('Run_no'+str(count))
#            j+=1
#            count+=1
#    i+=1
#    j=0
#
#fig.suptitle("'Loss Burst Vs Interval for The run 20 and 21 runs Node 1'", fontsize=16)


##==================Stattistical Implementation Starts Here =================
#
#x=get_lb(dict[0])[2]
#c=0
#d={}
#for key,value in x.items():
#    print(key,value)
#    if value =='N':
#        c+=1
#        if key%50 == 0:
#            d[key]=c;
#            c=0;
# 
#x_axis_new=[] 
#y_axis_new=[]      

#plt.bar(x_axis_new,y_axis_new)
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



##========================================Pmf for All Runs per receiver==================##     
#for i in range(0,len(recv_1)):
#    loss_burst=get_frame_value(recv_1[i])[2]
#    probability=probabilty_mass_function(loss_burst)
##    probability=probabilty(aggr_frame_loss,interval)
#    lists=probability.items()
#    x, y = zip(*lists)
#    plt.bar(x,y)
#    plt.xlabel('Interval', fontsize=18)
#    plt.ylabel('PMF of Lost Frames', fontsize=16)
#    plt.title('Node1:PMF_of_lost_frames_for_Run_No'+str(i))
#    plt.savefig('img/Node_1/PMF_of_lost_frames_for_Run_N0'+str(i)+'.png')
#    plt.clf()
#for i in range(0,len(recv_2)):
#    loss_burst=get_frame_value(recv_2[i])[2]
#    probability=probabilty_mass_function(loss_burst)
#    lists=probability.items()
#    x, y = zip(*lists)
#    plt.bar(x,y)
#    plt.xlabel('Interval', fontsize=18)
#    plt.ylabel('PMF of Lost Frames', fontsize=16)
#    plt.title('Node2:PMF_of_lost_frames_for_Run_No'+str(i))
#    plt.savefig('img/Node_2/PMF_of_lost_frames_for_Run_N0'+str(i)+'.png')
#    plt.clf()
#for i in range(0,len(recv_3)):
#    loss_burst=get_frame_value(recv_3[i])[2]
#    probability=probabilty_mass_function(loss_burst)
#    lists=probability.items()
#    x, y = zip(*lists)
#    plt.bar(x,y)
#    plt.xlabel('Interval', fontsize=18)
#    plt.ylabel('PMF of Lost Frames', fontsize=16)
#    plt.title('Node3:PMF_of_lost_frames_for_Run_No'+str(i))
#    plt.savefig('img/Node_3/PMF_of_lost_frames_for_Run_N0'+str(i)+'.png')
#    plt.clf()
#for i in range(0,len(recv_4)):
#    loss_burst=get_frame_value(recv_4[i])[2]
#    probability=probabilty_mass_function(loss_burst)
#    lists=probability.items()
#    x, y = zip(*lists)
#    plt.bar(x,y)
#    plt.xlabel('Interval', fontsize=18)
#    plt.ylabel('PMF of Lost Frames', fontsize=16)
#    plt.title('Node3:PMF_of_lost_frames_for_Run_No'+str(i))
#    plt.savefig('img/Node_4/PMF_of_lost_frames_for_Run_N0'+str(i)+'.png')
#    plt.clf()
##========================================Get Consolidate Runs=============
