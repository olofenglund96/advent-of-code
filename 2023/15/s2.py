import sys
from pprint import pprint
from collections import defaultdict

with open(f"2023/15/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

entries = lines[0].split(",")

csum = 0
boxes = defaultdict(list)
label_map = {}
for e in entries:
    if "=" in e:
        label, val = e.split("=")
    else:
        label = e[:-1]
        val = -1

    box_num = 0
    for c in list(label):
        box_num += ord(c)
        box_num *= 17
        box_num %= 256
    
    box = boxes[box_num]
    try:
        label_ix = box.index(label)
    except ValueError:
        label_ix = -1
    
    if val == -1:
        if label_ix == -1:
            continue
        
        del box[label_ix]
        continue

    val = int(val)
    label_map[label] = val
    if label_ix == -1:
        box.append(label)

fsum = 0
for ix in sorted(boxes.keys()):
    labels = boxes[ix]
    mul = 1
    for l in labels:
        foc = label_map[l]
        fsum += (ix + 1) * mul * foc
        mul += 1

print(fsum, file=sys.stderr)
