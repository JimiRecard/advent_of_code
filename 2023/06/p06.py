import math
import pathlib
import re
from dataclasses import dataclass


@dataclass
class Race:
    time: int
    distance: int


# Part 1

path = pathlib.Path(__file__).parent.resolve()
with open(f"{path}/input.txt", "r") as file:
    times = [int(time) for time in re.findall(r"\d+", file.readline())]
    distances = [int(distance) for distance in re.findall(r"\d+", file.readline())]


possible_ways = list()

for i in range(len(times)):
    race = Race(times[i], distances[i])
    delta = math.sqrt(race.time**2 - 4 * race.distance)
    min_time = math.floor((race.time - delta) / 2 + 1)
    max_time = math.ceil((race.time + delta) / 2 - 1)
    possible_ways.append(max_time - min_time + 1)

print(math.prod(possible_ways))  # answer: 160816


# Part 2
time = int("".join(str(time) for time in times))
distance = int("".join(str(distance) for distance in distances))
race = Race(time, distance)
delta = math.sqrt(race.time**2 - 4 * race.distance)
min_time = math.floor((race.time - delta) / 2 + 1)
max_time = math.ceil((race.time + delta) / 2 - 1)

print(max_time - min_time + 1)  # answer 46561107
