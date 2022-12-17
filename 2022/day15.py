import re

def md(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

data = [re.findall("\d+", l) for l in open("2022/day15.txt").readlines()]
data = [((x[0], x[1]), (x[2], x[3])) for x in data]
print(data)

