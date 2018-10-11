#!/usr/bin/python

import sys, re

f = open(sys.argv[1])
result = 0

for line in f:
   
    line = line.rstrip("\]\n")
    line = re.split("\[", line)

    checksum = line[1]

    temp = line[0].split("-")
    name = ""
    room_id = 0

    for i in temp:
        if re.match("[a-zA-Z]+", i):
            name += i
        else:
            room_id = int(i)

    count = {}
    for char in name:
        if char in count.keys():
            count[char] += 1
        else:
            count[char] = 1

    t_list = []
    for key in count:
        t_list.append((key, count[key]))

    t_list = sorted(t_list, key = lambda x: (-x[1], x[0]))

    t_checksum = ""
    for i in range(5):
        t_checksum += t_list[i][0]

    if t_checksum == checksum:
        result += room_id

print result
f.close()

