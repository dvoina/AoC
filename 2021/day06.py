
lf = [int(x) for x in open("day06.in").read().split(",")]
d={0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for i in lf:
    d[i] += 1

for i in range(80):
    d[(i + 7) % 9] += d[i % 9]
print(sum(d.values()), d)

for i in range(80, 256):
    d[(i + 7) % 9] += d[i % 9]
print(sum(d.values()), d)