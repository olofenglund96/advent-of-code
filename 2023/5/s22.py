import sys
from pprint import pprint
from collections import defaultdict
from icecream import ic

with open(f"2023/5/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

seeds_str = lines[0].split(":")[1]
seeds_t = [int(s) for s in seeds_str.split(" ") if s != ""]

seeds = []
for i in range(0, len(seeds_t), 2):
    st = seeds_t[i]
    sr = (st, st+seeds_t[i+1]-1)
    seeds.append(sr)

print(f"sl: {seeds}")

maps = {}
keys = []
for line in lines[1:]:
    if "map:" in line:
        key = line.split(" map:")[0].strip()
        maps[key] = []
        keys.append(key)
        continue

    if line.strip() == "":
        continue

    maps[keys[-1]].append([int(n) for n in line.strip().split(" ")])


def combine_layer(mappings, layer):
    combined_mapping = {}
    new_mappings = mappings
    while len(new_mappings) > 0:
        mv_lower, mv_upper = new_mappings.pop()
        overlap = False
        ic()
        for tk, tv in layer.items():
            tk_lower, tk_upper = tk
            tv_lower, tv_upper = tv
            ic()
            if mv_upper < tk_lower or mv_lower > tk_upper: # no overlap
                continue
            
            overlap = True
            if mv_lower < tk_lower:
                new_mappings.append((mv_lower, tk_lower))
            
            if mv_upper > tk_upper:
                new_mappings.append((tk_upper, mv_upper))
            ic()
            if mv_lower < tk_lower and mv_upper > tk_upper: # cover
                combined_mapping[(tk_lower, tk_upper)] = (tv_lower, tv_upper)
                continue
            ic()
            if mv_lower < tk_lower and mv_upper < tk_upper: # lower cover
                diff = mv_upper - tk_lower
                combined_mapping[(tk_lower, mv_upper)] = (tv_lower, tv_lower + diff)
                continue
            ic()
            if mv_lower > tk_lower and mv_upper > tk_upper: # upper cover
                diff = tk_upper - mv_lower
                combined_mapping[(mv_lower, tk_upper)] = (tv_upper - diff, tv_upper)
                continue
            ic()
            if mv_lower > tk_lower and mv_upper < tk_upper: # inside
                diffl = tk_lower - mv_lower
                diffu = tk_upper - mv_upper
                combined_mapping[(mv_lower, mv_upper)] = (tv_lower + diff, tv_upper - diffu)
                continue
            ic()
        
        if not overlap:
            ic()
            combined_mapping[(mv_lower, mv_upper)] = (mv_lower, mv_upper)
            
    return combined_mapping

def flatten(layerf, layert):
    layerc = {}

    print(f"Layer From: {layerf}")
    print(f"Layer To: {layert}")

    for keyf, lf in layerf.items():
        new_layer_map = combine_layer([lf], layert)
        print(f"Layer Combined: {new_layer_map}")
        input()


pprint(maps)

maps_ranges = defaultdict(dict)
for key, ranges in maps.items():
    for r in ranges:
        maps_ranges[key][(r[1], r[1] + r[2])] = (r[0], r[0] + r[2])

for k in keys:
    print(f"== {k} ==")
    pprint(maps_ranges[k])

flattened_map = {}
for i in range(len(keys)-1, 0, -1):
    from_layer = maps_ranges[keys[i-1]]
    to_layer = maps_ranges[keys[i]]

    flatten(from_layer, to_layer)

# == temperature-to-humidity ==
# {(0, 69): (1, 70), (69, 70): (0, 1)}
# == humidity-to-location ==
# {(56, 93): (60, 97), (93, 97): (56, 60)}

