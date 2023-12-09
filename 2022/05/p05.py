import re
from collections import deque

with open("input.txt", "r") as file:
    deque_list = [deque() for _ in range(9)]
    temp_deque = deque()
    for i, line in enumerate(file.read().split("\n")):
        if len(line) == 35 and line[0] != " ":
            for i in range(35):
                if i % 4 == 1 and line[i] != " ":
                    deque_list[i // 4].appendleft(line[i])

        else:
            ## CrateMover 9000
            # try:
            #     qty = int(re.findall(r"move (\d+)", line)[0])
            #     dq1 = int(re.findall(r"from (\d+)", line)[0]) - 1
            #     dq2 = int(re.findall(r"to (\d+)", line)[0]) - 1

            #     for j in range(qty):
            #         deque_list[dq2].append(deque_list[dq1].pop())

            # Cratemover 9001
            try:
                qty = int(re.findall(r"move (\d+)", line)[0])
                dq1 = int(re.findall(r"from (\d+)", line)[0]) - 1
                dq2 = int(re.findall(r"to (\d+)", line)[0]) - 1

                for j in range(qty):
                    temp_deque.append(deque_list[dq1].pop())

                for j in range(qty):
                    deque_list[dq2].append(temp_deque.pop())

            except:
                pass

    print([d[-1] for d in deque_list])
