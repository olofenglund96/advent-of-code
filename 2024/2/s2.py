import sys
from pprint import pprint
import numpy as np

def eval_row(row):
    descending = None
    for i, col in enumerate(row[1:]):
        diff = col - row[i]

        if descending is None:
            descending = diff > 0
        elif descending != (diff > 0):
            print(f"Invalid row, switch dir: {row}")
            ixs = [i, i+1]
            if i > 0:
                ixs.append(i-1)

            return ixs

        if abs(diff) > 3 or diff == 0:
            print(f"Invalid row, diff > 3 ({abs(diff)}): {row}")
            return [i, i+1]

    return []

with open(f"/Users/olofenglund/code/advent-of-code/2024/2/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

rows = [None]*len(lines)
for i, line in enumerate(lines):
    rows[i] = [int(l) for l in line.strip().split()]

row_valid = [True]*len(lines)

for row_ix, row in enumerate(rows):
    print(f"Row: {row}")
    row_skip_ixs = eval_row(row)
    if len(row_skip_ixs) == 0:
        continue

    for ix in row_skip_ixs:
        patched_skip_ixs = eval_row(row[:ix] + row[ix+1:])
        if len(patched_skip_ixs) == 0:
            row_valid[row_ix] = True
            break

        row_valid[row_ix] = False

print(row_valid)

print(sum(row_valid), file=sys.stderr)
