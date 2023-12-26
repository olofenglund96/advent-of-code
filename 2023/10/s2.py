import sys
from pprint import pprint
from neo4j import GraphDatabase
from tqdm import tqdm
from icecream import ic

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
    for y, line in enumerate(lines):
        for x, symbol in enumerate(list(line)):
            #print(symbol)
            if symbol == "S":
                start_coords = (x, y)
            
            if symbol != ".":
                nodes[(x, y)] = {'symbol': symbol, "connections": [], "visited": False, "dist": 0}
    
    rels = []
    for (x, y), node in nodes.items():
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

def bfs(nodes, start_coords):
    start_node = nodes[start_coords]
    start_node["visited"] = True
    start_node["parent"] = ()
    start_node["gid"] = -1
    neighbours = [(start_coords, start_node)]
    while len(neighbours) > 0:
        coords, n = neighbours.pop(0)
        for i, c in enumerate(n["connections"]):
            nnode = nodes[c]

            if nnode["visited"]:
                if nnode["gid"] != n["gid"] and nnode["gid"] != -1:
                    
                    print(f"Found loop! {nnode=}")
                continue


            if n["gid"] == -1:
                nnode["gid"] = i
            else:
                nnode["gid"] = n["gid"]                
            
            nnode["visited"] = True
            nnode["dist"] = n["dist"] + 1
            nnode["parent"] = coords

            neighbours.append((c, nnode))

def dfs(nodes, coords, dist):
    node = nodes[coords]
    node["visited"] = True
    node["dist"] = dist
    for c in node["connections"]:
        next_node = nodes[c]
        if next_node["visited"]:
            continue
        
        next_node["parent"] = coords
        dfs(nodes, c, dist + 1)

    
     
#pprint(nodes)
dfs(nodes, start_coords, 0)

#pprint(nodes)
max_dist = max(nodes.values(), key=lambda v: v["dist"])

max_node = nodes[start_coords]
for k, v in nodes.items():
    if v["dist"] > max_dist["dist"] - 3:
        print(f"{k} -> {v}")
    
    if v["dist"] > max_node["dist"]:
        max_node = v

snode = max_dist
while "parent" in snode:
    snode["in_loop"] = True
    snode = nodes[snode["parent"]]

nodes[start_coords]["in_loop"] = True
inside_cell_count = 0
inside_cell = False
prev_coord = (0, 0)
for x in range(0, len(lines[0])):
    for y in range(0, len(lines)):
        print(f"== ({x}, {y}) ==")
        if (x, y) == (0, 0):
            continue

        if (x, y) not in nodes:
            ic()
            if inside_cell:
                input(f"{inside_cell=}, {inside_cell_count=}")
                inside_cell_count += 1
            prev_coord = (x, y)
            continue
        
        node = nodes[(x, y)]
        print(f"{node=}")
        if "in_loop" in node:
            ic()
            if prev_coord not in node["connections"]:
                inside_cell = not inside_cell
            prev_coord = (x, y)
            continue

        if inside_cell:
            inside_cell_count += 1
        
        ic()
        prev_coord = (x, y)

print(inside_cell_count)

# print(max_node)

#pprint(nodes)
#cn = get_connected_nodes(start_node)
#pprint(cn)
#max_cl = max(cl)
#max_node = [k for k,v in nodes.items() if v["dist"] == max_cl]
#print_grid(nodes, max_node[0])

#print(max(cl), file=sys.stderr)
