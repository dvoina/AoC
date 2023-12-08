from collections import defaultdict
import re
from math import lcm
seq, data = open("day08.in").read().strip().split("\n\n")

nodes = defaultdict(dict)
for d in data.split("\n"):
    n,l,r =re.findall("\w{3}", d)
    nodes[n]["L"] = l
    nodes[n]["R"] = r

p = "AAA"
count = 0
while p!="ZZZ":
    d = seq[count % len(seq)] 
    p = nodes[p][d]
    count += 1
print(count)


def moves(p):
    count = 0
    while p[-1]!="Z":
        d = seq[count % len(seq)] 
        p = nodes[p][d]
        count += 1
    return count

starts = [n for n in nodes if n[-1]=="A"]
lens = list(map(moves, starts))    
print(lcm(*lens))