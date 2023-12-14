sky_map = list()
empty_rows_idx = list()
with open("input.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        # Needs to be list, str is not subscriptable
        sky_map.append([char for char in line.strip()])

        # Get indexes for 'empty' rows
        if all(char == "." for char in line.strip()):
            empty_rows_idx.append(i)

# Get indexes for 'empty' columns
empty_cols_idx = list()

for j in range(len(sky_map[0])):
    if all(sky_map[i][j] == "." for i in range(len(sky_map))):
        empty_cols_idx.append(j)

# Gets all galaxies indexes
galaxies_idx = [
    [i, j]
    for i in range(len(sky_map))
    for j in range(len(sky_map[0]))
    if sky_map[i][j] == "#"
]


def distance(
    g1: list[int],
    g2: list[int],
    empty_cols_idx: list[int],
    empty_rows_idx: list[int],
    expansion: int,
):
    """Returns the manhattan distance between two galaxies considering expansion

    Args:
        g1 (list[int]): Galaxy 1
        g2 (list[int]): Galaxy 2
        empty_cols_idx (list[int]): Indexes of empty collumns
        empty_rows_idx (list[int]): Indexes of empty rows
        expansion (int): how much an empty row or collumn expands

    Returns:
        int: The manhattan distance between two galaxies considering expansion
    """
    h_exp = sum(1 for i in empty_cols_idx if min(g1[1], g2[1]) < i < max(g1[1], g2[1]))
    v_exp = sum(1 for i in empty_rows_idx if min(g1[0], g2[0]) < i < max(g1[0], g2[0]))
    return (
        abs(g2[0] - g1[0])
        + abs(g2[1] - g1[1])
        - h_exp
        - v_exp
        + (h_exp + v_exp) * expansion
    )


# Gets all distances between all galaxies, considering expansion 2
galaxy_distances = list()
for i in range(len(galaxies_idx)):
    for j in range(i + 1, len(galaxies_idx)):
        galaxy_distances.append(
            distance(
                galaxies_idx[i], galaxies_idx[j], empty_cols_idx, empty_rows_idx, 2
            )
        )

# Gets all distances between all galaxies, considering expansion 1M
galaxy_distances_M = list()
for i in range(len(galaxies_idx)):
    for j in range(i + 1, len(galaxies_idx)):
        galaxy_distances_M.append(
            distance(
                galaxies_idx[i], galaxies_idx[j], empty_cols_idx, empty_rows_idx, 1e6
            )
        )


print(sum(galaxy_distances))  # answer: 9563821

print(int(sum(galaxy_distances_M)))  # answer: 827009909817
