import re
data = open("2022/day21.txt").read().strip().split("\n")
code = []
for l in data:
    l = "def " + re.sub("([a-z]{4})", r"\1()", l)
    l = l.replace(":", ": return")
    code.append(l)
code = "\n".join(code)
print(code)
exec(code)
print(root())
