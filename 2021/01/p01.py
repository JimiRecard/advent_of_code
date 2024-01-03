import pathlib

times_increased_pt1 = 0
times_increased_pt2 = 0
depths = list()
depth_windows = list()
path = pathlib.Path(__file__).parent.resolve()

with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        depths.append(int(line))

for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        times_increased_pt1 += 1

for i in range(2, len(depths)):
    depth_windows.append(sum([depths[i], depths[i - 1], depths[i - 2]]))

for i in range(1, len(depth_windows)):
    if depth_windows[i] > depth_windows[i - 1]:
        times_increased_pt2 += 1

print(times_increased_pt1)  # answer: 1475
print(times_increased_pt2)  # answer: 1516
