import sys
from pprint import pprint

with open(f"2023/8/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

instructions = list(lines[0].strip())

graph = {}
nodes = []
for line in lines[2:]:
    node, relations = line.replace(" ", "").strip().split("=")
    graph[node] = relations[1:-1].split(",")
    if node.endswith("A"):
        nodes.append(node)


def step(graph, node, instr):
    _nodes = graph[node]
    if instr == "L":
        next_node = _nodes[0]
    elif instr == "R":
        next_node = _nodes[1]

    return next_node

intervals = []
for ix, node in enumerate(nodes):
    instr_ix = 0
    steps = 0
    interval = 0
    while True:
        instr = instructions[instr_ix]
        instr_ix = (instr_ix + 1) % len(instructions)
        
        node = step(graph, node, instr)

        steps += 1

        #input(f"Step: {steps}, Ins: {instr}, ")
        if node.endswith("Z"):
            new_interval = steps - interval
            if new_interval == interval:
                print(f"{ix}: found stable interval {interval}")
                intervals.append(interval)
                break
                
            interval = new_interval


import math

# ival_sums = intervals.copy()
# matching_val = 0
# while True:
#     min_ival_ix = np.argmin(ival_sums)
#     ival_sums[min_ival_ix] += intervals[min_ival_ix]

#     if len(set(ival_sums)) == 1:
#         matching_val = ival_sums[0]
#         break

#     #input(ival_sums)

print(math.lcm(*intervals), file=sys.stderr)
