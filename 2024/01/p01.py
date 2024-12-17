import pathlib

l1, l2 = [], []

path = pathlib.Path(__file__).parent.resolve()
with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        a, b = [int(li) for li in line.split()]
        l1.append(a)
        l2.append(b)

l1.sort()
l2.sort()
d = 0
s = 0
for i in range(len(l1)):
    d += abs(l1[i] - l2[i])
    if l1[i] in l2:
        for item in l2:
            if item == l1[i]:
                s += l1[i]
print(d)
print(s)
