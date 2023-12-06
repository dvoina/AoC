import re
import math
data = open('day06.in').read().strip().split('\n')
times = [int(x) for x in re.findall('\d+', data[0])]
distances = [int(x) for x in re.findall('\d+', data[1])]
wins= []
for i, t in enumerate(zip(times, distances)):
    w = 0
    for pTime in range(t[0]):
        if pTime*(t[0]-pTime)>t[1]:
            w += 1
    wins.append(w)
print(math.prod(wins))

time = int("".join(re.findall('\d+', data[0])))
dist = int("".join(re.findall('\d+', data[1])))
print(time, dist)

w=0
for pTime in range(time):
    if pTime*(time-pTime) > dist:
        w += 1
print(w)
