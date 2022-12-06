import math

with open("input13.txt") as f:
    ts=int(f.readline().strip())
    l=[(i, int(x)) for i,x in enumerate(f.readline().strip().split(",")) if x!='x']

print(ts,l)
bu=[]

for k in l:
    b=0
    while b<=ts:
        b += k[1]
    bu.append(b)
w = min(bu)
bus = bu.index(w)

print((w-ts)*l[bus][1])

M = math.lcm(*[x[1] for x in l])
n = min([x[1] for x in l])
k=0
while True:
    c = all(k%x[1]==x[0] for x in l)
    if c:
        break
    else:
        k += n
print(k)