import sys
from pprint import pprint

with open(f"2023/8/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

instructions = list(lines[0].strip())

graph = {}
for line in lines[2:]:
    node, relations = line.replace(" ", "").strip().split("=")
    graph[node] = relations[1:-1].split(",")

#pprint(graph)

target = "ZZZ"
node = "AAA"
instr_ix = 0
steps = 0
while True:
    instr = instructions[instr_ix]
    instr_ix = (instr_ix + 1) % len(instructions)
    nodes = graph[node]
    if instr == "L":
        next_node = nodes[0]
    elif instr == "R":
        next_node = nodes[1]
    
    steps += 1

    #input(f"Step: {steps}, Ins: {instr}, ")
    
    if next_node == target:
        break

    node = next_node

#print(steps)

print(steps, file=sys.stderr)
