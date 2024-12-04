import sys
from pprint import pprint
import re

with open(f"/Users/olofenglund/code/advent-of-code/2024/3/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

instr = "".join(lines)

ix = 0
doing = True
mulsum = 0
while ix < len(instr):
    match = re.search("mul\([0-9]+,[0-9+]+\)|do\(\)|don't\(\)", instr[ix:])
    if match is None:
        break

    print(match)
    ix += match.span()[1]

    if match.group().startswith("mul("):
        if doing:
            begin, end = match.group().split(",")
            num_first = re.search("[0-9]+", begin).group()
            num_end = re.search("[0-9]+", end).group()
            mulsum += (int(num_first) * int(num_end))

        continue

    doing = match.group() == "do()"

print(mulsum, file=sys.stderr)
