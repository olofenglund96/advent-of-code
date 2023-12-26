
import sys

with open("2023/2/input", "r") as file:
    lines = [l.strip() for l in file.readlines()]

def min_colors(line):
    start = line.index(":")
    games = [g.strip() for g in line[start+1:].split(";")]
    min_colors = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for game in games:
        game_colors = game.split(", ")
        for gc in game_colors:
            num, color = gc.split(" ")
            if int(num) > min_colors[color]:
                min_colors[color] = int(num)

    mult = 1
    for cv in min_colors.values():
        mult *= cv

    return mult



gamesum = 0
for ix, line in enumerate(lines):
    gamesum += min_colors(line)

print(gamesum, file=sys.stderr)
