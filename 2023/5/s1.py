import sys
from pprint import pprint

with open(f"2023/5/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

seeds_str = lines[0].split(":")[1]
seeds = [int(s) for s in seeds_str.split(" ") if s != ""]

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

#pprint(maps)

locations = []
for seed in seeds:
    #print(f"== seed: {seed} ==")
    for key in keys:
        for dest, source, count in maps[key]:
            if seed < source or seed > source + count-1:
                continue
            
            offset = seed - source
            #print(f"{key} ~> old seed: {seed}, source: {source}, dest: {dest}, count: {count}, offset: {offset}, new seed: {dest + offset}")
            seed = dest + offset
            break

    #input()
    locations.append(seed)


print(min(locations), file=sys.stderr)
