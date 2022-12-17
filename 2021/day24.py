class CPU(object):
    def __init__(self) -> None:
        self.regs={'w':0, 'x':0, 'y':0, 'z':0}
    
    def execute(self, code, _input):
        k = 0
        for tokens in code:
            if tokens[0] == 'inp':
                self.regs[tokens[1]] = int(_input[k])
                k = k + 1
                continue
            op1, op2 = tokens[1:]
            if op1 in ['w', 'x', 'y', 'z']:
                op1 = self.regs[op1]
            else:
                op1 = int(op1)
            if op2 in ['w', 'x', 'y', 'z']:
                op2 = self.regs[op2]
            else:
                op2 = int(op2)
            if tokens[0] == 'add':
                self.regs[tokens[1]] = int(op1 + op2)
                continue
            if tokens[0] == 'sub':
                self.regs[tokens[1]] = int(op1 - op2)
                continue
            if tokens[0] == 'mul':
                self.regs[tokens[1]] = int(op1 * op2)
                continue
            if tokens[0] == 'div':
                self.regs[tokens[1]] = int(op1 // op2)
                continue
            if tokens[0] == 'mod':
                self.regs[tokens[1]] = int(op1 % op2)
                continue
            if tokens[0] == 'eql':
                if op1 == op2:
                    self.regs[tokens[1]] = 1
                else:
                    self.regs[tokens[1]] = 0
                continue
    def valid(self):
        return self.regs['z'] == 0


code = [[token.strip() for token in instr.split()] for instr in open('day24.in').readlines()]

_min=10000000000000
_max=19999999999999
cont = True
while cont:
    v = int((_min + _max)/2)
    print(v)
    cpu = CPU()
    cpu.execute(code, str(v))
    if cpu.valid():
        _min = v
        cont = True
    else:
        _max = v
        cont = True
    if _min==_max:
        cont = False

