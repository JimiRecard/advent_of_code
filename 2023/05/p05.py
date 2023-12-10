import re
from collections import deque

# Part 1
map_instructions = dict()

with open("input.txt", "r") as file:
    current_map = ""
    for i, line in enumerate(file.readlines()):
        if i == 0:
            seeds = [int(num) for num in line.split(": ")[1].strip().split(" ")]

        else:
            if line == "\n":
                pass
            elif "map:" in line:
                current_map = line.split(" map:")[0]
                map_instructions[current_map] = list()
            else:
                map_instructions[current_map].append(
                    [int(num) for num in line.split(" ")]
                )

locations = []
for seed in seeds:
    destination = seed
    for k, v in map_instructions.items():
        for v1 in v:
            if destination in range(v1[1], v1[1] + v1[2]):
                destination = destination - v1[1] + v1[0]
                break
    locations.append(destination)


print(min(locations))  # answer: 525792406


# Part 2
class Interval:
    def __init__(self, input: str):
        input_values = [int(num) for num in input.split(" ")]
        self.origin_left = input_values[1]
        self.origin_right = input_values[1] + input_values[2]
        self.destination_left = input_values[0]
        self.destination_right = input_values[0] + input_values[2]

    def __len__(self):
        return self.origin_right - self.origin_left

    def __str__(self):
        return (
            f"({self.origin_left}, {self.origin_right}):"
            f" ({self.destination_left}, {self.destination_right})"
        )

    def __repr__(self):
        return (
            f"({self.origin_left}, {self.origin_right}):"
            f" ({self.destination_left}, {self.destination_right})"
        )

    def __eq__(self, other):
        return (
            self.destination_left == other.destination_left
            and self.destination_right == other.destination_right
        )

    def __lt__(self, other):
        return self.destination_left < other.destination_left

    def __le__(self, other):
        return self.destination_left <= other.destination_left

    def __ne__(self, other):
        return (
            self.destination_left != other.destination_left
            or self.destination_right != other.destination_right
        )

    def __gt__(self, other):
        return self.destination_left > other.destination_left

    def __ge__(self, other):
        return self.destination_left >= other.destination_left

    def __add__(self, other):
        if (
            self.destination_left == other.origin_left
            and self.destination_right == other.origin_right
        ):
            return Interval(f"{other.destination_left} {self.origin_left} {len(self)}")
        else:
            raise IndexError

    def overlaps(self, other):
        return (
            self.destination_left in range(other.origin_left, other.origin_right)
            or self.destination_right - 1
            in range(other.origin_left, other.origin_right)
            or other.origin_left in range(self.destination_left, self.destination_right)
            or other.origin_right - 1
            in range(self.destination_left, self.destination_right)
        )

    def split_origin(self, num):
        if num in range(self.origin_left, self.origin_right):
            i1 = Interval(
                f"{self.destination_left} {self.origin_left} {num - self.origin_left}"
            )
            i2 = Interval(
                f"{self.destination_left + num - self.origin_left} {num} {self.origin_right - num}"
            )
            return [i1, i2]

    def split_destination(self, num):
        if num in range(self.destination_left, self.destination_right):
            i1 = Interval(
                f"{self.destination_left} {self.origin_left} {num - self.destination_left}"
            )
            i2 = Interval(
                f"{num} {self.origin_left + num - self.destination_left} {self.destination_right - num}"
            )
            return [i1, i2]

    def translate(self, num):
        if num in range(self.origin_left, self.origin_right):
            return num + self.destination_left - self.origin_left
        else:
            return None


all_maps: deque[list[Interval]] = deque()

with open("input.txt", "r") as file:
    current_map = ""
    for i, line in enumerate(file.readlines()):
        if i == 0:
            seed_ranges = [
                (int(r[0]), int(r[0]) + int(r[1]))
                for r in re.findall("(\d+) (\d+)", line)
            ]

        else:
            if line == "\n":
                pass
            elif "map:" in line:
                all_maps.append(list())
            else:
                all_maps[-1].append(Interval(line))


while len(all_maps) > 1:
    intervals1 = all_maps.popleft()
    intervals2 = all_maps.popleft()
    intervals3 = list()
    while any(
        origin.overlaps(destination)
        for origin in intervals1
        for destination in intervals2
    ):
        i1 = intervals1.pop(0)
        for i2 in intervals2:
            if i1.overlaps(i2):
                i3 = intervals2.pop(intervals2.index(i2))
                if i3.origin_left == i1.destination_left:
                    if i3.origin_right == i1.destination_right:
                        intervals3.append(i1 + i3)
                    elif i3.origin_right < i1.destination_right:
                        j1, j2 = i1.split_destination(i3.origin_right)
                        intervals3.append(j1 + i3)
                        intervals1.append(j2)
                    else:
                        j3, j4 = i3.split_origin(i1.destination_right)
                        intervals3.append(i1 + j3)
                        intervals2.append(j4)
                elif i3.origin_left < i1.destination_left:
                    if i3.origin_right == i1.destination_right:
                        j3, j4 = i3.split_origin(i1.destination_left)
                        intervals3.append(i1 + j4)
                        intervals2.append(j3)
                    elif i3.origin_right < i1.destination_right:
                        j1, j2 = i1.split_destination(i3.origin_right)
                        j3, j4 = i3.split_origin(i1.destination_left)
                        intervals3.append(j1 + j4)
                        intervals1.append(j2)
                        intervals2.append(j3)
                    else:
                        j3, j4 = i3.split_origin(i1.destination_left)
                        j4, j5 = j4.split_origin(i1.destination_right)
                        intervals3.append(i1 + j4)
                        intervals2.append(j3)
                        intervals2.append(j5)
                else:
                    if i3.origin_right == i1.destination_right:
                        j1, j2 = i1.split_destination(i3.origin_left)
                        intervals1.append(j1)
                        intervals3.append(j2 + i3)
                    elif i3.origin_right < i1.destination_right:
                        j0, j1 = i1.split_destination(i3.origin_left)
                        j1, j2 = j1.split_destination(i3.origin_right)
                        intervals1.append(j0)
                        intervals3.append(j1 + i3)
                        intervals1.append(j2)
                    else:
                        j1, j2 = i1.split_destination(i3.origin_left)
                        j3, j4 = i3.split_origin(i1.destination_right)
                        intervals1.append(j1)
                        intervals3.append(j2 + j3)
                        intervals2.append(j4)
                break
        else:
            intervals3.append(i1)
    intervals3 += intervals1
    intervals3 += intervals2
    all_maps.appendleft(intervals3)

final_locations_part1 = list()
final_locations = list()


for interval in sorted(all_maps[0]):
    for seed in seeds:
        if seed in range(interval.origin_left, interval.origin_right):
            final_locations_part1.append(interval.translate(seed))

    for sr in seed_ranges:
        if sr[0] in range(interval.origin_left, interval.origin_right):
            final_locations.append(interval.translate(sr[0]))
        elif sr[0] < interval.origin_left and sr[1] > interval.origin_left:
            final_locations.append(interval.translate(interval.origin_left))

print(min(final_locations_part1))  # answer: 525792406
print(min(final_locations))  # answer: 79004094
