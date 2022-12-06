from collections import defaultdict
import re

class Tile(object):
    def __init__(self, id, data):
        self.id = int(id)
        self.data = data
        self.edges = []
        self.neigh = [False] * 4

        self.__edges()

    def __edges(self):
        self.edges = [self.data[0], \
            "".join([d[0] for d in self.data]), \
            self.data[-1], \
            "".join([d[-1] for d in self.data]) \
        ]

    def countNeigh(self):
        return sum(map(lambda x: 1 if x else 0, self.neigh))

    def dropBorders(self):
        return [d[1:-1] for d in self.data[1:-1]]

    def matches(self, other):
        m = False
        for i, e1 in enumerate(self.edges):
            for e2 in other.edges:
                if e1 == e2 or e1 == e2[::-1]:
                    self.neigh[i] = True
                    m = True
        return m


tiles = [t.strip().split("\n") for t in open("input20.txt").read().strip().split("\n\n")]
tiles = [Tile(re.findall("\w+", t[0])[1], t[1:]) for t in tiles]
matches = defaultdict(bool)
for t1 in tiles:
    for t2 in tiles:
        if t1 is not t2 and t1.matches(t2):
            matches[(t1.id, t2.id)] = True
    t1.countNeigh()

corners = [x.id for x in tiles if x.countNeigh() == 2]
print(corners[0]*corners[1]*corners[2]*corners[3])

board = [[None for i in range(12)] for j in range(12)]
cand = [t.id for t in tiles]

cand.remove(corners[0])
board[0][0] = corners[0]

def solve(b, i, j, c, r):
    if len(r)>0:
        return

    if c == []:
        r.append([bb[:] for bb in b])
        return 
    
    if i==0 and j==0:
        solve(b, i, j+1, c, r)
    
    if j>11:
        solve(b, i+1, 0, c, r)
        return

    if i==0 and j>=0:    
        for k, t in enumerate(c):
            if matches[(b[i][j-1], t)]:
                b[i][j] = c.pop(k)
                solve(b, i, j+1, c, r)
                c.insert(k, t)
                b[i][j] = None

    if i>=0 and j==0:    
        for k, t in enumerate(c):
            if matches[(b[i-1][j], t)]:
                b[i][j] = c.pop(k)
                solve(b, i, j+1, c, r)
                c.insert(k, t)
                b[i][j] = None

    if i>0 and j>0:
        for k, t in enumerate(c):
            if matches[(b[i][j-1], t)] and matches[(b[i-1][j], t)]:
                b[i][j] = c.pop(k)
                solve(b, i, j+1, c, r)
                c.insert(k, t)
                b[i][j] = None

r = []
solve(board, 0, 0, cand, r)

sol = r[0]
for i, r in enumerate(sol):
    for j,c in enumerate(r):
        for t in tiles:
            if t.id==c:
                sol[i][j] = t.dropBorders()
map = []
for r in sol:
    for rr in range(8):
        map.append("".join([c[rr] for c in r]))
print("\n".join(map))