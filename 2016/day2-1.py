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
one = Tile("1")
two = Tile("2")
three = Tile("3")
four = Tile("4")
five = Tile("5")
six = Tile("6")
seven = Tile("7")
eight = Tile("8")
nine = Tile("9")


one.right = two
one.down = four

two.left = one
two.right = three
two.down = five

three.left = two
three.down = six

four.up = one
four.down = seven 
four.right = five

five.up = two
five.down = eight
five.left = four 
five.right = six

six.left = five
six.up = three
six.down = nine

seven.up = four
seven.right = eight

eight.up = five
eight.left = seven
eight.right = nine

nine.up = six
nine.left = eight         

f = open(sys.argv[1])
code = ""
current = five

for line in f:
    for char in line:
        if char == "U" and current.up != None:
            current = current.up
        elif char == "D" and current.down != None:
            current = current.down
        elif char == "L" and current.left != None:
            current = current.left
        elif char == "R" and current.right != None:
            current = current.right
    
    code += current.value

print code
f.close()
