#Rock, Paper, Scissors
scores = {'X':1, 'Y':2, 'Z':3}

wins = { 'A':'Y', 'B':'Z', 'C':'X'}
draws = {'A':'X', 'B':'Y', 'C':'Z'}
loses = {'A':'Z', 'B':'X', 'C':'Y'}

encryptedBook = [tuple(l.strip().split(" ")) for l in open("day02.txt").readlines()]

#encryptedBook = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]

#part 1
total = 0
for game in encryptedBook:
    score = 0
    if game[1] == wins[game[0]]:
        score = 6
    if game[1] == draws[game[0]]:
        score = 3
    score += scores[game[1]]
    total += score
print(total)

#part 2
total = 0
for game in encryptedBook:
    score = 0
    if game[1] == 'X':
        c = loses[game[0]]
    if game[1] == 'Y':
        score += 3
        c = draws[game[0]]
    if game[1] == 'Z':
        score += 6
        c = wins[game[0]]
    score += scores[c] 
    total += score
print(total)
