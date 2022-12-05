import re
a,b = open("2022/day05.txt").read().rstrip().split("\n\n")
initial = a.split("\n")
initial.reverse()
moves = b.split("\n")

stacks = {int(k):[] for k in re.findall("\d+", initial[0])}

l = len(stacks)
for level in initial[1:]:
    for index in range(l):
        token = re.findall("\w", level[4*index:4*index+3])
        if token != []:
            stacks[index+1].append(token[0])

for i, move in enumerate(moves):
    moves[i] = tuple([int(x) for x in re.findall("\d+", move)])

def move1(count:int, src:int, dst:int):
    for i in range(count):
        value = stacks[src].pop()
        stacks[dst].append(value)

def move2(count:int, src:int, dst:int):
    vv = []
    for i in range(count):
        vv.append(stacks[src].pop())
    vv.reverse()
    stacks[dst].extend(vv)

# for m in moves:
#     move1(m[0], m[1], m[2])
# print(stacks)

for m in moves:
    move2(m[0], m[1], m[2])
print(stacks)

s = ""
for index in range(1, 10):
    if len(stacks[index]) > 0:
        s+=stacks[index][-1]
print(s)