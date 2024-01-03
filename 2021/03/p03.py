import pathlib
import statistics

path = pathlib.Path(__file__).parent.resolve()
avg_bits = list()
first = True

with open(f"{path}/input.txt", "r") as file:
    file = file.readlines()
    file = [line.strip() for line in file]

size = len(file)

for line in file:
    if first:
        first = False
        avg_bits = [0 for i in range(len(line))]
    for i in range(len(line)):
        avg_bits[i] += int(line[i])

gamma_rate = [int(bit / size > 0.5) for bit in avg_bits]
epsilon_rate = [abs(1 - bit) for bit in gamma_rate]
gamma_rate = sum(
    [gamma_rate[i] * 2 ** (len(gamma_rate) - 1 - i) for i in range(len(gamma_rate))]
)
epsilon_rate = sum(
    [
        epsilon_rate[i] * 2 ** (len(epsilon_rate) - 1 - i)
        for i in range(len(epsilon_rate))
    ]
)

print(gamma_rate * epsilon_rate)  # answer: 3549854

file_o2 = file
file_co2 = file

for i in range(len(file_o2[0])):
    if len(file_o2) > 1:
        avg = statistics.mean([int(file_o2[j][i]) for j in range(len(file_o2))])
        avg = str(int(avg >= 0.5))
        file_o2 = [line for line in file_o2 if line[i] == avg]

o2_rate = sum(
    int(file_o2[0][i]) * 2 ** (len(file_o2[0]) - 1 - i) for i in range(len(file_o2[0]))
)

for i in range(len(file_co2[0])):
    if len(file_co2) > 1:
        avg = statistics.mean([int(file_co2[j][i]) for j in range(len(file_co2))])
        avg = str(int(avg < 0.5))
        file_co2 = [line for line in file_co2 if line[i] == avg]

co2_rate = sum(
    int(file_co2[0][i]) * 2 ** (len(file_co2[0]) - 1 - i)
    for i in range(len(file_co2[0]))
)

print(o2_rate * co2_rate)  # answer: 3765399
