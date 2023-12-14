import pathlib

path = pathlib.Path(__file__).parent.resolve()

# Part 1:
nice_strings = list()
with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        t1 = len([char for char in line if char in "aeiou"]) >= 3
        t2 = False
        for i in range(1, len(line)):
            if line[i] == line[i - 1]:
                t2 = True
        t3 = all(pair not in line for pair in ["ab", "cd", "pq", "xy"])

        if t1 and t2 and t3:
            nice_strings.append(line)

print(len(nice_strings))  # answer: 255


# Part 2:
nice_strings = list()
with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        t1 = False
        for i in range(1, len(line)):
            if line[i - 1 : i + 1] in line[i + 1 :]:
                t1 = True
                break
        t2 = False
        for i in range(0, len(line) - 2):
            if line[i] == line[i + 2]:
                t2 = True
                break

        if t1 and t2:
            nice_strings.append(line)

print(len(nice_strings))  # answer: 55
