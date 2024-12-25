import sys
from pprint import pprint
from collections import defaultdict

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
    ok_series = True
    for i, elem in enumerate(serie):
        if any(dep not in mapping[elem] for dep in serie[i+1:]):
            ok_series = False
            break

    if ok_series:
        ok_middle_pages.append(int(serie[len(serie)//2]))

print(ok_middle_pages)


print(sum(ok_middle_pages), file=sys.stderr)
