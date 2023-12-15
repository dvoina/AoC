import re
from collections import defaultdict
def _hash(s):
    sum = 0
    for c in s:
        o = ord(c)
        sum += o
        sum = (sum * 17) % 256
    return sum

data = [x for x in open("day15.in").read().strip().split(",")]
s = sum(_hash(x) for x in data)
print(s)

boxes = defaultdict(list)
data = [re.match(r"(\w+)(-|=)(\d+)?", x).groups() for x in data]
for d in data:
    box = _hash(d[0])
    if d[1]=="=":
        skip = False
        for i, l in enumerate(boxes[box]):
            if l[0] == d[0]:
                boxes[box][i] = (d[0], d[2])
                skip = True
                break
        if not skip:
            boxes[box].append((d[0], d[2]))
    if d[1]=='-':
        for i, lens in enumerate(boxes[box]):
            if lens[0] == d[0]:
                boxes[box].pop(i)
                break
s = 0
for k,v in boxes.items():
    for i, l in enumerate(v):
        s += (k+1) * (i+1) * int(l[1])
print(s)
