#   /\   /\
#  /  \ /  \
# |   _|_   |
# |    |    |
#  \  / \  /
#   \/   \/


import math
from collections import defaultdict, Counter
m = round(math.sqrt(3), 5)
directions = { 'e':(2,0), 'se':(1,-m), 'sw':(-1,-m), 'w':(-2,0), 'nw':(-1, m), 'ne':(1, m)}

data = [list(l.strip()) for l in open('input24.txt').readlines()]
black = set()
for l in data:
    x, y = 0, 0
    while len(l)>0:
        co = l.pop(0)
        if co in ['n', 's']:
            co += l.pop(0)
        x,y = x+directions[co][0], y+directions[co][1]
    black ^= {(x,y)}

print(len(black))
