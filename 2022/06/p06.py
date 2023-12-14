import pathlib

path = pathlib.Path(__file__).parent.resolve()
with open(f"{path}/input.txt", "r") as file:
    signal = file.read()
    for i, char in enumerate(signal):
        # # rule 1
        # char_set = {signal[j] for j in range(i, i + 4)}
        # if len(char_set) == 4:
        #     print(i + 4)
        #     break

        # rule 2
        char_set = {signal[j] for j in range(i, i + 14)}
        if len(char_set) == 14:
            print(i + 14)
            break
