import sys

with open("2023/1/input", "r") as file:
    lines = [l.strip() for l in file.readlines()]

digit_strs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

nums = []
for line in lines:
    first_num, first_idx, last_num, last_idx = None, 1000, None, 0
    chars = list(line)

    for i, c in enumerate(chars):
        if c.isdigit():
            if first_num is None:
                first_num = c
                first_idx = i

            last_num = c
            last_idx = i

    for i, ds in enumerate(digit_strs):
        if ds in line:
            fix = line.index(ds)
            lix = line.rfind(ds)
            if fix < first_idx:
                first_num = i+1
                first_idx = fix
            
            if lix > last_idx:
                last_num = i+1
                last_idx = lix


    num = int(f"{first_num}{last_num}")
    nums.append(num)

print(f"Tot: {sum(nums)}")
print(sum(nums), file=sys.stderr)