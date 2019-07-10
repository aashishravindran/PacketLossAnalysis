import pandas as pd



def get_source_time_stamp(file):

    line=file.readlines()
    time_stamp={}
    ts_filnal={}
    count=0
    length=len(line)

    for i in range(0,length):


        if "Starting" in line[i] or i == length-1:


            ts_filnal[count] = time_stamp;
            t=0
            time_stamp={}
            count += 1
        else :
            seq = int(line[i].split('and')[0].split('=')[1])
            new = float("{0:.3f}".format(float(line[i].split(', @')[1])))
            time_stamp[seq] = new

    return ts_filnal;



def get_receiver_delays(fp,ts_filnal):
    ls=fp.readlines()

    length=len(ls)

    lcount=0
    count=0
    diff=0.0

    dict={}
    recv_1={}

    for k in range(0,length):

        if "Starting" in ls[k]:
            #recv_1[count] = dict
            dict={}
            lcount+= 1
            count+= 1

        else:

            seq = int(ls[k].split('and')[0].split('=')[1])
            new = float("{0:.3f}".format(float(ls[k].split(', @')[1])))
            #print(lcount,seq,new)

            if seq in ts_filnal[lcount]:
                t=ts_filnal[lcount][seq]
                #print(t)
                diff=new-ts_filnal[lcount][seq]
                dict[seq] = diff
           # print(k)
            recv_1[count] = dict

    return recv_1



file=open("files/Sync_logs1.txt",'r')
fp=open("files/Sync_logs2.txt",'r')

time_stamp = get_source_time_stamp(file)
recv = get_receiver_delays(fp,time_stamp)
print(len(recv))
print(recv[3][21])



439199.7920000553



