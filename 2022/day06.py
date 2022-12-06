data = open("2022/day06.txt").read()

def allDifferent(a):
    return len(a) == len(set(a))

def detect(d, k):
    for i in range(len(d)-k):
        if allDifferent(data[i:i+k]):
            return i+k

print(detect(data, 4))
print(detect(data, 14))
