forest = []
with open("input.txt", "r") as file:
    for line in file.readlines():
        forest.append([int(ch) for ch in line if ch.isdigit()])

f_heigth = len(forest)
f_width = len(forest[0])


def is_visible(i, j):
    tree_height = forest[i][j]
    left_trees = [tree for tree in forest[i][:j]]
    if all([tree < tree_height for tree in left_trees]):
        return True
    right_trees = [tree for tree in forest[i][j + 1 :]]
    if all([tree < tree_height for tree in right_trees]):
        return True
    top_trees = [forest[_][j] for _ in range(i)]
    if all([tree < tree_height for tree in top_trees]):
        return True
    bottom_trees = [forest[_][j] for _ in range(i + 1, f_heigth)]
    if all([tree < tree_height for tree in bottom_trees]):
        return True
    return False


def scenic_score(i, j):
    tree_height = forest[i][j]
    left_trees, rigth_trees, top_trees, bottom_trees = 0, 0, 0, 0

    for idx in range(j - 1, -1, -1):
        left_trees += 1
        if forest[i][idx] >= tree_height:
            break

    for idx in range(j + 1, f_width):
        rigth_trees += 1
        if forest[i][idx] >= tree_height:
            break

    for idx in range(i - 1, -1, -1):
        top_trees += 1
        if forest[idx][j] >= tree_height:
            break

    for idx in range(i + 1, f_heigth):
        bottom_trees += 1
        if forest[idx][j] >= tree_height:
            break

    return left_trees * rigth_trees * bottom_trees * top_trees


if __name__ == "__main__":
    visible_trees = f_heigth * 2 + f_width * 2 - 4
    for i in range(1, f_heigth - 1):
        for j in range(1, f_width - 1):
            if is_visible(i, j):
                visible_trees += 1

    print(visible_trees)  # answer: 1812

    scenic_scores = set()
    for i in range(1, f_heigth - 1):
        for j in range(1, f_width - 1):
            scenic_scores.add(scenic_score(i, j))
    print(max(scenic_scores))  # answer: 315495
