def cf1(a,b):
    return abs(a-b)

def cf2(a,b):
    n = abs(a-b)
    return n*(n+1)//2

data = [int(x) for x in open("day07.in").read().split(",")]
#data=[16,1,2,0,4,2,7,1,2,14]
data.sort()
m = data[len(data)//2]
p1 = sum([cf1(x,m) for x in data])
print(p1)

dd = []
for p in data:
    dd.append(sum([cf2(p,x) for x in data]))
print(min(dd))