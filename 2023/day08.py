from collections import defaultdict
from functools import partial

import re
from math import lcm
seq, data = open("day08.in").read().strip().split("\n\n")

def part1(x):
    return x=="ZZZ"

def part2(x):
    return x[-1]=="Z"


nodes = defaultdict(dict)
for d in data.split("\n"):
    n,l,r =re.findall("\w{3}", d)
    nodes[n]["L"] = l
    nodes[n]["R"] = r


#Fancier for Ciprian's 
def moves(f, p):
    count = 0
    while not f(p):
        d = seq[count % len(seq)] 
        p = nodes[p][d]
        count += 1
    return count

print(moves(part1, "AAA"))

starts = [n for n in nodes if n[-1]=="A"]
lens = list(map(partial(moves, part2), starts))    
print(lcm(*lens))