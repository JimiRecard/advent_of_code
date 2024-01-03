import pathlib

path = pathlib.Path(__file__).parent.resolve()

# Part 1
h_pos, depth, aim = 0, 0, 0

with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        command, measure = line.strip().split(" ")
        match (command):
            case "forward":
                h_pos += int(measure)
            case "up":
                depth -= int(measure)
            case "down":
                depth += int(measure)

print(h_pos * depth)  # answer: 2073315


# Part 2
h_pos, depth, aim = 0, 0, 0

with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        command, measure = line.strip().split(" ")
        match (command):
            case "forward":
                h_pos += int(measure)
                depth += aim * int(measure)
            case "up":
                aim -= int(measure)
            case "down":
                aim += int(measure)

print(h_pos * depth)  # answer: 1840311528
