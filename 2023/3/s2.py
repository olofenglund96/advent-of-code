
import sys
import numpy as np
import re
from pprint import pprint
from collections import defaultdict

with open(f"2023/3/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

grid = []
nums = []
gears = []
for ix, line in enumerate(lines):
    chars = list(line)
    grid.append(chars)

    matches = re.finditer(r"\d+", line)
    for match in matches:
        indexes = list(range(match.start(), match.end()))
        number = match.group()

        nums.append((number, ix, indexes))

    for jx, c in enumerate(chars):
        if c == "*":
            gears.append((ix, jx))


def neighbours(grid, x, y):
    nb_coords_x = [x-1, x, x+1]
    nb_coords_y = [y-1, y, y+1]

    max_y = len(grid)-1
    max_x = len(grid[0])-1

    nbs = []
    for xc in nb_coords_x:
        if xc < 0 or xc > max_x:
            continue

        for yc in nb_coords_y:
            if yc < 0 or yc > max_y:
                continue

            nbs.append((yc, xc))

    return nbs

gear_to_num = defaultdict(list)
for gy, gx in gears:
    for num, y_ix, x_ixs in nums:
        all_nbds = []
        for ix in x_ixs:
            for ny, nx in neighbours(grid, ix, y_ix):
                if (ny, nx) not in all_nbds:
                    all_nbds.append((ny, nx))
        
        for yn, xn in all_nbds:
            if gy == yn and gx == xn:
                gear_to_num[(gy, gx)].append(num)

gearsum = 0
for nums in gear_to_num.values():
    if len(nums) < 2:
        continue
    gearmul = 1
    for num in nums:
        gearmul *= int(num)

    gearsum += gearmul


print(gearsum, file=sys.stderr)
