import pathlib

path = pathlib.Path(__file__).parent.resolve()
with open(f"{path}/input.txt", "r") as file:
    fully_contained_elfs = 0
    overlapping_elfs = 0
    for i, line in enumerate(file.read().split("\n")):
        elf1_text = line.split(",")[0]
        elf1 = [int(num) for num in elf1_text.split("-")]
        elf2_text = line.split(",")[1]
        elf2 = [int(num) for num in elf2_text.split("-")]
        if (
            elf1[0] <= elf2[0]
            and elf1[1] >= elf2[1]
            or elf1[0] >= elf2[0]
            and elf1[1] <= elf2[1]
        ):
            fully_contained_elfs += 1
        if (
            elf1[0] <= elf2[0]
            and elf1[1] >= elf2[1]
            or elf1[0] >= elf2[0]
            and elf1[1] <= elf2[1]
            or elf1[1] >= elf2[0]
            and elf1[0] < elf2[0]
            or elf2[1] >= elf1[0]
            and elf2[0] < elf1[0]
        ):
            overlapping_elfs += 1

    print(fully_contained_elfs)  # answer: 657
    print(overlapping_elfs)  # answer: 938
