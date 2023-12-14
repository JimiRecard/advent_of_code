import pathlib

path = pathlib.Path(__file__).parent.resolve()


houses: set[tuple[int]] = set()
houses_santa: set[tuple[int]] = set()
houses_robo: set[tuple[int]] = set()

current_house = (0, 0)
current_house_santa = (0, 0)
current_house_robo = (0, 0)

houses.add(current_house)
houses_santa.add(current_house_santa)
houses_robo.add(current_house_robo)

with open(f"{path}/input.txt", "r") as file:
    for i, char in enumerate(file.read()):
        pair = i % 2 == 0
        match char:
            case "^":
                current_house = (current_house[0], current_house[1] + 1)
                if pair:
                    current_house_santa = (
                        current_house_santa[0],
                        current_house_santa[1] + 1,
                    )
                else:
                    current_house_robo = (
                        current_house_robo[0],
                        current_house_robo[1] + 1,
                    )
            case "v":
                current_house = (current_house[0], current_house[1] - 1)
                if pair:
                    current_house_santa = (
                        current_house_santa[0],
                        current_house_santa[1] - 1,
                    )
                else:
                    current_house_robo = (
                        current_house_robo[0],
                        current_house_robo[1] - 1,
                    )
            case ">":
                current_house = (current_house[0] + 1, current_house[1])
                if pair:
                    current_house_santa = (
                        current_house_santa[0] + 1,
                        current_house_santa[1],
                    )
                else:
                    current_house_robo = (
                        current_house_robo[0] + 1,
                        current_house_robo[1],
                    )
            case "<":
                current_house = (current_house[0] - 1, current_house[1])
                if pair:
                    current_house_santa = (
                        current_house_santa[0] - 1,
                        current_house_santa[1],
                    )
                else:
                    current_house_robo = (
                        current_house_robo[0] - 1,
                        current_house_robo[1],
                    )

        houses.add(current_house)
        if pair:
            houses_santa.add(current_house_santa)
        else:
            houses_robo.add(current_house_robo)


print(len(houses))  # answer: 2081
houses_santa.union(houses_robo)
print(len(houses_santa.union(houses_robo)))  # answer: 2341
