series = [[int(x) for x in l.split()] for l in open("day09.in").readlines()]

def derivative(s):
    r=[]
    n = len(s)
    for i in range(1,n):
        r.append(s[i]-s[i-1])
    return r

def allZero(s):
    return all([x==0 for x in s])

def solve(s):
    if not allZero(s):
        return s[-1] + solve(derivative(s))
    else:
        return 0

def solve2(s):
    if not allZero(s):
        return s[0] - solve2(derivative(s))
    else:
        return 0


s = sum(map(solve, series))
print(s)

s = sum(map(solve2, series))
print(s)
