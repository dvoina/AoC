from collections import defaultdict
import functools 

def clamp(v, minVal = 0, maxVal = 0):
    return min(max(minVal, v), maxVal)

def neighbours(t, N, M):
    pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for p in pos:
        yield (clamp(t[0]+p[0], maxVal=N), clamp(t[1]+p[1], maxVal=M))

symbols=set()
data = [l for l in open('day03.in').read().strip().split('\n')]
for l in data:
    for c in l:
        if not c.isdigit() and c != '.':
            symbols.add(c) 

N = len(data)-1
M = len(data[0])-1
print(data)

numbers = []
validNumbers = set()

for i, line in enumerate(data):
    j = 0
    isDigit = False
    l = 0
    while j<len(line):
        c = line[j]
        if c.isdigit():
            if isDigit:
                l += 1
            else:
                isDigit = True
                l += 1
        else:
            if isDigit:
                s = j - l
                numbers.append((i, s, j, int(line[s:j])))
                l = 0
                isDigit = False
        j += 1
print(numbers)


dd = defaultdict(set)                    
for number in numbers:
    l,s,e,v= number
    b = False 
    for c in range(s, e):
        for p in neighbours((l,c), N, M):
            s = data[p[0]][p[1]] 
            if s in symbols:
                b =  True
                dd[p].add(v)         
        if b:
            validNumbers.add(v)

print(sum(validNumbers))
s = 0
for k,v in dd.items():
    if len(v)==2:
        s += functools.reduce(lambda x,y: x*y, v)
print(s)