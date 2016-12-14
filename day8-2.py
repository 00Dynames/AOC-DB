#!/usr/bin/python

import sys

f = open(sys.argv[1])

# maybe set row and col in variables
screen = [[False for n in range(50)] for i in range(6)]

# Read instructions
for line in f:
    line = line.rstrip()
    line = line.split(" ")

    if line[0] == "rect":
        num = [int(i) for i in line[1].split("x")]
        for point in [0, num[1] - 1]:
            for x in range(num[0]):
                screen[point][x] = True
       
        for point in [0, num[0] - 1]:
            for y in range(num[1]):
                screen[y][point] = True

    elif line[0] == "rotate":
        if line[1] == "row":
            shift = int(line[4]) % 50
            row = int((line[2].split("="))[1])
            print row, shift

    
            new_row = [False for i in range(50)]

            for i in range(len(new_row)):
                if i + shift >= len(new_row):
                    new_row[shift - (len(new_row) - i)] = screen[row][i]
                else:
                    new_row[i + shift] = screen[row][i]
            #print new_row, len(new_row)
        
            screen[row] = new_row

        elif line[1] == "column":
            shift = int(line[4]) % 6
            col = int((line[2].split("="))[1])
            print col, shift


            new_col = [False for i in range(6)]

            for i in range(6):
                if i + shift >= 5:
                    new_col[shift - (6 - i)] = screen[i][col]
                else:
                    print i + shift
                    new_col[i + shift] = screen[i][col]

            print new_col

            for i in range(6):
                screen[i][col] = new_col[i]



# Print screen
for i in range(len(screen)):
    for n in range(len(screen[i])):
        if screen[i][n]:
            print "#",
        else:
            print " ",
    print
