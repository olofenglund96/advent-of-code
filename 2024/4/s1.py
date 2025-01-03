import sys
from pprint import pprint
import numpy as np
from collections import defaultdict

def convert_lines_into_grid(lines, dtype=str, split_fun=list):
    grid = np.zeros(shape=(len(lines[0]), len(lines)), dtype=dtype)

    for i, line in enumerate(lines):
        grid[i,:] = np.array(split_fun(line))

    return grid

def get_adjacent_elements(grid, x, y, depth=1, geometry="euclidean"):
    if geometry != "euclidean":
        raise Exception(f"geometry '{geometry}' not supported")

    offsets = []
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            offsets.append((i,j))

    elements = defaultdict(list)

    for i, j in offsets:
        for d in range(depth):
            offset_x = x + i*(d+1)
            offset_y = y + j*(d+1)
            if (offset_x < 0 or offset_x > grid.shape[0]-1) or (offset_y < 0 or offset_y > grid.shape[1]-1):
                continue

            offset_x = max(min(offset_x, grid.shape[0]), 0)
            offset_y = max(min(offset_y, grid.shape[1]), 0)

            elements[(i,j)].append(grid[offset_x,offset_y])

    return elements

with open(f"/Users/olofenglund/code/advent-of-code/2024/4/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

grid = convert_lines_into_grid(lines, dtype=str, split_fun=list)

xmas_count = 0
for i, j in np.argwhere(grid == "X"):
    adjacent_elems = get_adjacent_elements(grid, i, j, depth=3)
    for elems in adjacent_elems.values():
        if "".join(elems) == "MAS":
            xmas_count += 1

print(xmas_count, file=sys.stderr)
