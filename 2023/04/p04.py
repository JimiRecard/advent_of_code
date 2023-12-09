import re

points = 0
cards = {f"Card {i}": 1 for i in range(1, 203)}
with open("input.txt", "r") as file:
    for card in file.readlines():
        card_number = int(re.findall("\d+", card.split(":")[0])[0])
        win_numbers = [
            num for num in re.findall("\d{1,2}", card.split(": ")[1].split(" |")[0])
        ]
        nums_you_have = [num for num in re.findall("\d{1,2}", card.split("| ")[1])]
        power = sum(1 for num in win_numbers if num in nums_you_have)

        if power > 0:
            points += pow(2, power - 1)

        for i in range(power):
            cards[f"Card {card_number + 1 + i}"] += 1 * cards[f"Card {card_number}"]

print(points)  # answer: 18619
print(sum(card for card in cards.values()))  # answer: 8063216
