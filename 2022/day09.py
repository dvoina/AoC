import math
moves = [tuple(l.strip().split()) for l in open("2022/day09.txt").readlines()]
print(moves)

directions = {"U": (0, 1), "D":(0, -1), "L":(-1, 0), "R":(1, 0)}
crt = (0, 0)
tailpos = {crt}

def doMove(head, tail, move):
    for _ in range(int(move[1])):
        head = (head[0] + directions[move[0]][0], head[1] + directions[move[0]][1])
        tail = adjustTail(head, tail, directions[move[0]])
        tailpos.add(tail)
    return head, tail

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def adjustTail(head, tail, d):
    if dist(head, tail) >= 2 :
        tail = abs(head[0])-abs(tail[0]), abs(head[1])-abs(head[1])
    if dist(head, tail) == 1:
        tail = (tail[0] + d[0], tail[1] + d[1])
    return tail
                

head, tail = crt, crt

for move in moves:
    head, tail = doMove(head, tail, move)
print(len(tailpos)-1)


s = [crt] * 10
for move in moves:
    for i in range(10):
        head, tail = doMove(head, tail, move)
print(len(tailpos)-1)
