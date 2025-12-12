#!/usr/bin/env python3
fname = input('Enter the file name; ')
if len(fname) < 1:
    fname = 'clown.txt'
handle = open(fname)
di = dict()
for line in handle:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    for w in wds:
        di[w] = di.get(w,0) + 1
#print(di)
largest = -1
theword = None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k
print("done", theword, largest)



