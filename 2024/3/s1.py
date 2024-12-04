import sys
from pprint import pprint
import re

with open(f"/Users/olofenglund/code/advent-of-code/2024/3/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

matches = []
for line in lines:
    matches.extend(re.findall("mul\([0-9]+,[0-9+]+\)", line))

tot_mul = 0
for match in matches:
    begin, end = match.split(",")
    print(begin, "and", end)
    num_first = re.search("[0-9]+", begin).group()
    num_end = re.search("[0-9]+", end).group()

    tot_mul += (int(num_first) * int(num_end))

print(tot_mul, file=sys.stderr)
