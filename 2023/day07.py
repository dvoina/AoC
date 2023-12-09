from collections import Counter

CARDS = ["*", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
HANDS = ["High card", "One pair", "Two pair", "Three of a kind", "Full house", "Four of a kind", "Five of a kind"]
class Hand(object):
    def __init__(self, cards:str):
        self.cards:str = cards

    def __cmp(self, other:object):
        k = HANDS.index(self.type()) - HANDS.index(other.type())
        if k == 0:
            for i in range(5):
                k = CARDS.index(self.cards[i]) - CARDS.index(other.cards[i])
                if k != 0:
                    return k
        else: 
            return k
        
    def __gt__(self, other):
        return self.__cmp(other) > 0

    def __lt__(self, other):
        return self.__cmp(other) < 0
    
    def __eq__(self, other):
        return self.__cmp(other) == 0

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.cards

    def type(self):
        d = Counter(self.cards)

        five = len(list(filter(lambda x: x==5, d.values()))) > 0
        four = len(list(filter(lambda x: x==4, d.values()))) > 0
        three = len(list(filter(lambda x: x==3, d.values()))) > 0
        pairs = list(filter(lambda x: x==2, d.values()))

        if five:
            return HANDS[6]
        if four:
            return HANDS[5]
        if three and len(pairs) == 1:
            return HANDS[4]
        if three and len(pairs) == 0:
            return HANDS[3]
        if len(pairs) == 2:
            return HANDS[2]
        if len(pairs) == 1:
            return HANDS[1]
        return HANDS[0]

class HandV2(Hand):
    def __init__(self, cards: str):
        super().__init__(cards)
        self.cards = self.cards.replace("J", "*")

    def type(self):
        d = Counter(self.cards)
        jokers = d.pop("*", 0)
        if jokers == 5:
            cc = [0]
            return HANDS[6]
        else:
            cc = sorted(d.values())
            cc[-1] += jokers

        five = len(list(filter(lambda x: x==5, cc))) > 0
        four = len(list(filter(lambda x: x==4, cc))) > 0
        three = len(list(filter(lambda x: x==3, cc))) > 0
        pairs = list(filter(lambda x: x==2, cc))

        if five:
            return HANDS[6]
        if four:
            return HANDS[5]
        if three and len(pairs) == 1:
            return HANDS[4]
        if three and len(pairs) == 0:
            return HANDS[3]
        if len(pairs) == 2:
            return HANDS[2]
        if len(pairs) == 1:
            return HANDS[1]
        return HANDS[0]


data = [tuple(l.split()) for l in open("day07.in").read().strip().split('\n')]
for i,d in enumerate(data):
    data[i] = (Hand(d[0]), int(d[1]))

s = 0
for i, h in enumerate(sorted(data, key=lambda t: t[0])):
    s += h[1] * (i+1)
print(s)

data = [tuple(l.split()) for l in open("day07.in").read().strip().split('\n')]
for i,d in enumerate(data):
    data[i] = (HandV2(d[0]), int(d[1]))

s = 0
for i, h in enumerate(sorted(data, key=lambda t: t[0])):
    s += h[1] * (i+1)
print(s)


