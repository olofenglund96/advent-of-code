import sys
from pprint import pprint
import numpy as np
from collections import defaultdict

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


grid = []

for line in lines:
    grid.append(list(line))

grid = np.array(grid)

col_segments = {}
for col in range(len(grid[0])):
    segs = get_segments(grid[:,col])
    if len(segs.keys()) > 0:
        col_segments[col] = segs

#pprint(col_segments)

max_weight = len(lines)

weight = 0
for col, segments in col_segments.items():
    for start, rock_count in segments.items():
        sweight = max_weight + 1 - start
        tweight = sum(range(sweight - rock_count, sweight))
        #print(f"{col=}, {start=}, {tweight=}, weights={list(range(sweight - rock_count, sweight))}")
        weight += tweight



print(weight, file=sys.stderr)
