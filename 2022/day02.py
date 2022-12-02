#Rock, Paper, Scissors
s = {
    'X':{'A':(4, 3), 'B':(1, 1), 'C':(7, 2)},
    'Y':{'A':(8, 4), 'B':(5, 5), 'C':(2, 6)},
    'Z':{'A':(3, 8), 'B':(9, 9), 'C':(6, 7)}
}

encryptedBook = [tuple(l.strip().split(" ")) for l in open("2022/day02.txt").readlines()]

s1, s2 = 0, 0
for game in encryptedBook:
    s1 += s[game[1]][game[0]][0]
    s2 += s[game[1]][game[0]][1]
print(s1, s2)
