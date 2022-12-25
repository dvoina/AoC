snafu = [x.strip() for x in open("2022/day25.txt").read().split("\n")]

def toInt(x:str) -> int:
    s2i = {'=':-2, '-':-1, '0':0, '1':1, '2':2}
    n=0
    p = len(x)
    for i,d in enumerate(reversed(x)):
        n += s2i[d]*5**i
    print(n)
    return n

def toSnafu(x:int) -> str:
    i2s = {4:'-', 3:'=', 0:'0', 1:'1', 2:'2'}
    s = ''
    while x != 0:
        rem = x % 5
        s = i2s[rem] + s
        if rem > 2:
            x += 5 - rem
        x //= 5
    return s

sum=0
for x in snafu:
    sum += toInt(x)
print(toSnafu(sum))

