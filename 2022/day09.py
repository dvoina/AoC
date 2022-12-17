import math
moves = map(lambda x: (directions[x[0]], int(x[1])), [l.split() for l in open("2022/day09.txt").readlines()])
directions = {"U": (0, 1), "D":(0, -1), "L":(-1, 0), "R":(1, 0)}
crt = (0, 0)
tailpos = {crt}

def doMove(head, tail, move):
    for _ in range(move[1]):
        head = (head[0] + move[0][0], head[1] + move[0][1])
        tail = adjustTail(head, tail, move[0])
        tailpos.add(tail)
    return head, tail

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


def adjustTail(h, t, d):
    return tail

head, tail = crt, crt

for move in moves:
    head, tail = doMove(head, tail, move)
print(len(tailpos))
