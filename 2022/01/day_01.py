elf_list = []
with open("input.txt", "r") as file:
    elf_calories = 0
    for line in file.readlines():
        if line == "\n":
            elf_list.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(line)
    print(max(elf_list))  # Answer: 69289
    elf_list.sort()
    print(elf_list[-1] + elf_list[-2] + elf_list[-3])  # Answer: 205615
