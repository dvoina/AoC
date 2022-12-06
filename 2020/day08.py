_code =[l.strip().split() for l in open("input8.txt").readlines()]

def run(code, patch = None):
    executed = set()
    if patch != None:
        code[patch[0]][0] = patch[1]
    acc = 0
    pc = 0
    while pc<len(code):
        i = code[pc]
        if pc in executed:
            print("LOOP")
            return acc
        executed.add(pc)
        if i[0] == "nop":
            pc +=1
            continue
        if i[0] == "acc":
            acc += int(i[1])
            pc += 1
            continue
        if i[0] == "jmp":
            pc += int(i[1])
            continue
    print("OK")
    return acc

cc = _code[:]
print(run(cc[:]))

patches = []
for p,i in enumerate(_code):

    if i[0]=="nop":
        patch = (p, "jmp")
        patches.append(patch)
        continue 
    
    if i[0]=="jmp":
        patch = (p, "nop")
        patches.append(patch)
        continue 

for p in patches:
    cc = _code[:]
    print(run(cc[:], p))
