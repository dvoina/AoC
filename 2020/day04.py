import re
batch = [l.strip() for l in open("input4.txt").readlines()]


class Rule(object):
    def validate(self, value) -> bool:
        return value != None

class cid(Rule):
    def validate(self, value) -> bool:
        return True

class pid(Rule):
    def validate(self, value) -> bool:
        if not Rule.validate(self, value):
            return False
        m = re.compile("\d{9}").match(value)
        return m != None

class ecl(Rule):
    def validate(self, value) -> bool:
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

class hcl(Rule):
    def validate(self, value) -> bool:
        if not Rule.validate(self, value):
            return False
        m = re.compile("#[0-9a-f]{6}").match(value)
        return m != None

class byr(Rule):
    def validate(self, value) -> bool:
        if not Rule.validate(self, value):
            return False
        return 1920 <= int(value) <= 2020

class iyr(Rule):
    def validate(self, value) -> bool:
        if not Rule.validate(self, value):
            return False
        return 2010 <= int(value) <= 2020

class eyr(Rule):
    def validate(self, value) -> bool:
        if not Rule.validate(self, value):
            return False
        return 2020 <= int(value) <=2030

class hgt(Rule):
    def validate(self, value) -> bool:
        if not Rule.validate(self, value):
            return False
        m = re.compile("(\d+)(cm|in)").match(value)
        if m != None:
            h = int(m.group(1))
            u = m.group(2)
            if u == "cm":
                return 150 <= h <=193
            if u == "in":
                return 59 <= h <= 76
        return False

mandatory = {"byr":byr(), "eyr":eyr(), "iyr":iyr(), "hgt":hgt(), "hcl":hcl(), "ecl":ecl(), "pid":pid(), "cid": cid()}


def validate(p):
    for f in mandatory.keys():
        rule = mandatory.get(f)
        value = p.get(f)
        if not rule.validate(value):
            print("{} has bad {}".format(p, f))
            return False
    return True

passport = {}
count = 0
for l in batch:
    if l=="":
        if validate(passport):
            count += 1
        passport ={}
        continue
    kp = l.split(" ")
    for f in kp:
        ff = f.split(":")
        passport[ff[0]]=ff[1]

print(count)
