import math
import re

symbols = {"+", "$", "%", "/", "*", "&", "-", "#", "=", "@"}
engine = []
parts = 0
gear_ratios = 0

with open("2023/3/input.txt", "r") as input:
    for line in input.readlines():
        engine.append(line.strip())

for i, line in enumerate(engine):
    # Part 1
    possible_parts_iter = re.finditer(r"\d+", line)
    for part_match in possible_parts_iter:
        left_index, right_index = part_match.span()
        right_index -= 1
        fix_left, fix_right = 0, 0
        if left_index > 0:
            left_index -= 1
        if right_index < len(line) - 1:
            right_index += 1
        if i == 0:
            adjacencies = "".join(
                [
                    line[left_index],
                    line[right_index],
                    engine[i + 1][left_index : right_index + 1],
                ]
            )
        elif i == 139:
            adjacencies = "".join(
                [
                    engine[i - 1][left_index : right_index + 1],
                    line[left_index],
                    line[right_index],
                ]
            )
        else:
            adjacencies = "".join(
                [
                    engine[i - 1][left_index : right_index + 1],
                    line[left_index],
                    line[right_index],
                    engine[i + 1][left_index : right_index + 1],
                ]
            )
        if any(symbol in adjacencies for symbol in symbols):
            parts += int(part_match.group())

    # Part 2
    possible_gears_iter = re.finditer("\*", line)
    for gear_match in possible_gears_iter:
        index = gear_match.start()
        left_index = 0 if index <= 2 else index - 3
        right_index = 139 if index >= 136 else index + 3
        up, down = [], []
        if i != 0:
            if engine[i - 1][index].isdigit():
                up_matches = re.finditer("\d+", engine[i - 1][index - 2 : index + 3])
                for up_match in up_matches:
                    if 2 >= up_match.span()[0] and 3 <= up_match.span()[1]:
                        up = [up_match.group()]
            else:
                up = re.findall("\d+$", engine[i - 1][left_index:index]) + re.findall(
                    "^\d+", engine[i - 1][index + 1 : right_index + 1]
                )
        if i != 139:
            if engine[i + 1][index].isdigit():
                down_matches = re.finditer("\d+", engine[i + 1][index - 2 : index + 3])
                for down_match in down_matches:
                    if 2 >= down_match.span()[0] and 3 <= down_match.span()[1]:
                        down = [down_match.group()]
            else:
                down = re.findall("\d+$", engine[i + 1][left_index:index]) + re.findall(
                    "^\d+", engine[i + 1][index + 1 : right_index + 1]
                )
        left = re.findall("\d+$", line[left_index:index])
        right = re.findall("^\d+", line[index + 1 : right_index + 1])
        numbers = up + down + left + right
        numbers = [int(num) for num in numbers]
        if len(numbers) > 1:
            gear_ratios += math.prod(numbers)


print(parts)  # answer: 527369
print(gear_ratios)  # answer: 73074886
