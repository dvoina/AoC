from collections import defaultdict

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
hands = ["High card", "One pair", "Two pair", "Three of a kind", "Full house", "Four of a kind", "Five of a kind"]
class Hand(object):
    def __init__(self, cards:str):
        self.cards = cards

    def __cmp__(self, other):
        k = hands.index(self.type()) - hands.index(other.type())
        if k == 0:
            for i in range(5):
                k = cards.index(self.cards[i]) - cards.index(other.cards[i])
                if k != 0:
                    return k
        else: 
            return k
        
    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0
    
    def __eq__(self, other):
        return self.__cmp__(other) == 0
        

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.cards

    def __score(self):
        return (self.type, self.score)

    def type(self):
        d = defaultdict(int)
        for card in self.cards:
            d[card] += 1

        five = len(list(filter(lambda x: x==5, d.values()))) > 0
        four = len(list(filter(lambda x: x==4, d.values()))) > 0
        three = len(list(filter(lambda x: x==3, d.values()))) > 0
        pairs = list(filter(lambda x: x==2, d.values()))

        if five:
            return hands[6]
        if four:
            return hands[5]
        if three and len(pairs) == 1:
            return hands[4]
        if three and len(pairs) == 0:
            return hands[3]
        if len(pairs) == 2:
            return hands[2]
        if len(pairs) == 1:
            return hands[1]
        return hands[0]


data = [tuple(l.split()) for l in open("day07.in").read().strip().split('\n')]
for i,d in enumerate(data):
    data[i] = (Hand(d[0]), int(d[1]))

s = 0
for i, h in enumerate(sorted(data, key=lambda t: t[0])):
    s += h[1] * (i+1)
print(s)

