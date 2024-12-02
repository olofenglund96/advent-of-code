import sys
from pprint import pprint
from collections import Counter

with open(f"/Users/olofenglund/code/advent-of-code/2024/1/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

l1, l2 = [], []

for line in lines:
    l11, l22 = line.split()
    l1.append(int(l11))
    l2.append(int(l22))


l1.sort()
l2c = Counter(l2)

print(l2c)

sim = 0
for l11 in l1:
    l22 = l2c.get(l11)
    if l22 is not None:
        sim += l11 * l22

print(sim, file=sys.stderr)
