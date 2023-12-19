import re

def _eval_cond(a,b,c):
    if b == '<':
        return int(a)<int(c)
    if b == '>':
        return int(a)>int(c)
    
def _eval(k, p, workflows):
    for s in workflows[k]:
        if s == 'A':
            return 'A'
        if s == 'R':
            return 'R'
        _p = re.match(r"(?P<var>\w+)(?P<operator>[<=>])(?P<value>\d+):(?P<next>\w+)",s)
        if _p:
            _p = _p.groupdict()
            if _eval_cond(p[_p['var']], _p['operator'], _p['value']):
                return _eval(_p["next"], p, workflows)
            else:
                continue
        _p = re.match(r"(?P<next>\w+)",s).groupdict()
        return _eval(_p['next'], p, workflows) 
        


_workflows = {'A':'A', 'R':'R'}
workflows, parts = [x .split("\n") for x in open("day19.in").read().strip().split("\n\n")]
for i,w in enumerate(workflows):
    _w = re.match(r"(?P<id>\w+){(?P<rules>.*?)}", w).groupdict()
    _workflows[_w['id']]=_w['rules'].split(',')
for i,p in enumerate(parts):
    parts[i] = re.match(r"{x=(?P<x>\d+),m=(?P<m>\d+),a=(?P<a>\d+),s=(?P<s>\d+)}", p).groupdict()

s = 0
for p in parts:
    if _eval('in', p, _workflows) == 'A':
        s += sum([int(p[x]) for x in p])
print(s)