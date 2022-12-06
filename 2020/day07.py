import re
from collections import defaultdict

RE = re.compile(r"(\d+) (.*?) bags?")

def traverse1(d, x, s):
    if d[x]:
        for p in d[x]:
            s.add(p)
            traverse1(d, p, s)

def traverse2(d, x):
    print(x, d[x],)
    if d[x] == {}:
        return 1
    sum = 0    
    for k,v in d[x].items():
        sum += v * traverse2(d, k)
    return sum + 1

data = dict([(a.strip().split(" bags contain ")[0], a.strip().split("contain")[1].split(",")) for a in open("input7.txt").readlines()])
parents = defaultdict(set)
for k,v in data.items():
    x = {}
    for e in v:
        m = RE.match(e.strip())
        if m != None:
            parents[m.group(2)].add(k)
            x[m.group(2)] = int(m.group(1))
    data[k] = x


ss=set()
traverse1(parents, "shiny gold", ss)
print(len(ss))
print(traverse2(data, "shiny gold")-1)
