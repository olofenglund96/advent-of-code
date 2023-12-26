import sys
from pprint import pprint
from tqdm import tqdm

with open(f"2023/11/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

universe = []

for line in lines:
    cells = list(line)
    universe.append(cells)

empty_cols = []
empty_rows = []

col_galaxy_count = [0]*len(universe[0])
for i, row in enumerate(universe):
    if len(set(row)) == 1:
        empty_rows.append(i)
    
    for j, cell in enumerate(row):
        if cell == "#":
            col_galaxy_count[j] += 1

empty_cols = [i for i, cgc in enumerate(col_galaxy_count) if cgc == 0]


mul = 1000000-1

# for row in universe:
#     print("".join(row))

galaxies = []
for i, row in enumerate(universe):
    for j, cell in enumerate(row):
        if cell == "#":
            galaxies.append((i, j))

galaxy_distances = {}

def calc_dist(i1, i2, mul, comp):
    r = range(i1, i2)

    if i1 > i2:
        r = range(i2, i1)
    
    dist = abs(i2 - i1)
    for k in r:
        #print(f"{k=}, {dist=}")
        if k in comp:
            dist += mul
            #print("adding mul")

    return dist

for i, (x1, y1) in enumerate(galaxies):
    for j, (x2, y2) in enumerate(galaxies):
        if (i, j) in galaxy_distances or (j, i) in galaxy_distances or i == j:
            continue

        
        #print(f"distx calc {x1=}, {x2=}, {empty_rows=}")
        distx = calc_dist(x1, x2, mul, empty_rows)

        #print(f"disty calc {y1=}, {y2=}, {empty_cols=}")
        disty = calc_dist(y1, y2, mul, empty_cols)
        
        galaxy_distances[(i, j)] = distx + disty
        
        #input(f"({i}, {j}) -> {distx} + {disty} = {distx + disty}")

#print(len(galaxy_distances.keys()))
#pprint(galaxy_distances)

print(sum(galaxy_distances.values()), file=sys.stderr)
