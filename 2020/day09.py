data = [int(l.strip()) for l in open("input9.txt").readlines()]
print(len(data))
for i in range(len(data)-26):
    preamble, n = data[i:i+25], data[i+25]
    lut = set()

    for x in preamble:
        for y in preamble:
            lut.add(x+y)

    if n not in lut:
        print(n)
        break
    
for size in range(2, len(data)):
    for i in range(len(data) - size):
        s = data[i:i+size]
        if sum(s) == n:
<<<<<<< HEAD
            print(min(s) + max(s))
=======
            print(min(s) + max(s))
            
>>>>>>> 9a85b6e (more)
