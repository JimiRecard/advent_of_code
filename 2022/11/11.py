import re
from collections import deque


class Monkey1:
    def __init__(
        self, items: list[int], test: int, operation: str, truthy: int, falsy: int
    ):
        self.items = deque()
        for item in items:
            self.items.append(item)
        self.test = test
        self.operation = operation
        self.truthy = truthy
        self.falsy = falsy
        self.monkey_business = 0

    def worry_level(self, item):
        if self.operation.split()[1] == "old":
            item *= item
        else:
            if self.operation[0] == "*":
                item *= int(self.operation.split()[1])
            else:
                item += int(self.operation.split()[1])

        return item // 3

    def throw(self):
        self.monkey_business += 1
        item = self.items.popleft()
        item = self.worry_level(item)
        if item % self.test == 0:
            return self.truthy, item
        else:
            return self.falsy, item

    def __str__(self):
        return f"Monkey items: {self.items}"

    def __repr__(self):
        return f"Monkey items: {self.items}"


monkey_list: list[Monkey1] = []

with open("input.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        match i % 7:
            case 1:
                items = [int(item) for item in re.findall("\d+", line)]
            case 2:
                operation = line[re.search("old ", line).end() : -1]
            case 3:
                test = int(re.findall("\d+", line)[0])
            case 4:
                truthy = int(re.findall("\d+", line)[0])
            case 5:
                falsy = int(re.findall("\d+", line)[0])
                monkey_list.append(Monkey1(items, test, operation, truthy, falsy))


for round in range(20):
    for monkey in monkey_list:
        while monkey.items:
            i, item = monkey.throw()
            monkey_list[i].items.append(item)

mb_list = [monkey.monkey_business for monkey in monkey_list]
mb_list.sort()
print(mb_list[-1] * mb_list[-2])  # answer: 316888


class Monkey2:
    def __init__(
        self, items: list[list[int]], test: int, operation: str, truthy: int, falsy: int
    ):
        self.items = deque()
        for item in items:
            self.items.append([item % i for i in [2, 3, 5, 7, 11, 13, 17, 19]])
        self.test = [2, 3, 5, 7, 11, 13, 17, 19].index(test)
        self.operation = operation
        self.truthy = truthy
        self.falsy = falsy
        self.monkey_business = 0

    def worry_level(self, item):
        if self.operation.split()[1] == "old":
            for i, prime in enumerate([2, 3, 5, 7, 11, 13, 17, 19]):
                item[i] = (item[i] * item[i]) % prime
        else:
            m = int(self.operation.split()[1])
            for i, prime in enumerate([2, 3, 5, 7, 11, 13, 17, 19]):
                if self.operation[0] == "*":
                    item[i] = (item[i] * m) % prime
                else:
                    item[i] = (item[i] + m) % prime

        return item

    def throw(self):
        self.monkey_business += 1
        item = self.items.popleft()
        item = self.worry_level(item)
        if item[self.test] == 0:
            return self.truthy, item
        else:
            return self.falsy, item

    def __str__(self):
        return f"Monkey items: {self.items}"

    def __repr__(self):
        return f"Monkey items: {self.items}"


monkey_list: list[Monkey2] = []

with open("input.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        match i % 7:
            case 1:
                items = [int(item) for item in re.findall("\d+", line)]
            case 2:
                operation = line[re.search("old ", line).end() : -1]
            case 3:
                test = int(re.findall("\d+", line)[0])
            case 4:
                truthy = int(re.findall("\d+", line)[0])
            case 5:
                falsy = int(re.findall("\d+", line)[0])
                monkey_list.append(Monkey2(items, test, operation, truthy, falsy))

for round in range(10000):
    for monkey in monkey_list:
        while monkey.items:
            i, item = monkey.throw()
            monkey_list[i].items.append(item)

mb_list = [monkey.monkey_business for monkey in monkey_list]
mb_list.sort()
print(mb_list[-1] * mb_list[-2])  # answer: 35270398814
