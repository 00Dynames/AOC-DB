#!/usr/bin/python

import sys

class Tile:
    
    def __init__(self, value):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.value = value
    
    # might be redundant, it's mostly for following the OO principle 
    # of have public/private variables
    def add_neighbour(self, direction, neighbour):
        if direction == "UP":
            self.up = neighour
        elif direction == "DOWN":
            self.down = neighbour
        elif direction == "RIGHT":
            self.right = neighbour
        elif direction == "LEFT":
            self.left = neighbour

# can have this in a dict
# not too different from the last exercise
# the num_pad is still mostly hard coded in 

num_pad = {"one": Tile("1"),
           "two": Tile("2"),
           "three": Tile("3"),
           "four": Tile("4"),
           "five": Tile("5"),
           "six": Tile("6"),
           "seven": Tile("7"),
           "eight": Tile("8"),
           "nine": Tile("9"),
           "A": Tile("A"),
           "B": Tile("B"),
           "C": Tile("C"),
           "D": Tile("D")
}

num_pad["one"].down = num_pad["three"]

num_pad["two"].right = num_pad["three"]
num_pad["two"].down = num_pad["six"]

num_pad["three"].up = num_pad["one"]
num_pad["three"].down = num_pad["seven"]
num_pad["three"].right = num_pad["four"]
num_pad["three"].left = num_pad["two"]

num_pad["four"].left = num_pad["three"]
num_pad["four"].down = num_pad["eight"]

num_pad["five"].right = num_pad["six"]

num_pad["six"].up = num_pad["two"]
num_pad["six"].down = num_pad["A"]
num_pad["six"].right = num_pad["seven"]
num_pad["six"].left = num_pad["five"]

num_pad["seven"].up = num_pad["three"]
num_pad["seven"].down = num_pad["B"]
num_pad["seven"].right = num_pad["eight"]
num_pad["seven"].left = num_pad["six"]

num_pad["eight"].up = num_pad["four"]
num_pad["eight"].right = num_pad["nine"]
num_pad["eight"].down = num_pad["C"]
num_pad["eight"].left = num_pad["seven"]

num_pad["nine"].left = num_pad["eight"]

num_pad["B"].up = num_pad["seven"]
num_pad["B"].right = num_pad["C"]
num_pad["B"].down = num_pad["D"]
num_pad["B"].left = num_pad["A"]

num_pad["A"].up = num_pad["six"]
num_pad["A"].right = num_pad["B"]

num_pad["C"].up = num_pad["eight"]
num_pad["C"].left = num_pad["B"]

num_pad["D"].up = num_pad["B"]

f = open(sys.argv[1])
code = ""
current = num_pad["five"]

for line in f:
    for char in line:
        print char, current.value,
        if char == "U" and current.up != None:
            current = current.up
        elif char == "D" and current.down != None:
            current = current.down
        elif char == "L" and current.left != None:
            current = current.left
        elif char == "R" and current.right != None:
            current = current.right
    
    code += current.value
    print current.value

print code
f.close()
