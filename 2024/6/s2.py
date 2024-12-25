import sys
from pprint import pprint
import aoclib
import numpy as np
from collections import defaultdict

direction_map = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

direction_order = ["^", ">", "v", "<"]

def index_symbols_in_grid(grid):
    unique_symbols = np.unique(grid)
    symbol_map = {}
    for sym in unique_symbols:
        symbol_map[sym] = np.argwhere(grid == sym)

    return symbol_map

def in_grid(grid, x, y):
    return (x >= 0 and x < grid.shape[0]) and (y >= 0 and y < grid.shape[1])

def _cell_to_str(grid, i, j, background=None):
    bgcell = background[i, j] if background is not None else "."
    cell = grid[i, j]
    if isinstance(cell, str):
        return cell if cell != "" else bgcell

    return "X" if int(cell) == 1 else bgcell


def print_grid(grid, background=None):
    printstr = ""
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            printstr += _cell_to_str(grid, i, j, background=background)
        printstr += "\n"

    print(printstr)

def print_grid_area(grid, center_x, center_y, radius, background=None,):
    min_x = max(center_x - radius, 0)
    max_x = min(center_x + radius, grid.shape[0])

    min_y = max(center_y - radius, 0)
    max_y = min(center_y + radius, grid.shape[1])

    grid = grid[min_x:max_x, min_y:max_y]
    if background is not None:
        background = background[min_x:max_x, min_y:max_y]


    printstr = ""
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            printstr += _cell_to_str(grid, i, j, background=background)
        printstr += "\n"

    print(printstr)


def get_next_pos(pos_x, pos_y, direction):
    step_x, step_y = direction_map[direction]
    return pos_x + step_x, pos_y + step_y


def move(grid, pos_x, pos_y, direction):
    next_x, next_y = get_next_pos(pos_x, pos_y, direction)

    if not in_grid(grid, next_x, next_y):
        return next_x, next_y, direction

    next_sym = grid[next_x, next_y]
    if next_sym != "#":
        return next_x, next_y, direction

    direction = direction_order[(direction_order.index(direction) + 1) % len(direction_order)]
    next_x, next_y = get_next_pos(pos_x, pos_y, direction)

    return next_x, next_y, direction

def next_pos_obs_loops(grid, mask, pos_x, pos_y, direction):
    while in_grid(grid, pos_x, pos_y):
        if direction in mask[(pos_x, pos_y)]:
            #mask[pos_x, pos_y] = "8"

            #print_grid_area(mask, pos_x, pos_y, 10, grid)
            return True

        mask[(pos_x, pos_y)].append(direction)
        pos_x, pos_y, direction = move(grid, pos_x, pos_y, direction)

    return False


with open(f"/Users/olofenglund/code/advent-of-code/2024/6/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

grid = aoclib.convert_lines_into_grid(lines, dtype=str, split_fun=list)
symbols = index_symbols_in_grid(grid)

pos_x, pos_y = symbols["^"][0]
spx, spy = pos_x, pos_y
direction = "^"
mask = defaultdict(list)
placed_obs_loc = np.zeros(grid.shape, dtype=bool)

while in_grid(grid, pos_x, pos_y):
    npos_x, npos_y, ndirection = move(grid, pos_x, pos_y, direction)
    if not in_grid(grid, npos_x, npos_y):
        break

    grid[npos_x, npos_y] = "#"
    pmask = mask.copy()
    placed_obs = next_pos_obs_loops(grid, pmask, pos_x, pos_y, direction)
    grid[npos_x, npos_y] = "."

    if placed_obs:
        if npos_x == spx and npos_y == spy:
            print("Not allowed in start point")
        else:
            placed_obs_loc[npos_x, npos_y] = True


    mask[(pos_x, pos_y)].append(direction)
    pos_x, pos_y, direction = npos_x, npos_y, ndirection

#1401 < x < 1479

print(np.sum(placed_obs_loc), file=sys.stderr)
