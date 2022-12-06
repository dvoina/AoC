card=17607508
door=15065270
divisor=20201227

c = 0
while True:
    if pow(7, c, divisor) == card:
        break
    c += 1
print(pow(door, c, divisor))