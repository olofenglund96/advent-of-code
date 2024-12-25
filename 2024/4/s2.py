import sys
import numpy as np
import aoclib

with open(f"/Users/olofenglund/code/advent-of-code/2024/4/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

grid = aoclib.convert_lines_into_grid(lines, dtype=str, split_fun=list)

xmas_count = 0
for i, j in np.argwhere(grid == "A"):
    adjacent_elems = aoclib.get_adjacent_elements(grid, i, j, depth=1)

    if (adjacent_elems[(-1,-1)] == ["M"] and adjacent_elems[(1,1)] == ["S"] or \
       adjacent_elems[(-1,-1)] == ["S"] and adjacent_elems[(1,1)] == ["M"]) and \
       (adjacent_elems[(-1,1)] == ["M"] and adjacent_elems[(1,-1)] == ["S"] or \
       adjacent_elems[(-1,1)] == ["S"] and adjacent_elems[(1,-1)] == ["M"]):
        xmas_count += 1

print(xmas_count, file=sys.stderr)
