import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], ".."))

lines = []
with open("2022/1/input", "r") as file:
    lines = [l.strip() for l in file.readlines()]

elf_sums = []
curr_sum = 0
for l in lines:
    if l == "":
        elf_sums.append(curr_sum)
        curr_sum = 0
        continue

    curr_sum += int(l)


sum_sorted = sorted(elf_sums)

print(sum(sum_sorted[-3:]))
