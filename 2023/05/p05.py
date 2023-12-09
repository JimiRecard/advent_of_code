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
        self.origin_initial = input_values[1]
        self.origin_final = input_values[1] + input_values[2]
        self.destination_initial = input_values[0]
        self.destination_final = input_values[0] + input_values[2]

    def __len__(self):
        return self.origin_final - self.origin_initial

    def __str__(self):
        return (
            f"({self.origin_initial}, {self.origin_final}):"
            f" ({self.destination_initial}, {self.destination_final})"
        )

    def __repr__(self):
        return (
            f"({self.origin_initial}, {self.origin_final}):"
            f" ({self.destination_initial}, {self.destination_final})"
        )

    def __eq__(self, other):
        return (
            self.destination_initial == other.destination_initial
            and self.destination_final == other.destination_final
        )

    def __lt__(self, other):
        return self.destination_initial < other.destination_initial

    def __le__(self, other):
        return self.destination_initial <= other.destination_initial

    def __ne__(self, other):
        return (
            self.destination_initial != other.destination_initial
            or self.destination_final != other.destination_final
        )

    def __gt__(self, other):
        return self.destination_initial > other.destination_initial

    def __ge__(self, other):
        return self.destination_initial >= other.destination_initial

    def __add__(self, other):
        if (
            self.destination_initial == other.origin_initial
            and self.destination_final == other.origin_final
        ):
            return Interval(
                f"{other.destination_initial} {self.origin_initial} {len(self)}"
            )
        else:
            raise IndexError

    def overlaps(self, other):
        return (
            self.destination_initial in range(other.origin_initial, other.origin_final)
            or self.destination_final - 1
            in range(other.origin_initial, other.origin_final)
            or other.origin_initial
            in range(self.destination_initial, self.destination_final)
            or other.origin_final - 1
            in range(self.destination_initial, self.destination_final)
        )

    def split_origin(self, num):
        if num in range(self.origin_initial, self.origin_final):
            i1 = Interval(
                f"{self.destination_initial} {self.origin_initial} {num - self.origin_initial}"
            )
            i2 = Interval(
                f"{self.destination_initial + num - self.origin_initial} {num} {self.origin_final - num}"
            )
            return [i1, i2]

    def split_destination(self, num):
        if num in range(self.destination_initial, self.destination_final):
            i1 = Interval(
                f"{self.destination_initial} {self.origin_initial} {num - self.destination_initial}"
            )
            i2 = Interval(
                f"{num} {self.origin_initial + num - self.destination_initial} {self.destination_final - num}"
            )
            return [i1, i2]

    def translate(self, num):
        if num in range(self.origin_initial, self.origin_final):
            return num + self.destination_initial - self.origin_initial
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
                if i3.origin_initial == i1.destination_initial:
                    if i3.origin_final == i1.destination_final:
                        intervals3.append(i1 + i3)
                    elif i3.origin_final < i1.destination_final:
                        j1, j2 = i1.split_destination(i3.origin_final)
                        intervals3.append(j1 + i3)
                        intervals1.append(j2)
                    else:
                        j3, j4 = i3.split_origin(i1.destination_final)
                        intervals3.append(i1 + j3)
                        intervals2.append(j4)
                elif i3.origin_initial < i1.destination_initial:
                    if i3.origin_final == i1.destination_final:
                        j3, j4 = i3.split_origin(i1.destination_initial)
                        intervals3.append(i1 + j4)
                        intervals2.append(j3)
                    elif i3.origin_final < i1.destination_final:
                        j1, j2 = i1.split_destination(i3.origin_final)
                        j3, j4 = i3.split_origin(i1.destination_initial)
                        intervals3.append(j1 + j4)
                        intervals1.append(j2)
                        intervals2.append(j3)
                    else:
                        j3, j4 = i3.split_origin(i1.destination_initial)
                        j4, j5 = j4.split_origin(i1.destination_final)
                        intervals3.append(i1 + j4)
                        intervals2.append(j3)
                        intervals2.append(j5)
                else:
                    if i3.origin_final == i1.destination_final:
                        j1, j2 = i1.split_destination(i3.origin_initial)
                        intervals1.append(j1)
                        intervals3.append(j2 + i3)
                    elif i3.origin_final < i1.destination_final:
                        j0, j1 = i1.split_destination(i3.origin_initial)
                        j1, j2 = j1.split_destination(i3.origin_final)
                        intervals1.append(j0)
                        intervals3.append(j1 + i3)
                        intervals1.append(j2)
                    else:
                        j1, j2 = i1.split_destination(i3.origin_initial)
                        j3, j4 = i3.split_origin(i1.destination_final)
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
        if seed in range(interval.origin_initial, interval.origin_final):
            final_locations_part1.append(interval.translate(seed))

    for sr in seed_ranges:
        if sr[0] in range(interval.origin_initial, interval.origin_final):
            final_locations.append(interval.translate(sr[0]))
        elif sr[0] < interval.origin_initial and sr[1] > interval.origin_initial:
            final_locations.append(interval.translate(interval.origin_initial))

print(min(final_locations_part1))  # answer: 525792406
print(min(final_locations))  # answer: 79004094
