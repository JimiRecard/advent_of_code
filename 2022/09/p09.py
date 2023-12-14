import pathlib


def new_tpos(h: list[int], t: list[int]):
    dx = h[0] - t[0]
    dy = h[1] - t[1]
    dist = abs(dx) + abs(dy)
    if dist <= 1 or (dist == 2 and dx and dy):
        return
    elif dist == 2:
        if dx:
            t[0] += int(dx / abs(dx))
        else:
            t[1] += int(dy / abs(dy))
    else:
        t[0] += int(dx / abs(dx))
        t[1] += int(dy / abs(dy))


def h_move(hpos: list[int], dir: str):
    match (dir):
        case "U":
            hpos[1] += 1
        case "D":
            hpos[1] -= 1
        case "R":
            hpos[0] += 1
        case "L":
            hpos[0] -= 1


path = pathlib.Path(__file__).parent.resolve()
with open(f"{path}/input.txt", "r") as file:
    rope = [[0, 0] for _ in range(2)]
    tpos_set = {(rope[1][0], rope[1][1])}
    for line in file.readlines():
        direction = line[0]
        for _ in range(int(line.split()[1])):
            h_move(rope[0], direction)
            new_tpos(rope[0], rope[1])
            tpos_set.add((rope[1][0], rope[1][1]))

    print(len(tpos_set))  # answer: 5902


with open(f"{path}/input.txt", "r") as file:
    rope = [[0, 0] for _ in range(10)]
    tpos_set = {(rope[-1][0], rope[-1][1])}
    for line in file.readlines():
        direction = line[0]
        for _ in range(int(line.split()[1])):
            for i, knot in enumerate(rope):
                if i == 0:
                    h_move(knot, direction)
                else:
                    new_tpos(rope[i - 1], rope[i])
            tpos_set.add((rope[-1][0], rope[-1][1]))

    print(len(tpos_set))  # answer: 2445
