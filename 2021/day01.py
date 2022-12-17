# data = [int(x) for x in open('day01.in').read().split()]
# delta = []
# for i in range(len(data)-1):
#     if data[i+1]-data[i]>=0:
#         delta.append(1)
#     else:
#         delta.append(0)
# print(sum(delta))

# data2=[]
# delta = []
# n=len(data)-(len(data)%3)
# for i in range(n):
#     s = sum(data[i:i+3])
#     data2.append(s)
# for i in range(len(data2)-2):
#     if data2[i+1]-data2[i]>=0:
#         delta.append(1)
#     else:
#         delta.append(0)
# print(sum(delta)-1)

from itertools import pairwise
from more_itertools import windowed

with open("day01.in") as f:
    depths = [int(x) for x in f]

print(sum(b > a for a, b in pairwise(depths)))
print(sum(sum(b) > sum(a) for a, b in pairwise(windowed(depths, 3))))