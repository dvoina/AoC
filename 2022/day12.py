from math import inf

import networkx as nx

lines = open("2022/day12.txt").readlines()

starts = set()
hm = {}
for y, l in enumerate(lines):
    for x, char in enumerate(l):
        p = (y, x)
        hm[p] = ord(char)
        if char == "S":
            s = p
            hm[p] = ord("a")
        if char == "E":
            e = p
            hm[p] = ord("z")
        if char == "a":  # Part 2
            starts.add(p)

G = nx.DiGraph()
for p in hm:
    for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if hm.get((p[0]+d[0], p[1]+d[1]), inf) <= hm[p] + 1:
            G.add_edge(p, (p[0]+d[0], p[1]+d[1]))

# Part 1
print(nx.shortest_path_length(G, s, e))

# Part 2
paths = nx.shortest_path_length(G, target=e)
print(min(paths.get(a, inf) for a in starts))