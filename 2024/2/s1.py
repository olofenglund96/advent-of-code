import sys
from pprint import pprint
import numpy as np

with open(f"/Users/olofenglund/code/advent-of-code/2024/2/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

rows = [None]*len(lines)
for i, line in enumerate(lines):
    rows[i] = [int(l) for l in line.strip().split()]

row_valid = [True]*len(lines)

for row_ix, row in enumerate(rows):
    descending = None
    print(f"Row: {row}")
    for i, col in enumerate(row[1:]):
        diff = col - row[i]
        print(diff)
        if descending is None:
            descending = diff > 0
        elif descending != (diff > 0):
            print(f"Invalid row, switch dir: {row}")
            row_valid[row_ix] = False
            break

        if abs(diff) > 3 or diff == 0:
            print(f"Invalid row, diff > 3 ({abs(diff)}): {row}")
            row_valid[row_ix] = False
            break

print(row_valid)

print(sum(row_valid), file=sys.stderr)
