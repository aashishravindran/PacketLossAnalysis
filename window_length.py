file=open("files/Sync_logs1.txt",'r')

line=file.readlines()
time_stamp={}

for i in range(0,len(line)):
    if "Starting" in line[i]:
        val=i+1;
    else:
       val = i;

    while "Starting" not in line[val] and val+1 < len(line):
        seq = int(line[0].split('and')[0].split('=')[1])
        new = float("{0:.3f}".format(float(line[val].split(', @')[1])))
        if seq in time_stamp:
            time_stamp[seq] = new-time_stamp[seq]
            print('I broke=================='+str(val))
            #break;
        else:
            time_stamp[seq] = new

        val += 1



print(time_stamp)





