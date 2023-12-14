import pathlib
import re

path = pathlib.Path(__file__).parent.resolve()

wrapping_paper_areas = list()
ribbon_lengths = list()

with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        l, w, h = [int(num) for num in re.findall("\d+", line)]
        paper_area = 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
        wrapping_paper_areas.append(paper_area)
        ribbon_length = min(2 * l + 2 * w, 2 * w + 2 * h, 2 * h + 2 * l) + l * w * h
        ribbon_lengths.append(ribbon_length)


print(sum(wrapping_paper_areas))  # answer: 1598415
print(sum(ribbon_lengths))  # answer: 3812909
