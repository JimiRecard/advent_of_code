import pathlib

cycle = 0
x = 1
display = [[" " for i in range(40)] for j in range(6)]
signal_strength = 0


def write_display(cycle, x, display):
    if (cycle % 40) in [x - 1, x, x + 1]:
        display[cycle // 40][cycle % 40] = "#"


path = pathlib.Path(__file__).parent.resolve()
with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        op = line.split()[0]
        write_display(cycle, x, display)
        cycle += 1
        write_display(cycle, x, display)
        if cycle % 40 == 20:
            signal_strength += cycle * x
        if op == "addx":
            cycle += 1
            if cycle % 40 == 20:
                signal_strength += cycle * x
            x += int(line.split()[1])

print(signal_strength)  # answer: 13220

for line in display:
    print("".join(line))  # answer: RUAKHBEK
