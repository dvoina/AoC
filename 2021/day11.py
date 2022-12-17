import cellpylib as cpl

def neighbours(x, y, mx, my:int) -> list:
    def valid(p):
        return (0<=p[0]<mx) and (0<=p[1]<my)

    return filter(valid, [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)])

squids = [[int(x) for x in y] for y in open("day11.in").read().split()]

print(squids)
flashes = 0
for step in range(100):
    for i,r in enumerate(squids):
        for j,c in enumerate(r):
            squids[i][j] += 1
            if squids[i][j]>9:
                for n in neighbours(i, j, 10, 10):
                    squids[n[1]][n[0]] +=1
    for i,r in enumerate(squids):
        for j,c in enumerate(r):
            squids[i][j] += 1
            if squids[i][j]>9:
                squids[i][j]=0
                flashes += 1
print(flashes)
