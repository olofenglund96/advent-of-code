
import sys
import numpy as np
import re
from pprint import pprint

with open(f"2023/3/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

grid = []
nums = []
for ix, line in enumerate(lines):
    chars = list(line)
    grid.append(chars)

    matches = re.finditer(r"\d+", line)
    for match in matches:
        indexes = list(range(match.start(), match.end()))
        number = match.group()

        nums.append((number, ix, indexes)),

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

            nbs.append(grid[yc][xc])

    return nbs

num_sum = 0
for num, y_ix, x_ixs in nums:
    #print(f"=== Num: {num} ===")
    all_nbds = []
    for ix in x_ixs:
        all_nbds.extend(neighbours(grid, ix, y_ix))

    #print(f"{all_nbds=}")
    symbols = re.findall(r'[^\w\d\s.]', "".join(all_nbds))

    if len(symbols) != 0:
        #print("Symbols!!")
        #print(f"{num=}, {symbols=}")
        num_sum += int(num)


print(num_sum, file=sys.stderr)
