import re

R = re.compile("(\d+)-(\d+) ([a-z]): ([a-z]+)")
def p(l:str) -> int:
    m = R.match(l)
    if m != None:
        a,b,l,s = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
        count = 0
        for letter in s:
            if letter == l:
                count += 1
        if a<=count<=b:
            return 1
    return 0
def xor(a,b):
    return (not a and b) or (not b and a)

def q(l:str) -> int:
    m = R.match(l)
    if m != None:
        a,b,l,s = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
        if xor(s[a-1]==l,s[b-1]==l):
            return 1
    return 0

ll = sum([p(x) for x in open("input2.txt").readlines()])
print(ll)

ll = sum([q(x) for x in open("input2.txt").readlines()])
print(ll)


