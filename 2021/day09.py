# def neighbours(x, y, mx, my:int) -> list:
#     neigh = [(x-1, y), (x+1, y), (x, y-1), (x,y+1)]
#     if x==0:
#         neigh.remove((x-1, y))
#     if x==mx-1:
#         neigh.remove((x+1, y))
#     if y==0:
#         neigh.remove((x, y-1))
#     if y==my-1:
#         neigh.remove((x, y+1))
#     return neigh

# def basin(x,y,data, _basin):
#     for n in neighbours(x, y, len(data[0]), len(data)):
#         if n not in _basin and data[n[1]][n[0]]>abs(data[y][x]):
#             _basin.append(n)
#             basin(n[1], n[0], data, _basin)


# data = [[int(x) for x in y] for y in open("day09.in").read().split()]
# points=[]
# for i,r in enumerate(data):
#     for j,c in enumerate(r):
#         vals = [data[y][x] for x,y in neighbours(j, i, len(data[0]), len(data))]
#         if c < min(vals):
#             points.append((i,j))
# print(sum([data[i][j]+1 for i,j in points]))
# basins = []
# for p in points:
#     bb=[p]
#     basin(p[1], p[0], data, bb)
#     basins.append(bb)
# basins.sort(reverse=True)
# print(len(basins[0])*len(basins[1])*len(basins[2]))

from math import prod

import networkx as nx

with open("day09.in") as f:
    ls = f.read().strip().split("\n")


# Part one
G = nx.grid_2d_graph(len(ls), len(ls[0]))
depth = {(i, j): int(ls[i][j]) for i, j in G.nodes}
print(
    sum(
        depth[v] + 1
        for v in G.nodes
        if all(depth[v] < depth[u] for u in G.neighbors(v))
    )
)

# Part two
G.remove_nodes_from(k for k, v in depth.items() if v == 9)
print(prod(sorted(map(len, nx.connected_components(G)))[-3:]))