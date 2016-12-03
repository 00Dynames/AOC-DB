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
            self.face = self.directions[(self.directions.index(self.face) + 1) % len(self.directions)]
        elif direction == "L":
            self.face = self.directions[(self.directions.index(self.face) - 1) % len(self.directions)]

    def travel(self, distance):
        if self.face == "N":
            for i in range(distance):
                self.location[1] += 1
                if (self.location[0], self.location[1]) not in self.visited:
                    self.visited.append((self.location[0], self.location[1]))
                else:
                    return False
        elif self.face == "S":
            for i in range(distance):
                self.location[1] -= 1
                if (self.location[0], self.location[1]) not in  self.visited:
                    self.visited.append((self.location[0], self.location[1]))
                else:
                    return False
        elif self.face == "E":
            for i in range(distance):
                self.location[0] += 1
                if (self.location[0], self.location[1]) not in self.visited:
                    self.visited.append((self.location[0], self.location[1]))
                else:
                    return False
        elif self.face == "W":
            for i in range(distance):
                self.location[0] -= 1
                if (self.location[0], self.location[1]) not in self.visited:
                    self.visited.append((self.location[0], self.location[1]))
                else:
                    return False

    def read_instruction(self, instruction):
        ins_direction = instruction[0]
        ins_distance = int(instruction[1:])

        self.adjust_direction(ins_direction)
        if self.travel(ins_distance) == False:
            return False

    def get_distance(self):
        return abs(self.location[0]) + abs(self.location[1])
 
bob = elf()
instructions = sys.argv[1]
instructions = instructions.split(", ")

for i in instructions:
    if bob.read_instruction(i) == False:
        break

print bob.get_distance()

