import sys
from pprint import pprint
import aoclib
import numpy as np

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
    cell = grid[i, j]
    if isinstance(cell, str):
        return cell

    if background is not None:
        return "X" if int(cell) == 1 else background[i, j]

    return "X" if int(cell) == 1 else "."


def print_grid(grid, background=None):
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


with open(f"/Users/olofenglund/code/advent-of-code/2024/6/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

grid = aoclib.convert_lines_into_grid(lines, dtype=str, split_fun=list)
symbols = index_symbols_in_grid(grid)

pos_x, pos_y = symbols["^"][0]
direction = "^"
mask = np.zeros(grid.shape, dtype=bool)

while in_grid(grid, pos_x, pos_y):
    mask[pos_x, pos_y] = True

    pos_x, pos_y, direction = move(grid, pos_x, pos_y, direction)
    #print_grid(mask, grid)


print(np.sum(mask), file=sys.stderr)
