import pathlib
from collections import defaultdict

sizes = defaultdict(int)
file_path = []

path = pathlib.Path(__file__).parent.resolve()
with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        if line.startswith("$ cd"):
            match (line):
                case "$ cd /\n":
                    file_path.clear()
                    file_path.append("/")
                case "$ cd ..\n":
                    file_path.pop()
                case _:
                    dir = line.split()[-1]
                    file_path.append(dir)
        else:
            if line.split()[0].isdigit():
                size = int(line.split()[0])
                for i in range(len(file_path)):
                    dir = "/".join(file_path[: i + 1]).replace("//", "/")
                    sizes[dir] += size

print(sum([size for size in sizes.values() if size < 100000]))  # answer: 1783610
needed_space = sizes["/"] - 40000000
print(min([size for size in sizes.values() if size > needed_space]))  # answer: 4370655
