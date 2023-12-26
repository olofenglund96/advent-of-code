import sys
from pprint import pprint

with open(f"2023/12/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

cases = []
for line in lines:
    springs, conditions = line.split(" ")
    conditions = [int(c) for c in conditions.split(",")]

    cases.append((springs, conditions))

combinations = []

for springs, conditions in cases:
    count, done = compute_combinations(springs, conditions)


print(lines[-1], file=sys.stderr)


def compute_combinations(springs, conditions):
    offset = 0

    for c in springs[offset:]:
        pass
