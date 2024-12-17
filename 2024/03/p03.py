import pathlib
import re


m1 = 0
m2 = 0
do = True
path = pathlib.Path(__file__).parent.resolve()
with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        muls = re.findall(r"(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)", line)
        for mul in muls:
            # part 1
            if mul[2]:
                m1 += int(mul[2]) * int(mul[3])

            # part 1
            if mul[1]:
                do = False
            elif mul[0]:
                do = True
            elif do:
                m2 += int(mul[2]) * int(mul[3])
print(m1)
print(m2)
