import re

class Monkey(object):
    def __init__(self):
        self.number = 0
        self.items = []
        self.operation = ""
        self.test = 0
        self.mt = 0
        self.mf = 0
        self.activity = 0

    def ifTrue(self, o, monkeys:dict):
        print(f"Item with worry level {o} is thrown to monkey {self.mt}.")
        monkeys.get(self.mt).items.append(o)

    def ifFalse(self, o, monkeys: dict):
        print(f"Item with worry level {o} is thrown to monkey {self.mf}.")
        monkeys.get(self.mf).items.append(o)

    def round(self, monkeys:dict, part1):
        while self.items:
            w = self.items.pop()
            print(f"Monkey inspects an item with a worry level of {w}.")
            w = self._operation(w)
            if part1:
                w = w // 3
            print(f"Monkey gets bored with item. Worry level is divided by 3 to {w}.")
            if w % self.test == 0:
                print(f"Current worry level is divisible by {self.test}.")
                self.ifTrue(w, monkeys)
            else:
                print(f"Current worry level is not divisible by {self.test}.")
                self.ifFalse(w, monkeys)
            self.activity += 1

    def _operation(self, old):
        return eval(self.operation)
        
    def __str__(self):
        return f"""
        Monkey {self.number}:
          Starting items: {self.items}
          Operation: {self.operation}
          Test: divisible by {self.test}
            If true: throw to monkey {self.mt}
            If false: throw to monkey {self.mf}
          Activity: {self.activity} 
        """

    def __repr__(self):
        return str(self)

scripts = [tuple(s.split("\n")) for s in open("2022/day11.txt").read().split("\n\n")]
monkeys = {}

for s in scripts:
    m = Monkey()
    m.number = int(re.findall("\d+", s[0])[0])
    m.items = [int(x.strip()) for x in s[1].replace("  Starting items: ", "").split(",")]
    m.operation = s[2].replace("  Operation: new = ", "")
    m.test = int(re.findall("\d+", s[3])[0])
    m.mt = int(re.findall("\d+", s[4])[0])
    m.mf = int(re.findall("\d+", s[5])[0])
    print(m)
    monkeys[m.number] = m

# part 1
for _ in range(20):
    for m in sorted(monkeys.keys()):
        monkey = monkeys.get(m)
        monkey.round(monkeys, True)

top2 = sorted(monkeys.values(),key=lambda x: x.activity,reverse=True)[0:2]
print(top2[0].activity * top2[1].activity)

# part 2
for _ in range(1000):
    for m in sorted(monkeys.keys()):
        monkey = monkeys.get(m)
        monkey.round(monkeys, False)

top2 = sorted(monkeys.values(),key=lambda x: x.activity,reverse=True)[0:2]
print(top2[0].activity * top2[1].activity)