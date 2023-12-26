
import sys

with open("2023/2/input", "r") as file:
    lines = [l.strip() for l in file.readlines()]

def valid_game(line, bounds):
    start = line.index(":")
    games = [g.strip() for g in line[start+1:].split(";")]
    
    for game in games:
        game_colors = game.split(", ")
        for gc in game_colors:
            num, color = gc.split(" ")
            if int(num) > bounds[color]:
                return False

    return True

bounds = {
    "red": 12,
    "green": 13,
    "blue": 14
}

gamesum = 0
for ix, line in enumerate(lines):
    if valid_game(line, bounds):
        gamesum += ix+1

print(gamesum, file=sys.stderr)
