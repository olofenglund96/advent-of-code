import sys
from pprint import pprint

with open(f"2023/15/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

entries = lines[0].split(",")

csum = 0
for e in entries:
    cval = 0
    for c in list(e):
        cval += ord(c)
        cval *= 17
        cval %= 256
    
    csum += cval


print(csum, file=sys.stderr)
