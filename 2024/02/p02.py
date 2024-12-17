import pathlib

safe_reports1 = 0
safe_reports2 = 0
path = pathlib.Path(__file__).parent.resolve()
with open(f"{path}/input.txt", "r") as file:
    for line in file.readlines():
        levels = [int(num) for num in line.split()]
        steps = [abs(levels[i - 1] - levels[i]) for i in range(1, len(levels))]
        ascending = all([(levels[i - 1] < levels[i]) for i in range(1, len(levels))])
        descending = all([(levels[i - 1] > levels[i]) for i in range(1, len(levels))])
        if (ascending or descending) and max(steps) <= 3 and min(steps) >= 1:
            safe_reports1 += 1
        else:
            for i in range(len(levels)):
                new_levels = levels[:]
                new_levels.pop(i)
                steps = [
                    abs(new_levels[i - 1] - new_levels[i])
                    for i in range(1, len(new_levels))
                ]
                ascending = all(
                    [
                        (new_levels[i - 1] < new_levels[i])
                        for i in range(1, len(new_levels))
                    ]
                )
                descending = all(
                    [
                        (new_levels[i - 1] > new_levels[i])
                        for i in range(1, len(new_levels))
                    ]
                )
                if (ascending or descending) and max(steps) <= 3 and min(steps) >= 1:
                    safe_reports2 += 1
                    break

print(safe_reports1)
print(safe_reports1 + safe_reports2)
