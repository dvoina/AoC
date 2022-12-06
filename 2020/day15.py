from collections import defaultdict

data = [1, 20, 8, 12, 0, 14]
#data = [0,3,6]

d = defaultdict(list)
for i,x in enumerate(data):
    d[x].append(i+1)

n=0
for i in range(len(data)+1, 2020):
    if n in d:
        d[n].append(i)
        n = d[n][-1]-d[n][-2]
    else:
        d[n].append(i)
        n = 0
print(n)
for i in range(2020, 30000000):
    if n in d:
        d[n].append(i)
        n = d[n][-1]-d[n][-2]
    else:
        d[n].append(i)
        n = 0
print(n)


    