#!/usr/bin/python 

import sys, re

f = open(sys.argv[1])

regex = r"(\w)(\w)(?!\1)\2\1"
result = 0

for line in f:

    line = line.rstrip()
    line = re.split("[\[\]]", line)    
    
    line_result = True 

    for char in range(1, len(line), 2):
        if re.search(regex, line[char]):
            line_result = False

    if not line_result:
        continue
    line_result = False

    for char in range(0, len(line), 2):
        if re.search(regex, line[char]):
            line_result = True

    print line, line_result
    if line_result:
        result += 1

print result
