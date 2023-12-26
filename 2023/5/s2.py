import sys
from pprint import pprint

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

pprint(maps)

locations = []

final_seeds = {}
for sstart, send in seeds:

    ranges = {(sstart, send): (sstart, send)}
    for key in keys:
        print(f"== {key} ==")
        next_ranges = {}
        for (s, e), (rs, re) in ranges.items():
            print(f"{rs} -> {re}")
            for dest, source, count in maps[key]:
                rend = source + count - 1
                print("--------")
                if re < source or rs > rend:
                    print(f"No overlap with {source} -> {rend}..")
                    #next_ranges.append((rs, re))
                    continue

                rs_offset = rs-source if rs > source else 0
                re_offset = rend-re if re < rend else 0
                rsf, ref = dest + rs_offset, dest + count - 1 - re_offset
                s, e = s + (source + rs_offset - rs), e - (re - (rend - re_offset))
                print(f"Overlap with {source} -> {rend}. Final range: {source + rs_offset} -> {source + count - 1 - re_offset}")
                print(f"Dest: {dest} -> {dest + count - 1}. Final dest range: {rsf} -> {ref}")
                print(f"{s=}, {e=}, {rs=}, {re=}, {rs_offset=}, {re_offset=}, {rend=}")
                next_ranges[(s, e)] = (rsf, ref)
                #print(f"{key} ~> old seed: {seed}, source: {source}, dest: {dest}, count: {count}, offset: {offset}, new seed: {dest + offset}")
        
        if len(next_ranges.keys()) > 0:
            ranges = next_ranges
    
    final_seeds[(s, e)] = ranges

#for dest, source, count in maps[key]:

print(seeds, final_seeds)

#print(min(locations), file=sys.stderr)
