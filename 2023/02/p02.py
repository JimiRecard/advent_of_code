import pathlib
import re

path = pathlib.Path(__file__).parent.resolve()

possible_games = []
powers = []
with open(f"{path}/input.txt", "r") as input:
    for game in input.readlines():
        r_num = max([int(num) for num in re.findall(r"(\d+) red", game)])
        g_num = max([int(num) for num in re.findall(r"(\d+) green", game)])
        b_num = max([int(num) for num in re.findall(r"(\d+) blue", game)])
        power = r_num * g_num * b_num
        powers.append(power)
        if r_num <= 12 and g_num <= 13 and b_num <= 14:
            game_num = int(re.findall(r"Game (\d+):", game)[0])
            possible_games.append(game_num)

print(sum(possible_games))  # answer: 2541
print(sum(powers))  # answer: 66016
