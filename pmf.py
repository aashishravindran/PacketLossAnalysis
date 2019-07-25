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
            bm.append('Y')
            val[i]='Y'
            x_axsi.append(i)
            
        else:
            bm.append('N')
            val[i]='N'
            x_axsi.append(i)
    
         
    
    return [x_axsi,bm,val]



def identify_loss_burst_intervals(run):
    count=0
    dict={}
    for key,value in run.items():
        if value == 'N':
            count+=1;
        if (value == 'Y' and count>1):
            dict[key]=count;
            count=0;
    return dict;


#def get_agg_frame_loss(x,interval):
#    
#   
#    fina_dict={}
#    d={}
#    c=0
#    for key,value in x.items():
##        print(key,value)
#        if value =='N':
#            d[key]=value
#            c+=1
#        if (key%interval == 0 or key == 499) and key !=0:
#            fina_dict[key]=c;
#            c=0
#        else:
#             d[key]=value
#    
#    return fina_dict


def probabilty(y,interval):
    prob={}
    sumval=0
    i=0
    for key,value in y.items(): 
        sumval+=value
        i+=1
        if i == interval :
            prob[key]=sumval/500
            sumval=0
            i=0
     
    return prob
  
#
#fig,ax=plt.subplots(nrows=2,ncols=1,sharex=False,sharey=True,squeeze=False)
def consolidated_run(recv):
    run={}
    for i in range(0,len(recv)):
        test=get_frame_value(recv[i])[2]         
        d=identify_loss_burst_intervals(test)
        t=probabilty(d,1)   
        run[i]=(sum(t.values())/float(len(t)))
        
    
    result=run
#    res=pd.DataFrame(result)
#    res['Interval']=result.index
#    result['0']=result['pmf']
    
#    result['pmf_sum']=result.loc[:, result.columns != 'Interval'].sum(axis=1)
#    result['pmf']=result['pmf_sum']/(len(run)*500)
    
    return result  
#
#def get_loss_burst_len(run):
#    count=0
#    dict={}
#    for key,value in run.items():
#        if value == 'N':
#            count+=1;
#        if value =='Y' and count>1:
#            dict[key]=count;
#            count=0;
#    return dict;
#
#
#frame1=24
#name= open("files/"+str(frame1)+"Mbps"+"_1.txt")
#recv_1=file_read(name)
#ret=consolidated_run(recv_1)
#
#
#lists=ret.items()
#x, y = zip(*lists)
#plt.bar(x,y)


    
    
               
               


     
   
    
        
        



            
               
                    
                    
                
                
                
                
                
            
    
    
    



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

