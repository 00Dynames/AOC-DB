#!/usr/bin/python

import sys

f = open(sys.argv[1])

result = 0

for line in f:
    line = line.rstrip()
    line = line.split(" ")

    if line[0] == "rect":
        num = [int(i) for i in line[1].split("x")]
        result += num[0] * num[1]
        print num

print result
