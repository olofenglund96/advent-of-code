import sys
from pprint import pprint
import numpy as np
from dataclasses import dataclass

class Beam:
    def __init__(self, loc, vel):
        self.loc = loc

        self.vel = vel

    def __str__(self) -> str:
        return f"Beam({self.loc=}, {self.vel=})"
    
    def __repr__(self) -> str:
        return f"Beam({self.loc=}, {self.vel=})"

    def move(self):
        xloc, yloc = self.loc
        xvel, yvel = self.vel
        xloc += xvel
        yloc += yvel
        self.loc = (xloc, yloc)

    def turn(self, left=False):
        xvel, yvel = self.vel

        if not left:
            self.vel = (-yvel, xvel)
        else:
            self.vel = (yvel, -xvel)

        self.move()

    def turn_symbol(self, symbol):
        xvel, yvel = self.vel

        if symbol == "/":
            if xvel != 0:
                return self.turn(left=True)
            
            if yvel != 0:
                return self.turn()
            
        if symbol == "\\":
            if xvel != 0:
                return self.turn()
            
            if yvel != 0:
                return self.turn(left=True)


    def split(self):
        new_beam = Beam(self.loc, self.vel)

        self.turn(left=True)
        new_beam.turn()

        self.move()
        new_beam.move()
        
        return new_beam
    
    def outside(self, xmax, ymax):



with open(f"2023/16/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

grid = []
for line in lines:
    grid.append(list(line))

xmax = len(grid[0])
ymax = len(grid)
grid_counts = np.zeros((len(grid[0]), len(grid)))
grid = np.array(grid)


# xpos, ypos, xvel, yvel
beams = [Beam((0, 0), (1, 0))]

while True:
    new_beams = []
    for beam in beams:
        sym = grid[beam.loc]

        if sym == ".":
            beam.move()
        elif sym == "|" or sym == "-":
            new_beam = beam.split()
            new_beams.append(new_beam)
        else:
            beam.turn_symbol(sym)

    beams = beams + new_beams
    
    filtered_beams = []
    for beam in beams:
        if not beam.outside(xmax=xmax, ymax=ymax):
            filtered_beams.append(beam)

    pprint(beams)
    input()



print(lines[-1], file=sys.stderr)
