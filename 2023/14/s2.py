import sys
from pprint import pprint
import numpy as np
from collections import defaultdict
from tqdm import tqdm

with open(f"2023/14/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

def get_segments(stack):
    segments = defaultdict(int)
    seg_ix = 0
    for i, s in enumerate(stack):
        if s == "O":
            segments[seg_ix] += 1
        
        if s == "#":
            seg_ix = i+1

    return segments

def print_grid(grid, rot=0):
    _grid = np.rot90(grid, rot)
    for row in _grid:
        print("".join(row))


def compute_load(grid):
    max_weight = grid.shape[0]
    weight = 0
    for ix, row in enumerate(grid):
        for cell in row:
            if cell == "O":
                weight += max_weight - ix

    return weight

def find_pattern(weights):
    if len(weights) < 100:
        return False, -1
    
    _weights = weights[len(weights) - 100:]
    wl = set(_weights)

    found_indexes = []
    freq = -1
    for wc in wl:
        fx = []
        for ix, w in enumerate(_weights):
            if w == wc:
                fx.append(ix)

        found_indexes.append(fx)

    lowest_freq = min(found_indexes, key=len)
    if len(lowest_freq) < 2:
        return False, -1
    
    freqs = []
    for i in range(0, len(lowest_freq), 2):
        freqs.append(lowest_freq[i+1] - lowest_freq[i])
    
    print(f"{freqs=}")
    freqs = list(set(freqs))
    if len(freqs) > 1:
        print(f"More than one freq found {freq=}")
        return False, -1

    freq = freqs[0]

    for fxs in found_indexes:
        for fx in fxs[:-1]:
            if fx + freq not in fxs and fx + freq < max(fxs):
                print(f"Some number does not follow {freq=} ({fx + freq} not in {fxs=})")
                return False, -1


    print(f"Frequency is {freq}")
    return True, freq


grid = []
grid_no_rocks = []

for line in lines:
    chars = list(line)
    grid.append(chars)

    no_rocks = []
    for char in chars:
        if char == "O":
            no_rocks.append(".")
            continue

        no_rocks.append(char)
    
    grid_no_rocks.append(no_rocks)



grid = np.rot90(np.array(grid), 1)
grid_no_rocks_s = np.array(grid_no_rocks)

weights = []
freq = -1

for i in range(10000):
    grid_no_rocks = np.rot90(grid_no_rocks_s.copy(), -i % 4)
    grid = np.rot90(grid, -1)

    if i % 4 == 0:
        weight = compute_load(grid)
        weights.append(weight)

    if i % 40 == 0:
        found_freq, freq = find_pattern(weights)
        if found_freq:
            break

    col_segments = {}
    for col in range(len(grid[0])):
        col_segments[col] = get_segments(grid[:,col])

    max_weight = grid.shape[0]
    weight = 0
    for col, segments in col_segments.items():
        for start, rock_count in segments.items():
            grid_no_rocks[start:start+rock_count, col] = "O"

    #print_grid(grid_no_rocks, i % 4)
    grid = grid_no_rocks

if freq == -1:
    print("No freq found")
    print(f"{weights[-50:]}")
    exit(1)

interval = weights[-freq:]
print(f"{interval=}, {i=}")

iterations = int(i / 4)
iterations_left = 1000000000 - iterations - 1

ix = iterations_left % freq
final_num = interval[ix]

print(f"{iterations=}, {iterations_left=}, {ix=}, {final_num=}")
print(final_num, file=sys.stderr)
