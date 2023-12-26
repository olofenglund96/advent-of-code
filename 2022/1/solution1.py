import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], ".."))

lines = []
with open("2022/1/input", "r") as file:
    lines = [l.strip() for l in file.readlines()]

max_elf_sum = 0
curr_sum = 0
for l in lines:
    if l == "":
        if curr_sum > max_elf_sum:
            max_elf_sum = curr_sum

        curr_sum = 0
        continue

    curr_sum += int(l)


print(max_elf_sum)
