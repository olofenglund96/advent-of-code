import sys
from pprint import pprint
from neo4j import GraphDatabase
from tqdm import tqdm

input_file = sys.argv[1]

with open(f"2023/10/{input_file}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

driver = GraphDatabase.driver("neo4j+s://f9df972c.databases.neo4j.io", auth=("neo4j", "XNmg0eWmHHog2-G46yQxv6OltxMPw_5XM3EJUn8LsYY"))

symbol_to_coord = {
    "|": [(0, 1), (0, -1)],
    "-": [(1, 0), (-1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, 1), (-1, 0)],
    "F": [(0, 1), (1, 0)],
}

def get_connected_coords(symbol, x, y):
    offsets = symbol_to_coord[symbol]
    ccs = []
    for of in offsets:
        xd, yd = of
        xn, yn = x + xd, y + yd
        if xn < 0 or yn < 0:
            continue

        ccs.append((xn, yn))

    return ccs
    

def get_data(input_file, lines):
    nodes = {}
    start_coords = None
    for y, line in enumerate(tqdm(lines)):
        for x, symbol in enumerate(list(line)):
            #print(symbol)
            if symbol == "S":
                start_coords = (x, y)
            
            if symbol != ".":
                nodes[(x, y)] = {'symbol': symbol, "connections": [], "visited": False, "dist": 0}
    
    rels = []
    for (x, y), node in tqdm(nodes.items()):
        sym = node["symbol"]
        if sym == "S":
            continue
        
        ccs = get_connected_coords(sym, x, y)
        node["connections"] = ccs
        for cc in ccs:
            if cc in nodes and nodes[cc]["symbol"] == "S":
                nodes[cc]["connections"].append((x, y))
        
    return start_coords, nodes

start_coords, nodes = get_data(input_file, lines)

def ac(coord_list, func, ix):
    return func(coord_list, key=lambda c: c[ix])[ix]

import numpy as np

def print_grid(nodes, highlight):
    coord_list = [k for k, v in nodes.items() if v["visited"]]
    minx, maxx, miny, maxy = ac(coord_list, min, 0), ac(coord_list, max, 0), ac(coord_list, min, 1), ac(coord_list, max, 1)

    #sprint(minx, maxx, miny, maxy)

    grid = np.full((4 + maxx - minx, 4 + maxy - miny), ".", dtype=str)

    for x, y in coord_list:
        node = nodes[(x, y)]
        if (x, y) == highlight:
            grid[x - minx + 2, y - miny + 2] = "X"
        else:
            grid[x - minx + 2, y - miny + 2] = node["symbol"]

    #pprint(grid)
    for y in range(4 + maxy - miny):
        for x in range(4 + maxx - minx):
            print(grid[x, y], end="")

        print()

def bfs(nodes, start_node):
    start_node["visited"] = True
    neighbours = [start_node]
    cycle_lengths = []
    while len(neighbours) > 0:
        n = neighbours.pop(0)
        for c in n["connections"]:
            nnode = nodes[c]
            if nnode["visited"]:
                cycle_lengths.append(n["dist"] + 1)
                continue

            nnode["visited"] = True
            nnode["dist"] = n["dist"] + 1

            neighbours.append(nnode)
    

    return cycle_lengths
    
#pprint(nodes)
cl = bfs(nodes, nodes[start_coords])

#pprint(nodes)
#cn = get_connected_nodes(start_node)
#pprint(cn)
#max_cl = max(cl)
#max_node = [k for k,v in nodes.items() if v["dist"] == max_cl]
#print_grid(nodes, max_node[0])

sorted_cl = sorted(cl, reverse=True)
print(sorted_cl[:10])
print(max(cl), file=sys.stderr)
