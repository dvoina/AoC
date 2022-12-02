calories = [sum([int(k) for k in c.split("\n")]) for c in open("day01.txt").read().split("\n\n")]
calories.sort(reverse=True)
print(calories[0])
print(sum(calories[0:3]))



