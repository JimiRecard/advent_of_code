import pathlib
import re

xmas = 0
x_mas = 0
path = pathlib.Path(__file__).parent.resolve()
matrix = []

# ↔️
with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        matrix.append(line.rstrip("\n"))

        xmas += len(re.findall("XMAS", line))
        xmas += len(re.findall("SAMX", line))

# ↕️
transpose = ["".join(list(row)) for row in zip(*matrix)]
for line in transpose:
    xmas += len(re.findall("XMAS", line))
    xmas += len(re.findall("SAMX", line))

# ↖️↘️
for i in range(0, len(matrix) - 3):
    for j in range(0, len(matrix[0]) - 3):
        if (
            matrix[i][j] == "X"
            and matrix[i + 1][j + 1] == "M"
            and matrix[i + 2][j + 2] == "A"
            and matrix[i + 3][j + 3] == "S"
        ) or (
            matrix[i][j] == "S"
            and matrix[i + 1][j + 1] == "A"
            and matrix[i + 2][j + 2] == "M"
            and matrix[i + 3][j + 3] == "X"
        ):
            xmas += 1

# ↙️↗️
for i in range(3, len(matrix)):
    for j in range(0, len(matrix[0]) - 3):
        if (
            matrix[i][j] == "X"
            and matrix[i - 1][j + 1] == "M"
            and matrix[i - 2][j + 2] == "A"
            and matrix[i - 3][j + 3] == "S"
        ) or (
            matrix[i][j] == "S"
            and matrix[i - 1][j + 1] == "A"
            and matrix[i - 2][j + 2] == "M"
            and matrix[i - 3][j + 3] == "X"
        ):
            xmas += 1

# part 2
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[0]) - 1):
        if matrix[i][j] == "A":
            if (
                (matrix[i - 1][j - 1] == "S" and matrix[i + 1][j + 1] == "M")
                or (matrix[i - 1][j - 1] == "M" and matrix[i + 1][j + 1] == "S")
            ) and (
                (matrix[i - 1][j + 1] == "S" and matrix[i + 1][j - 1] == "M")
                or (matrix[i - 1][j + 1] == "M" and matrix[i + 1][j - 1] == "S")
            ):
                x_mas += 1

print(xmas)
print(x_mas)
