import pathlib


class Card:
    # # Part 1
    # _card_values = "23456789TJQKA"

    # Part 2
    _card_values = "J23456789TQKA"

    def __init__(self, card: str) -> None:
        if card in self._card_values:
            self.card = card
            self.value = self._card_values.index(card)
        else:
            raise ValueError

    def __str__(self):
        return f"Card {self.card}"

    def __repr__(self):
        return f"Card {self.card}"

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __hash__(self):
        return hash((self.value, self.card))


class Hand:
    _hand_dict = {
        0: "High card",
        1: "One pair",
        2: "Two pair",
        3: "Three of a kind",
        4: "Full house",
        5: "Four of a kind",
        6: "Five of a kind",
    }

    def __init__(self, hand: str) -> None:
        self.card_string = hand.split(" ")[0]
        self.cards = [Card(c) for c in self.card_string]
        self.bid = int(hand.split(" ")[1])

    @property
    def type(self):
        card_set = set(self.cards)
        card_dict = dict.fromkeys(card_set, 0)

        for card in self.cards:
            card_dict[card] += 1

        # Part 2

        if Card("J") in card_set and len(card_set) > 1:
            J = card_dict.pop(Card("J"))
            card_dict[max(card_dict, key=card_dict.get)] += J

        # End Part 2

        match max(card_dict.values()):
            case 5:  # Five of a kind
                return 6
            case 4:  # Four of a kind
                return 5
            case 3:
                if len(card_dict) == 2:  # Full house
                    return 4
                else:  # Three of a kind
                    return 3
            case 2:
                if len(card_dict) == 3:  # Two pair
                    return 2
                else:  # One pair
                    return 1
            case 1:  # High card
                return 0

    def __str__(self):
        return f"Hand {self.card_string}: {self._hand_dict[self.type]}"

    def __repr__(self):
        return f"Hand {self.card_string}: {self._hand_dict[self.type]}"

    def __lt__(self, other):
        if self == other:
            return False
        else:
            if self.type < other.type:
                return True
            elif self.type == other.type:
                for i in range(len(self.cards)):
                    if self.cards[i] < other.cards[i]:
                        return True
                    elif self.cards[i] == other.cards[i]:
                        pass
                    else:
                        return False
            else:
                return False

    def __le__(self, other):
        if self == other:
            return True
        else:
            if self.type < other.type:
                return True
            elif self.type == other.type:
                for i in range(len(self.cards)):
                    if self.cards[i] < other.cards[i]:
                        return True
                    elif self.cards[i] == other.cards[i]:
                        pass
                    else:
                        return False
            else:
                return False

    def __eq__(self, other):
        return self.card_string == other.card_string

    def __ne__(self, other):
        return self.card_string != other.card_string

    def __gt__(self, other):
        if self == other:
            return False
        else:
            if self.type > other.type:
                return True
            elif self.type == other.type:
                for i in range(len(self.cards)):
                    if self.cards[i] > other.cards[i]:
                        return True
                    elif self.cards[i] == other.cards[i]:
                        pass
                    else:
                        return False
            else:
                return False

    def __ge__(self, other):
        if self == other:
            return True
        else:
            if self.type > other.type:
                return True
            elif self.type == other.type:
                for i in range(len(self.cards)):
                    if self.cards[i] > other.cards[i]:
                        return True
                    elif self.cards[i] == other.cards[i]:
                        pass
                    else:
                        return False
            else:
                return False

    def __hash__(self):
        return hash(self.card_string)


hands = list()

path = pathlib.Path(__file__).parent.resolve()
with open(f"{path}/input.txt", "r") as file:
    for hand in file.readlines():
        hands.append(Hand(hand))

hands.sort()
winnings = [hands[i].bid * (i + 1) for i in range(len(hands))]

print(sum(winnings))
# answer Part 1: 251545216
# answer Part 2: 250384185
