import pandas as pd


def compute_time_sync(reference_timestamps, new_file, dest_pt):
    test = open(dest_pt, "w")

    ref_index = 0;
    # k=0;
    j = 0;
    length = int(len(new_file))  # Get length of New_file
    print(length)

    while j < length:

        if j == 0:
            # print("I came Here")
            # Time Sync Calcualtion Starts here
            new_val = new_file[0].split(",@")  # Split to get the time Stamp
            count = float("{0:.3f}".format(float(new_val[1]) - reference_timestamps[ref_index]))
            sync_count = float("{0:.3f}".format(float(new_val[1]) - count))
            fin_out = str(new_val[0]) + ", @" + str(sync_count)
            test.write(fin_out + "\n")

        elif (new_file[j].strip() == "=================Starting New Run========="):

            j += 1;
            ref_index += 1
            new_val = new_file[j].split(",@")
            count = float("{0:.3f}".format(float(new_val[1]) - reference_timestamps[ref_index]))
            sync_count = float("{0:.3f}".format(float(new_val[1]) - count))
            fin_out = str(new_val[0]) + ", @" + str(sync_count)
            test.write("=========================Starting New Run==================\n")
            test.write(fin_out + "\n")
            print(fin_out)



        else:
            # Calculating for other frames from the second frame to "Starting new Run"
            new_val_1 = new_file[j].split(",@")
            final_count = float("{0:.3f}".format(float(new_val_1[1]) - sync_count))
            T_count = float("{0:.3f}".format(float(new_val_1[1]) + final_count))
            fin_out_1 = str(new_val_1[0]) + ", @" + str(T_count)
            test.write(fin_out_1 + "\n")
            print("s" + fin_out_1 + "," + str(j))

        j += 1

    test.close()  # Close the file
    return 0;

def get_retransmission_delays (ref,sync):
    #print("Here1")
    difference=[]
    delay={}
    for i in range(0, len(sync)):
        for j in range(0, len(sync[i])):
            # print(sync[i][j])
            # print(sync[i+1][j])
            if sync[i][j] in ref[0]:
                diff = sync[i + 1][j] - ref[1][ref[0].index(sync[i][j])]
                # print(diff)
                difference.append(diff)
                delay[sync[i][j]]=diff


    return delay;





# def get_source_time_stamp(file):
#
#     line=file.readlines()
#     time_stamp={}
#     ts_filnal={}
#     count=0
#     length=len(line)
#
#     for i in range(0,length):
#
#
#         if "Starting" in line[i] or i == length-1:
#
#
#             ts_filnal[count] = time_stamp;
#             t=0
#             time_stamp={}
#             count += 1
#         else :
#             seq = int(line[i].split('and')[0].split('=')[1])
#             new = float("{0:.3f}".format(float(line[i].split(', @')[1])))
#             time_stamp[seq] = new
#
#     return ts_filnal;



# def get_receiver_delays(fp,ts_filnal):
#     ls=fp.readlines()
#
#     length=len(ls)
#
#     lcount=0
#     count=0
#     diff=0.0
#
#     dict={}
#     recv_1={}
#
#     for k in range(0,length):
#
#         if "Starting" in ls[k]:
#             #recv_1[count] = dict
#             dict={}
#             lcount+= 1
#             count+= 1
#
#         else:
#
#             seq = int(ls[k].split('and')[0].split('=')[1])
#             new = float("{0:.3f}".format(float(ls[k].split(', @')[1])))
#             #print(lcount,seq,new)
#
#             if seq in ts_filnal[lcount]:
#                 t=ts_filnal[lcount][seq]
#                 #print(t)
#                 diff=new-ts_filnal[lcount][seq]
#                 dict[seq] = diff
#            # print(k)
#             recv_1[count] = dict
#
#     return recv_1
#
#
#
# file=open("files/Sync_logs1.txt",'r')
# fp=open("files/Sync_logs2.txt",'r')
#
# time_stamp = get_source_time_stamp(file)
# recv = get_receiver_delays(fp,time_stamp)
# print(len(recv))
# print(recv[0][21])



#439199.7920000553



