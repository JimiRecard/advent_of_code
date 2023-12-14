import pathlib

path = pathlib.Path(__file__).parent.resolve()
with open(f"{path}/input.txt", "r") as file:
    score_1 = 0
    score_2 = 0
    win_1 = ["A Y", "B Z", "C X"]
    draw_1 = ["A X", "B Y", "C Z"]
    loss_2 = ["A Z", "B X", "C Y"]
    for play in file.read().split("\n"):
        # rule 1
        if play in win_1:
            score_1 += 6
        elif play in draw_1:
            score_1 += 3

        if "X" in play:
            score_1 += 1
        elif "Y" in play:
            score_1 += 2
        elif "Z" in play:
            score_1 += 3

        # rule 2

        match play[0]:
            case "A":
                if "X" in play:
                    score_2 += 3
                elif "Y" in play:
                    score_2 += 4
                elif "Z" in play:
                    score_2 += 8
            case "B":
                if "X" in play:
                    score_2 += 1
                elif "Y" in play:
                    score_2 += 5
                elif "Z" in play:
                    score_2 += 9
            case "C":
                if "X" in play:
                    score_2 += 2
                elif "Y" in play:
                    score_2 += 6
                elif "Z" in play:
                    score_2 += 7

    print(score_1)  # answer: 10941
    print(score_2)  # answer: 13071
