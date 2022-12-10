instr = open("2022/day10.txt").read().split("\n")

x = {1:1}
cycle = 1
for i in instr:
    if i == "noop":
        v = x[cycle]
        cycle +=1
        x[cycle] = v
    if i.startswith("addx"):
        o = int(i[5:])
        v = x[cycle]
        x[cycle +1 ] = v 
        cycle +=2
        x[cycle] = v + o

pos = [20, 60, 100, 140, 180, 220]
s = 0
for p in pos:
    s += (p*x[p])

print(s) 

l=0
pixels = [[' ' for i in range (40)] for j in range(6)]

for pl in range(6):
    for pc in range(40):
        cycle = 40*pl + (pc+1)
        pv = [x[cycle]-1, x[cycle], x[cycle]+1]
        if pc in pv:
            pixels[pl][pc] = '#'

for l in pixels:
    print(''.join(l))


