#!/usr/bin/python

import sys, operator

f = open(sys.argv[1])
first_line = True

word = []

for line in f:
    
    line = line.rstrip()   
 
    if first_line:
        for i in range(len(line)):
            word.append({})    
        first_line = False
    
    for char in range(len(line)):
        
        if line[char] in word[char].keys():
            word[char][line[char]] += 1
        else:
            word[char][line[char]] = 1

for i in range(len(word)):
    print min(word[i].iteritems(), key=operator.itemgetter(1))[0],

#print word
