#!/usr/bin/python

import sys, re

f = open(sys.argv[1])
count = 0

for line in f:

    line = line.rstrip()
    line = re.sub("^\s+","", line)
    line = re.split(" *", line)

    for i in range(len(line)):
        line[i] = int(line[i])    
    
    c_count = 0
    for i in range(len(line)):
        if line[i] + line[(i + 1) % len(line)] > line[(i + 2) % len(line)]:
            c_count += 1
            #print True

    if c_count == 3:
        count += 1
        #print line

print count
f.close()
