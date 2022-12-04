pairs = [tuple(pair.split(',')) for pair in open("2022/day04.txt").read().strip().split("\n")]
vals= []

def contained(a:str,b:str) -> bool:
    a,b=[int(x) for x in a.split("-")], [int(x) for x in b.split("-")]
    if (a[0]>=b[0]) and (a[1]<=b[1]):
        return True
    return False

def overlaps(a:str,b:str) -> bool:
    a,b=[int(x) for x in a.split("-")], [int(x) for x in b.split("-")]
    if a[1] < b[0]:
        return False
    if b[1] < a[0]:
        return False
    return True

#part 1
count = 0 
for pair in pairs:
    a,b = pair
    if contained(a,b) or contained(b,a):
        count += 1
print(count)

#part 2
count = 0 
for pair in pairs:
    a,b = pair
    if overlaps(a,b):
        count += 1
print(count)

