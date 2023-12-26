import sys

with open(f"2023/6/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

def get_input_line(line):
    _line = line.split(":")[1]
    _line = _line.strip().split(" ")
    return int("".join(_line))

def race_distance(race_time, button_time):
    move_time = race_time - button_time

    return move_time * button_time

def print_race_outcome(race_time, button_time, record_dist, race_dist):
    print(f"Total RT: {race_time}, BT: {button_time}, TT: {race_time-button_time} -> Race distance: {race_dist} (record: {record_dist})")


def find_winning_race(race_time, record_dist, backwards=False):
    r = range(race_time)
    if backwards:
        r = range(race_time, 0, -1)

    for button_time in r:
        dist = race_distance(race_time, button_time)
        if dist > record_dist:
            #print(f"BT: {button_time} Won the race!")
            return button_time

        #print_race_outcome(race_time, button_time, record_dist, dist)

race_time = get_input_line(lines[0])
record_dist = get_input_line(lines[1])

start_win_time = find_winning_race(race_time, record_dist, backwards=False)
end_win_time = find_winning_race(race_time, record_dist, backwards=True)

prod = end_win_time-start_win_time + 1
#print(f"Race ({race_time}, {record_dist}) => {start_win_time} to {end_win_time}")


print(prod, file=sys.stderr)
