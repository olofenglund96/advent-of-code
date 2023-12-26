import sys
from pprint import pprint
import math

with open(f"2023/4/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

cards = []

for line in lines:
    start = line.index(":")
    divider = line.index("|")
    wns = line[start+1:divider]
    mns = line[divider+1:]

    wn = [int(n.strip()) for n in wns.split(" ") if n != ""]
    mn = [int(n.strip()) for n in mns.split(" ") if n != ""]

    cards.append((set(wn), set(mn)))

def compute_scores(ixs):
    next_ixs = []
    #print(f"{ixs=}")
    for ix in ixs:
        #print(f"{ix=}")
        wn, mn = cards[ix]
        isect_count = len(wn.intersection(mn))
        
        if isect_count == 0:
            continue

        ni = list(range(ix+1, ix+isect_count+1))
        next_ixs.extend(ni)
        #print(f"{isect_count=}, {ni=}")
        #input()

    return next_ixs

ni = compute_scores(list(range(len(cards))))

tot_sc = len(cards) +len(ni)
while True:
    ni = compute_scores(ni)
    if len(ni) == 0:
        break

    tot_sc += len(ni)

print(tot_sc, file=sys.stderr)
