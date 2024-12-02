import sys
from pprint import pprint

with open(f"/Users/olofenglund/code/advent-of-code/2024/1/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

l1, l2 = [], []

for line in lines:
    l11, l22 = line.split()
    l1.append(int(l11))
    l2.append(int(l22))


l1.sort()
l2.sort()

diffs = 0
for l11, l22 in zip(l1, l2):
    diffs += abs(l11 - l22)

print(diffs, file=sys.stderr)
