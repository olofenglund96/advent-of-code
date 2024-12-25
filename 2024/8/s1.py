import sys
from pprint import pprint

with open(f"/Users/olofenglund/code/advent-of-code/2024/8/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

print(lines[-1], file=sys.stderr)
