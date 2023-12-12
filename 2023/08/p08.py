import math
import re

desert_map = dict()
with open("input.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        if i == 0:
            instructions = line.strip()
            instructions = [int(char == "R") for char in instructions]
        elif i == 1:
            pass
        else:
            ways = re.findall("\w+", line.split("= (")[1])
            desert_map[line.split(" ")[0]] = ways


# Part 1
steps = 0
current_node = "AAA"
while current_node != "ZZZ":
    for instruction in instructions:
        current_node = desert_map[current_node][instruction]
        steps += 1
        if current_node == "ZZZ":
            print(steps)  # answer: 18727
            break

# Part 2
steps = {node: 0 for node in desert_map.keys() if node[-1] == "A"}
for k in steps.keys():
    current_node = k
    while current_node[-1] != "Z":
        for instruction in instructions:
            current_node = desert_map[current_node][instruction]
            steps[k] += 1
            if current_node[-1] == "Z":
                break

print(math.lcm(*steps.values()))  # answer: 18024643846273
