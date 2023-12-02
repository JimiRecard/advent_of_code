import string

with open("input.txt", "r") as file:
    dup_priorities = 0
    badge_priorities = 0
    letter_values = " " + string.ascii_letters
    group_sacks: list[set] = []

    for i, line in enumerate(file.read().split("\n")):
        div = int(len(line) / 2)
        set1 = set(line[:div])
        set2 = set(line[div:])
        item = set1.intersection(set2).pop()
        dup_priorities += letter_values.index(item)

        group_sacks.append(set(line))
        if i % 3 == 2:
            badge = (
                group_sacks[0]
                .intersection(group_sacks[1])
                .intersection(group_sacks[2])
                .pop()
            )
            badge_priorities += letter_values.index(badge)
            group_sacks = []

    print(dup_priorities)  # answer: 7824
    print(badge_priorities)  # answer: 2798
