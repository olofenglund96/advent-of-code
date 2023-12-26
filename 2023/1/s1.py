import sys

with open("2023/1/input", "r") as file:
    lines = [l.strip() for l in file.readlines()]


nums = []
for line in lines:
    first_num, last_num = None, None
    chars = list(line)

    for c in chars:
        if c.isdigit():
            if first_num is None:
                first_num = c

            last_num = c
        
    num = int(f"{first_num}{last_num}")
    nums.append(num)

print(f"Tot: {sum(nums)}")
print(sum(nums), file=sys.stderr)