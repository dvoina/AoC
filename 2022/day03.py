data = [l.strip() for l in open("2022/day03.txt").readlines()]

# data = ["vJrwpWtwJgWrhcsFMMfFFhFp", 
# "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", 
# "PmmdzqPrVvPwwTWBwg", 
# "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
# "ttgJtRGJQctTZtZT",
# "CrZsJsPPZsGzwwsLwLmpwMDw"]

lc = range(ord('a'), ord('z')+1)
uc = range(ord('A'), ord('Z')+1)

def score(c):
    cc = ord(c)
    if cc in lc:
        return cc - 96
    if ord(c) in uc:
        return cc - 38
    return 0

#part 1
sum = 0
for bp in data:
    l = int(len(bp)/2)
    s1 = set(bp[:l])
    s2 = set(bp[l:])
    common = s1.intersection(s2)
    sum += score(list(common)[0])
print(sum)

#part2
sum = 0
for k in range(int(len(data)/3)):
    s1 = set(data[3*k])
    s2 = set(data[3*k+1])
    s3 = set(data[3*k+2])
    common = s1.intersection(s2).intersection(s3)
    sum += score(list(common)[0])
print(sum)