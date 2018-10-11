#!/usr/bin/python 

import sys, re

f = open(sys.argv[1])

regex = r"(?=((\w)(\w)(?!\3))\2)"
result = 0

for line in f:
    print line,
    line = line.rstrip()
    line = re.split("[\[\]]", line)    
    
    #line_result = True
    bab = []

    for char in range(0, len(line), 2):
        if re.search(regex, line[char]):
            match_iter = re.finditer(regex, line[char])
            match_result = [match.groups() for match in match_iter] 
            bab = [i[2] + i[1] + i[2] for i in match_result]
            break
    #        line_result = False
    
    print bab


    #if not line_result:
    #    continue
    #line_result = False

    for char in range(1, len(line), 2):
        for i in bab:
            if re.search(i, line[char]):
                print True
                result += 1



    #        line_result = True

    print line
    #if line_result:
    #    result += 1

print result
