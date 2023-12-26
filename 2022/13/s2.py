
import sys

with open("2022/13/input", "r") as file:
    lines = [l.strip() for l in file.readlines()]

print(lines[-1], file=sys.stderr)
