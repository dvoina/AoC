import re


def score(s):
    if len(s) == 0:
        return 0
    return  1 << (len(s) - 1)

data = [[t.strip() for t in re.split("(: |\| )", line)] for line in open("day04.in").read().strip().split("\n")]
s = 0
for i, card in enumerate(data):
    data[i] = (card[0], set(card[2].split()), set(card[4].split()))
    winners = data[i][1] & data[i][2]
    s += score(winners)
print(s)

c = [1 for card in data]
print(c)
for i,card in enumerate(data):
    winners = card[1] & card[2]
    for j in range(len(winners)):
        c[i+1+j] += c[i]
print(sum(c))