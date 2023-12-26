import sys
from pprint import pprint

with open(f"2023/9/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]


def calc_seq_diff(seq):
    diffs = []
    for i in range(0, len(seq)-1):
        diffs.append(seq[i+1] - seq[i])

    #print(f"{seq=}, {diffs=}")
    return diffs


def compute_next_num(seq):
    all_diffs = [seq]
    diffs = calc_seq_diff(seq)
    all_diffs.append(diffs)
    while diffs[-1] != 0:
        diffs = calc_seq_diff(diffs)
        all_diffs.append(diffs)
    
    #print(f"{all_diffs=}")
    sumnum = 0
    for diff in all_diffs[::-1]:
        sumnum = diff[0] - sumnum
        #print(f"{diff=}, {sumnum=}")

    #print(f"Got sumnum {sumnum} for {seq=}")

    return sumnum
        

seqs = []
for line in lines:
    seqs.append([int(l) for l in line.split(" ")])


sumnums = []
for seq in seqs:
    sumnums.append(compute_next_num(seq))


print(sum(sumnums), file=sys.stderr)
