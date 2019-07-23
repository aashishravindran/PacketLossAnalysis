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
        
    
    
def get_lb(run):  
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


def get_agg_frame_loss(x,interval):
    
   
    fina_dict={}
    d={}
    c=0
    for key,value in x.items():
        print(key,value)
        if value =='N':
            d[key]=value
               
            
          
    for key,value in d.items():
        c+=1
        if key%interval ==0:
            fina_dict[key]=c;
            c=0
            
    
    return fina_dict


def probabilty(y):
    prob={}
    for key,value in y.items(): 
        prob[key]=value/len(y)
    
    return prob



def get_frame_Ye_n(x,interval):
    fina_dict={}
    c=0
    nc=0
    for key,value in x.items():
        print(key,value)
        if key%interval !=0:
            if value =='N':
                nc+=1
            if value=='Y':
                c+=1
        else:
            va=[]
            va.append(nc)
            va.append(c)
            fina_dict[key]=va
            nc=0
            c=0              
    
#    for key,value in d.items():
#        c+=1
#        if key%interval ==0:
#            fina_dict[key]=c;
#            c=0       
    return fina_dict
    
#
#fig,ax=plt.subplots(nrows=2,ncols=1,sharex=False,sharey=True,squeeze=False)
    


    
    



frame1=24

name= open("files/"+str(frame1)+"Mbps"+"_1.txt")
name_1=open("files/"+str(frame1)+"Mbps"+"_2.txt")
name_2=open("files/"+str(frame1)+"Mbps"+"_3.txt")
name_3=open("files/"+str(frame1)+"Mbps"+"_4.txt")



recv_1=file_read(name)
recv_2=file_read(name_1)
recv_3=file_read(name_2)
recv_4=file_read(name_3)


def consolidated_run(recv):
    run={}
    for i in range(0,len(recv)):
        test=get_lb(recv[i])[2]         
        d=get_agg_frame_loss(test,10)
        t=probabilty(d)   
        run[i]=t
    
    result=pd.DataFrame(run)
    result['Interval']=result.index
    result['mean_pmf']=result.loc[:, result.columns != 'Interval'].mean(axis=1)
    
    return result
res1=consolidated_run(recv_1)
res2=consolidated_run(recv_2)
res3=consolidated_run(recv_3)
res4=consolidated_run(recv_4)

plt.bar(res1['Interval'],res1['mean_pmf'])
plt.xlabel('Interval', fontsize=18)
plt.ylabel('MeanPmf', fontsize=16)
plt.title('Aggregated Pmf form Node 1')
plt.savefig('img/Node_1/Aggrpmg.png')
plt.clf()           



plt.bar(res2['Interval'],res2['mean_pmf'])
plt.xlabel('Interval', fontsize=18)
plt.ylabel('MeanPmf', fontsize=16)
plt.title('Aggregated Pmf form Node 2')
plt.savefig('img/Node_2/Aggrpmg.png')
plt.clf()           



plt.bar(res3['Interval'],res3['mean_pmf'])
plt.xlabel('Interval', fontsize=18)
plt.ylabel('MeanPmf', fontsize=16)
plt.title('Aggregated Pmf form Node 3')
plt.savefig('img/Node_3/Aggrpmg.png')
plt.clf()           


plt.bar(res4['Interval'],res4['mean_pmf'])
plt.xlabel('Interval', fontsize=18)
plt.ylabel('MeanPmf', fontsize=16)
plt.title('Aggregated Pmf form Node 4')
plt.savefig('img/Node_4/Aggrpmg.png')
plt.clf()

#================== Derive Code Starts Here =========================================#


#for i in range(0,len(recv_1)):
#      plt.bar(get_lb(recv_1[i])[0],get_lb(recv_1[i])[1])
#      plt.xlabel('SeqNo', fontsize=18)
#      plt.ylabel('Frame_received/Lost', fontsize=16)
#      plt.title('img/Node_1/Run_no'+str(i))
#      plt.savefig('img/Node_1/Run_no'+str(i)+'.png')
#      plt.clf()
#
#for i in range(0,len(recv_2)):
#      plt.bar(get_lb(recv_2[i])[0],get_lb(recv_2[i])[1])
#      plt.xlabel('SeqNo', fontsize=18)
#      plt.ylabel('Frame_received/Lost', fontsize=16)
#      plt.title('img/Node_2/Run_no'+str(i))
#      plt.savefig('img/Node_2/Run_no'+str(i)+'.png')
#      plt.clf()
#
#
#for i in range(0,len(recv_3)):
#      plt.bar(get_lb(recv_3[i])[0],get_lb(recv_3[i])[1])
#      plt.xlabel('SeqNo', fontsize=18)
#      plt.ylabel('Frame_received/Lost', fontsize=16)
#      plt.title('img/Node_3/Run_no'+str(i))
#      plt.savefig('img/Node_3/Run_no'+str(i)+'.png')
#      plt.clf()
#
#
#
#for i in range(0,len(recv_4)):
#      plt.bar(get_lb(recv_4[i])[0],get_lb(recv_4[i])[1])
#      plt.xlabel('SeqNo', fontsize=18)
#      plt.ylabel('Frame_received/Lost', fontsize=16)
#      plt.title('img/Node_4/Run_no'+str(i))
#      plt.savefig('img/Node_4/Run_no'+str(i)+'.png')
#      plt.clf()



#======================== Aggregated Length Data========================#


#
#
#for i in range(0,len(recv_1)):
#    x_axis_new=[]
#    y_axis_new=[]
#    d=get_lb(recv_1[i])[2]
#    t=get_agg_frame_loss(d,10)
##
#    for key,value in t.items(): 
#        x_axis_new.append(key)
#        y_axis_new.append(value/len(t))      
#
#    plt.bar(x_axis_new,y_axis_new)
#    plt.xlabel('Interval', fontsize=18)
#    plt.ylabel('PMF of Lost Frames', fontsize=16)
#    plt.title('Node1:PMF_of_lost_frames_for_Run_No'+str(i))
#    plt.savefig('img/Node_1/PMF_of_lost_frames_for_Run_N0'+str(i)+'.png')
#    plt.clf()
#    
#
#
#for i in range(0,len(recv_2)):
#    x_axis_new=[]
#    y_axis_new=[]
#    d=get_lb(recv_2[i])[2]
#    t=get_agg_frame_loss(d,10)
##
#    for key,value in t.items(): 
#        x_axis_new.append(key)
#        y_axis_new.append(value/len(t))      
#
#    plt.bar(x_axis_new,y_axis_new)
#    plt.xlabel('Interval', fontsize=18)
#    plt.ylabel('PMF of Lost Frames', fontsize=16)
#    plt.title('Node2:PMF_of_lost_frames_for_Run_No'+str(i))
#    plt.savefig('img/Node_2/PMF_of_lost_frames_for_Run_N0'+str(i)+'.png')
#    plt.clf()
#
#for i in range(0,len(recv_3)):
#    x_axis_new=[]
#    y_axis_new=[]
#    d=get_lb(recv_3[i])[2]
#    t=get_agg_frame_loss(d,10)
##
#    for key,value in t.items(): 
#        x_axis_new.append(key)
#        y_axis_new.append(value/len(t))      
#
#    plt.bar(x_axis_new,y_axis_new)
#    plt.xlabel('Interval', fontsize=18)
#    plt.ylabel('PMF of Lost Frames', fontsize=16)
#    plt.title('Node3:PMF_of_lost_frames_for_Run_No'+str(i))
##    plt.savefig('img/Node_2/PMF_of_lost_frames_for_Run_N0'+str(i)+'.png')
#    plt.savefig('img/Node_3/PMF_of_lost_frames_for_Run_N0'+str(i)+'.png')
#    plt.clf()
#    
#for i in range(0,len(recv_4)):
#    x_axis_new=[]
#    y_axis_new=[]
#    d=get_lb(recv_4[i])[2]
#    t=get_agg_frame_loss(d,10)
##
#    for key,value in t.items(): 
#        x_axis_new.append(key)
#        y_axis_new.append(value/len(t))      
#
#    plt.bar(x_axis_new,y_axis_new)
#    plt.xlabel('Interval', fontsize=18)
#    plt.ylabel('PMF of Lost Frames', fontsize=16)
#    plt.title('Node4:PMF_of_lost_frames_for_Run_No'+str(i))
#    plt.savefig('img/Node_4/PMF_of_lost_frames_for_Run_N0'+str(i)+'.png')
#    plt.clf()
#==========================================================================================    

#x_axis_new=[]
#y_axis_new=[]
#d=get_lb(recv_1[0])[2]
#t=get_frame_Ye_n(d,10)
#res=pd.DataFrame(t).transpose()
#res['Interval']=res.index
#res['N']=res[0]
#res['Y']=res[1]
#res.drop(columns =[0,1], inplace = True) 
#res['pmf_no']=res['N']/len(res['N'])
#res['pmf_yes']=res['Y']/len(res['Y'])
#plt.bar(res['Interval'],res['pmf_no'],color='red')
#plt.bar(res['Interval'],res['pmf_yes'],color='blue')


#for key,value in t.items(): 
#        x_axis_new.append(key)
#        y_axis_new.append(value/len(t)) 


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

