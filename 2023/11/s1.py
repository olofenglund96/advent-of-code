import sys
from pprint import pprint

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

offset = 0
for er in empty_rows:
    eri = er + offset
    offset += 1
    universe = universe[:eri] + [["."]*len(universe[0])] + universe[eri:]

offset = 0
for ec in empty_cols:
    eci = ec + offset
    offset += 1
    for row in universe:
        row.insert(eci, ".")


galaxies = []
for i, row in enumerate(universe):
    for j, cell in enumerate(row):
        if cell == "#":
            galaxies.append((i, j))

galaxy_distances = {}

interesting_galaxies = [(0, 3)]

pprint(galaxies)

for i, (x1, y1) in enumerate(galaxies):
    for j, (x2, y2) in enumerate(galaxies):
        if (i, j) in galaxy_distances or (j, i) in galaxy_distances or i == j:
            continue
        dist = abs(x1 - x2) + abs(y1 - y2)

        galaxy_distances[(i, j)] = dist

        print(f"({x1=}, {x2=}), ({y1=}, {y2=})")
        input(f"({i}, {j}) -> {abs(x1 - x2)} + {abs(y1 - y2)} = {dist}")

with open("./saveg.txt", "w") as file:
    [file.write(f"{str(v)}\n") for v in galaxy_distances.values()]

print(sum(galaxy_distances.values()), file=sys.stderr)
