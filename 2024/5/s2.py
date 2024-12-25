import sys
from pprint import pprint
from collections import defaultdict

def get_swap_ixs(mapping, series):
    for i, elem in enumerate(series):
        elem_deps = mapping[elem]
        for j, dep in enumerate(series[i+1:]):
            if dep not in elem_deps:
                return i, i+j+1

    return -1, -1

def reorder_list(mapping, series):
    already_valid = True
    swapped_series = series
    while True:
        swap_i, swap_j = get_swap_ixs(mapping, swapped_series)
        if swap_i == -1 and swap_j == -1:
            return already_valid, swapped_series

        already_valid = False
        saved_elem = swapped_series[swap_i]
        swapped_series[swap_i] = swapped_series[swap_j]
        swapped_series[swap_j] = saved_elem


with open(f"/Users/olofenglund/code/advent-of-code/2024/5/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

mapping = defaultdict(list)
series = []
for line in lines:
    if "|" in line:
        start, end = line.split("|")
        mapping[start].append(end)
    elif "," in line:
        series.append(line.split(","))

ok_middle_pages = []
for serie in series:
    already_valid, reordered_list = reorder_list(mapping, serie)
    if already_valid:
        continue

    ok_middle_pages.append(int(serie[len(reordered_list)//2]))


print(ok_middle_pages)


print(sum(ok_middle_pages), file=sys.stderr)
