data = [[int(x) for x in l.strip()] for l in open("day03.in").read().split()]
t = len(data)
n = len(data[0])
gamma = [0] * n
epsilon = [0] * n
for d in data:
    for i,r in enumerate(d):
        gamma[i] += r
print(gamma)
for i,d in enumerate(gamma):
    if d>int(t/2): 
        gamma[i]=1
        epsilon[i]=0
    else:
        gamma[i]=0
        epsilon[i]=1
gamma = int("".join([str(x) for x in gamma]), 2)
epsilon = int("".join([str(x) for x in epsilon]), 2)
print(gamma, epsilon, gamma*epsilon)
