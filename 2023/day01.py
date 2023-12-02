digits = set([str(i) for i in range(10)])
digits2 = {'one':'o1e', 'two':'t2o', 'three':'th3ee', 'four':'fo4r', 'five':'fi5e', 'six':'s6x', 'seven':'se7en', 'eight':'ei8ht', 'nine':'ni9e'}

nums = [[int(x) for x in l if x in digits] for l in open("day01.in").readlines()]
s = sum([10*n[0]+n[-1] for n in nums if len(n)>0])
print(s)

text = [l.strip() for l in  open("day01.in").readlines()]
for i, l in enumerate(text):
    for d in digits2:
        l = l.replace(d, digits2[d])
    text[i] = l
nums = [[int(x) for x in l if x in digits] for l in text]
s = sum([10*n[0]+n[-1] for n in nums])
print(s)
