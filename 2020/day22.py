data = open("input22.txt").read().strip().split("\n\n")
player1, player2 = [[int(x) for x in d.split("\n")[1:]] for d in data]
rounds = 0
while True:
    card1, card2 = player1.pop(0), player2.pop(0)
    if card1 > card2:
        player1.append(card1)
        player1.append(card2)
    else:
        player2.append(card2)
        player2.append(card1)
    rounds += 1
    if rounds % 1000 == 0:
        print(".", end="")
    if len(player1) == 0 or len(player2)==0:
        break
print(rounds)
score = 0
if len(player1)==0:
    n = len(player2)
    for i,x in enumerate(player2):
        score += x*(n-i)
if len(player2)==0:
    n = len(player1)
    for i,x in enumerate(player1):
        score += x*(n-i)

print(score)

def solve(p1, p2):
    prev = set()
    while p1 and p2:
        hand = (tuple(p1), tuple(p2))
        if hand in prev:
            return True, p1
        prev.add(hand)
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if len(p1) >= c1 and len(p2) >= c2:
            p1_won, _ = solve(p1[:c1], p2[:c2])
        else:
            p1_won = c1 > c2
        winner = p1 if p1_won else p2
        winner.append(c1 if p1_won else c2)
        winner.append(c1 if not p1_won else c2)
    return p1_won, winner

player1, player2 = [[int(x) for x in d.split("\n")[1:]] for d in data]
a,b =  solve(player1, player2)

score = 0
n = len(b)
for i,x in enumerate(b):
    score += x*(n-i)
print(score)