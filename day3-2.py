#!/usr/bin/python

import sys, re

f = open(sys.argv[1])
count = 0
line_num = 1

col = [[], [], []]

for line in f:

    line = line.rstrip()
    line = re.sub("^\s+","", line)
    line = re.split(" *", line)

    for i in range(len(line)):
        col[i].append(int(line[i]))

    if line_num % 3 == 0:
    
        for c in col:
            c_count = 0
            for i in range(len(c)):
                if c[i] + c[(i + 1) % len(c)] > c[(i + 2) % len(c)]:
                    c_count += 1
            
            if c_count == 3:
                count += 1
        
        col = [[], [], []]
    
    line_num += 1

print count
f.close()
