import pathlib

sequences = list()


path = pathlib.Path(__file__).parent.resolve()
with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        sequences.append([int(num) for num in line.split(" ")])


def next_int(seq: list):
    diff_list = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    if any(diff_list):
        return seq[-1] + next_int(diff_list)
    else:
        return seq[-1]


def previous_int(seq: list):
    diff_list = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    if any(diff_list):
        return seq[0] - previous_int(diff_list)
    else:
        return seq[0]


extrapolated_values_right = list()
for sequence in sequences:
    extrapolated_values_right.append(next_int(sequence))

extrapolated_values_left = list()
for sequence in sequences:
    extrapolated_values_left.append(previous_int(sequence))

print(sum(extrapolated_values_right))  # answer: 1904165718
print(sum(extrapolated_values_left))  # answer: 964
