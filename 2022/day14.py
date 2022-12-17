rocks = [[tuple(map(int, t.strip().split(","))) for t in l.split(" -> ")] for l in open("2022/day14.txt").readlines()]

d={}
for r in rocks:
    for i, p in enumerate(r[:-1]):
        a,b=r[i], r[i+1]
        if a[0]==b[0]:
            for y in range(min(a[1], b[1]), max(a[1], b[1])):
                d[(a[0], y)]='#'
        if a[1]==b[1]:
            for x in range(min(a[0], b[0]), max(a[0], b[0])):
                d[(x, a[1])]='#'


