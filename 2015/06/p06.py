import pathlib
import re

path = pathlib.Path(__file__).parent.resolve()

# Part 1:
light_grid = [[False for i in range(1000)] for j in range(1000)]
with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        c1, c2 = [
            [int(num[0]), int(num[1])] for num in re.findall(r"(\d+),(\d+)", line)
        ]
        for i in range(c1[0], c2[0] + 1):
            for j in range(c1[1], c2[1] + 1):
                if "toggle" in line:
                    light_grid[i][j] = not light_grid[i][j]
                elif "on" in line:
                    light_grid[i][j] = True
                else:
                    light_grid[i][j] = False

lights_on = sum([sum(line) for line in light_grid])
print(lights_on)  # answer: 543903

# Part 2:
light_grid = [[0 for i in range(1000)] for j in range(1000)]
with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        c1, c2 = [
            [int(num[0]), int(num[1])] for num in re.findall(r"(\d+),(\d+)", line)
        ]
        for i in range(c1[0], c2[0] + 1):
            for j in range(c1[1], c2[1] + 1):
                if "toggle" in line:
                    light_grid[i][j] += 2
                elif "on" in line:
                    light_grid[i][j] += 1
                else:
                    if light_grid[i][j] > 0:
                        light_grid[i][j] -= 1

lights_on = sum([sum(line) for line in light_grid])
print(lights_on)  # answer: 14190930
