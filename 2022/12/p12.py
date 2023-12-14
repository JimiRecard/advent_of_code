import pathlib

path = pathlib.Path(__file__).parent.resolve()
with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        print(line)
