def nxt(previous: list[int], index: list[int], field: list[str]):
    style = field[index[0]][index[1]]
    match style:
        case "S":
            return None
        case "F":
            if previous[0] == index[0]:
                return [index[0] + 1, index[1]]
            else:
                return [index[0], index[1] + 1]
        case "-":
            if previous[1] < index[1]:
                return [index[0], index[1] + 1]
            else:
                return [index[0], index[1] - 1]
        case "7":
            if previous[0] == index[0]:
                return [index[0] + 1, index[1]]
            else:
                return [index[0], index[1] - 1]
        case "|":
            if previous[0] < index[0]:
                return [index[0] + 1, index[1]]
            else:
                return [index[0] - 1, index[1]]
        case "J":
            if previous[0] == index[0]:
                return [index[0] - 1, index[1]]
            else:
                return [index[0], index[1] - 1]
        case "L":
            if previous[0] == index[0]:
                return [index[0] - 1, index[1]]
            else:
                return [index[0], index[1] + 1]


#  sets 2D array field and finds S_index
field = list()
with open("input.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        # str is not subscriptable, list is
        field.append([char for char in line.strip()])
        if "S" in line:
            S_index = [i, line.index("S")]


# starting from first pipe after S is easier, as direction is already defined
# (previous is S)
steps = 1
previous_index = S_index
if field[S_index[0] - 1][S_index[1]] in ["7", "|", "F"]:
    current_index = [S_index[0] - 1, S_index[1]]
elif field[S_index[0]][S_index[1] + 1] in ["J", "-", "7"]:
    current_index = [S_index[0], S_index[1] + 1]
elif field[S_index[0] + 1][S_index[1]] in ["J", "|", "L"]:
    current_index = [S_index[0] + 1, S_index[1]]
elif field[S_index[0]][S_index[1] - 1] in ["F", "-", "L"]:
    current_index = [S_index[0], S_index[1] - 1]


# navigates through all pipes in loop
while current_index != S_index:
    steps += 1
    previous_index, current_index = current_index, nxt(
        previous_index, current_index, field
    )
    # To ease map visualization, replace loop pipes with box drawing chars
    # Important for Part 2
    field[previous_index[0]][previous_index[1]] = field[previous_index[0]][
        previous_index[1]
    ].translate(str.maketrans("LJF7-|", "└┘┌┐─│"))

print(int(steps / 2))  # answer: 6806


# Part 2

# Replace every non loop tile with # for better visualization. Optional step
# Also replace S with the right pipe according to its surroundings. Not optional
# Assumes S is not in one of the borders
for f in field:
    for i in range(len(f)):
        if f[i] == "S":
            # match [left, up, right, down]
            match [
                field[S_index[0]][S_index[1] - 1],
                field[S_index[0] - 1][S_index[1]],
                field[S_index[0]][S_index[1] + 1],
                field[S_index[0] + 1][S_index[1]],
            ]:
                case ["┌" | "─" | "└", "│" | "┐" | "┌", _, _]:
                    f[i] = "┘"

                case [_, "│" | "┐" | "┌", "┐" | "─" | "┘", _]:
                    f[i] = "└"

                case [_, _, "┐" | "─" | "┘", "│" | "└" | "┘"]:
                    f[i] = "┌"

                case ["┌" | "─" | "└", _, _, "│" | "└" | "┘"]:
                    f[i] = "┐"

                case ["┌" | "─" | "└", _, "┐" | "─" | "┘", _]:
                    f[i] = "─"

                case [_, "│" | "┐" | "┌", _, "│" | "└" | "┘"]:
                    f[i] = "│"

        elif f[i] not in "└┘┌┐─│":
            f[i] = "#"

    # show map
    print("".join(f))

num_of_inner_chars = 0


for j, f in enumerate(field):
    bottom_inside = False
    top_inside = False
    for i in range(len(f)):
        # Every line begins outside the loop. After walls, the character is inside
        # Corner characters divide in top and bottom.
        # ┌┘ and └┐ (with as many ─ in between) form a full wall.
        if f[i] == "│":
            top_inside = not top_inside
            bottom_inside = not bottom_inside
        elif f[i] in "└┘":
            top_inside = not top_inside
        elif f[i] in "┌┐":
            bottom_inside = not bottom_inside
        else:
            if bottom_inside and top_inside and f[i] != "─":
                num_of_inner_chars += 1

print(num_of_inner_chars)  # answer: 449
