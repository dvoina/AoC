groups = [g.split("\n") for g in open("input6.txt").read().split("\n\n")]

total = 0
for g in groups:
    answers = set("".join(g))
    total += len(answers)

print(total)

total = 0
for g in groups:
    answ = []
    for p in g:
        a = set(p)
        answ.append(a)
    aa = answ[0]
    for a in answ:
        aa.intersection_update(a)
    total += len(aa)

print(total)    
