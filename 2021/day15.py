import networkx as nx

data = [[int(x) for x in y.strip()] for y in open("day15.in").read().split()]
m=len(data)
n=len(data[0])

def getNeighbours(line, col, maxLine, maxCol):
    def pred(p):
        return ((0 <= p[0] < maxLine) and (0 <= p[1] < maxCol))
    neighbours = [(line-1, col), (line+1, col), (line, col-1), (line, col+1)]
    return filter(pred, neighbours)

def multiplyLine(d,n):
    def v(x):
        r = x+1
        if r>9: 
            return 1
        else:
            return r
     
    dd = []
    for i in range(1, n+1):
        dd.extend([v(x) for x in d])
    return dd

G = nx.DiGraph()
for i,l in enumerate(data):
    for j,c in enumerate(l):
        for nn in getNeighbours(i, j, m, n):
            G.add_edge((i,j), nn, weight=c)

print(nx.shortest_path_length(G, (0,0), (m-1, n-1), weight="weight"))
newData = []
for c in range(0,5):
    for l in data:
        newData.append(multiplyLine(l,(c+5)))

m,n = len(newData), len(newData[0])
for x in newData:
    print("".join([str(xx) for xx in x]))

G = nx.DiGraph()
for i,l in enumerate(data):
    for j,c in enumerate(l):
        for nn in getNeighbours(i, j, m, n):
            G.add_edge((i,j), nn, weight=c)

print(nx.shortest_path_length(G, (0,0), (m-1, n-1), weight="weight"))