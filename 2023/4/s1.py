import sys
from pprint import pprint
import math

with open(f"2023/4/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

w_nbrs = []
my_nbrs = []

for line in lines:
    start = line.index(":")
    divider = line.index("|")
    wns = line[start+1:divider]
    mns = line[divider+1:]

    wn = [int(n.strip()) for n in wns.split(" ") if n != ""]
    mn = [int(n.strip()) for n in mns.split(" ") if n != ""]

    w_nbrs.append(wn)
    my_nbrs.append(mn)

#pprint(w_nbrs)
#pprint(my_nbrs)

score = 0
for wn, mn in zip(w_nbrs, my_nbrs):
    #isect = set(w_nbrs).intersection(my_nbrs)
    count = 0
    for n in mn:
        if n in wn:
            count += 1
    
    if count == 0:
        continue
    score += int(math.pow(2, count - 1))
    #print(f"{score=}, {count=}, this score: {sc}")


print(score, file=sys.stderr)
