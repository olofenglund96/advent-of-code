import sys
from pprint import pprint
import numpy as np
from dataclasses import dataclass
from collections import defaultdict
from tqdm import tqdm

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
        #print(f"Turn {left=} at {self.loc=}")
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


    def maybe_split(self, sym):
        xvel, yvel = self.vel
        if (sym == "-" and yvel == 0) or (sym == "|" and xvel == 0):
            self.move()
            return None
        
        #print(f"Split at {self.loc=}")
        new_beam = Beam(self.loc, self.vel)

        self.turn(left=True)
        new_beam.turn()
        
        return new_beam
    
    def inside(self, xmax, ymax):
        xloc, yloc = self.loc
        return xloc >= 0 and xloc < xmax and yloc >= 0 and yloc < ymax


def print_grid(grid, pois):
    for y, row in enumerate(grid):
        line = ""
        for x, cell in enumerate(row):
            if (x, y) in pois:
                line += "o"
            else:
                line += cell
        
        print(line)


with open(f"2023/16/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

grid = []
for line in lines:
    grid.append(list(line))

xmax = len(grid[0])
ymax = len(grid)
grid_arr = grid
grid = np.array(grid)

starting_beams = []
for x in range(xmax):
    starting_beams.append(Beam((x, 0), (0, 1)))
    starting_beams.append(Beam((x, ymax-1), (0, -1)))

for y in range(ymax):
    starting_beams.append(Beam((0, y), (1, 0)))
    starting_beams.append(Beam((xmax-1, y), (-1, 0)))

#pprint(starting_beams)

max_energy = 0
for sbeam in tqdm(starting_beams):
    #print(f"Doing beam {sbeam=}")
    grid_counts = np.zeros((xmax, ymax))
    grid_beam_history = defaultdict(list)

    beams = [sbeam]
    const_iters = 0
    prev_e_cells = 0
    while True:
        new_beams = []
        for beam in beams:
            if beam.vel in grid_beam_history[beam.loc]:
                continue

            grid_beam_history[beam.loc].append(beam.vel)
            grid_counts[beam.loc[1], beam.loc[0]] = 1
            sym = grid[beam.loc[1], beam.loc[0]]

            if sym == ".":
                beam.move()
            elif sym == "|" or sym == "-":
                new_beam = beam.maybe_split(sym)
                if new_beam is not None and new_beam.inside(xmax, ymax):
                    new_beams.append(new_beam)
            else:
                beam.turn_symbol(sym)

            if beam.inside(xmax, ymax):
                new_beams.append(beam)

        beams = new_beams
        # pois = []
        # for b in beams:
        #     pois.append(b.loc)
        # print_grid(grid, pois)
        # pprint(beams)

        energized_cells = np.count_nonzero(grid_counts)
        if energized_cells == prev_e_cells:
            const_iters += 1
        else:
            const_iters = 0

        prev_e_cells = energized_cells

        if const_iters > 10:
            break
        
        if len(new_beams) == 0:
            break

        #input()

    if energized_cells > max_energy:
        max_energy = energized_cells

print(max_energy, file=sys.stderr)
