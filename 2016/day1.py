#!/usr/bin/python

import sys

class elf:

    def __init__(self):
        self.face = "N"
        self.location = [0, 0]
        self.directions = ["N", "E", "S", "W"]
        self.visited = [(0, 0)]

    def adjust_direction(self, direction):
        if direction == "R":
            #print "R"
            self.face = self.directions[(self.directions.index(self.face) + 1) % len(self.directions)]
        elif direction == "L":
            #print "L"
            self.face = self.directions[(self.directions.index(self.face) - 1) % len(self.directions)]

    def travel(self, distance):
        if self.face == "N":
            self.location[1] += distance
        elif self.face == "S":
            self.location[1] -= distance
        elif self.face == "E":
            self.location[0] += distance 
        elif self.face == "W":
            self.location[0] -= distance

    def read_instruction(self, instruction):
        ins_direction = instruction[0]
        ins_distance = int(instruction[1:])

        self.adjust_direction(ins_direction)
        self.travel(ins_distance)

    def get_distance(self):
        return abs(self.location[0]) + abs(self.location[1])
 
bob = elf()
instructions = sys.argv[1]
instructions = instructions.split(", ")

for i in instructions:
    bob.read_instruction(i)

print bob.get_distance()


