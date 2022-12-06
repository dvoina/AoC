def seat(s:str) -> int:
    r=int(s[:7].replace("B", "1").replace("F", "0"), 2)
    c=int(s[7:].replace("R", "1").replace("L", "0"), 2)
    return r*8+c

seats = [seat(l.strip()) for l in open("input5.txt").readlines()]
seats.sort()
print(max(seats))

for i in range(min(seats), max(seats)):
    if i not in seats:
        print(i)
