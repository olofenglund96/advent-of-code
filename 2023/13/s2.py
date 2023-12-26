import sys
from pprint import pprint
import numpy as np

with open(f"2023/13/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]


def print_pattern_row(row):
    pstr = ""
    for r in row:
        if r:
            pstr += "#"
        else:
            pstr += "."

    print(pstr)

def is_reflection(pattern, tlen, reflection_ix):
    smudge_fixed = False
    for i in range(reflection_ix, -1, -1):
        dist_to_reflection = reflection_ix - i
        reflected_i = reflection_ix + dist_to_reflection + 1
        if reflected_i >= tlen:
            return smudge_fixed

        org_p = pattern[i, :]
        ref_p = pattern[reflected_i, :]
        comp = org_p != ref_p
        diffs = np.count_nonzero(comp)

        #print(f"({reflection_ix=}, {i=}, {reflected_i=}) {diffs=}")
        #print_pattern_row(org_p)
        #print_pattern_row(ref_p)

        if diffs == 0:
            continue

        if diffs == 1 and not smudge_fixed:
            smudge_fixed = True
            continue

        return False

    return smudge_fixed

def find_reflections(pattern):
    ylen, xlen = pattern.shape
    colr, rowr = 0, 0
    # col reflection
    #print("Checking cols")
    for col in range(0, xlen-1):
        if is_reflection(pattern.transpose(), xlen, col):
            colr = col + 1
            #print(f"Reflection around {col=}!")

    # row reflection
    #print("Checking rows")
    for row in range(0, ylen-1):
        if is_reflection(pattern, ylen, row):
            rowr = row + 1
            #print(f"Reflection around {row=}!")

    return colr, rowr

patterns = []

pattern = []
for line in lines:
    if line == "" and len(pattern) != 0:
        patterns.append(np.array(pattern))
        pattern = []
        continue

    symbols = [s == "#" for s in line]
    pattern.append(symbols)

patterns.append(np.array(pattern))

refsum = 0

for pattern in patterns:
    colr, rowr = find_reflections(pattern)
    #input(f"{colr=}, {rowr=}")
    refsum += colr + rowr * 100

print(refsum, file=sys.stderr)