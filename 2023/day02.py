import re
from collections import defaultdict

MR, MG, MB = 12, 13, 14

games = [l.split(':') for l in open('day02.in').read().strip().split('\n')]

sum = 0
for game in games:
    id = int(re.findall('\d+', game[0])[0])
    valid = True
    rounds = game[1].split(";")
    for r in rounds:
        d = defaultdict(int)
        values = re.findall("(\d+) (red|green|blue)", r)
        for v in values:
            d[v[1]] += int(v[0])
        if d['red'] > MR or d['green'] > MG or d['blue'] > MB:
            valid = False
            break
    if valid:
        sum += id
print(sum)

sum = 0
for game in games:
    id = int(re.findall('\d+', game[0])[0])
    rounds = game[1].split(";")
    d = defaultdict(int)
    for r in rounds:
        values = re.findall("(\d+) (red|green|blue)", r)
        for v in values:
            d[v[1]] = max(d[v[1]], int(v[0]))
    
    power = d['red'] * d['green'] * d['blue']
    sum += power
print(sum)