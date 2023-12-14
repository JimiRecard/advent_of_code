import pathlib

path = pathlib.Path(__file__).parent.resolve()

floor = 0
first = True
with open(f"{path}/input.txt", "r") as file:
    for i, char in enumerate(file.read()):
        if char == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1 and first:
            first = False
            print(i + 1)  # answer Part 2: 1795

print(floor)  # answer Part 1: 74
