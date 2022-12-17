moves = [m for m in open("2022/day17.txt").read().strip()]

print(moves)

r0 = [('#', "#", "#", "#")]
r1 = [('.', '#', '.'), ('#', '#', '#'), ('.', '#', '.')]
r2 = [('.', ',', '#'), ('.', ',', '#'), ('#', '#', '#')]
r3 = [('#'), ('#'), ('#'), ('#')]
r4 = [('#', '#'), ('#', '#')]
rocks = [r0, r1, r2, r3, r4]

for i in range(2023):
    rock = rocks[i % len(rocks)]
    blocked = False
    while not blocked:
        move = moves.pop(0)
        
