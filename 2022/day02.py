#Rock, Paper, Scissors
s1 = {
    'X':{'A':4, 'B':1, 'C':7},
    'Y':{'A':8, 'B':5, 'C':2},
    'Z':{'A':3, 'B':9, 'C':6}
}


s2 = {
    'X':{'A':3, 'B':1, 'C':2},
    'Y':{'A':4, 'B':5, 'C':6},
    'Z':{'A':8, 'B':9, 'C':7}
}

encryptedBook = [tuple(l.strip().split(" ")) for l in open("2022/day02.txt").readlines()]

t1 = 0 
t2 = 0
for game in encryptedBook:
    t1 += s1[game[1]][game[0]]
    t2 += s2[game[1]][game[0]]
print(t1, t2)
