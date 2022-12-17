pairs = [tuple(p.split("\n")) for p in open("2022/day13.txt").read().split("\n\n")]
pairs = [(eval(p[0]), eval(p[1])) for p in pairs]


from typing import Union

def compare(left, right) -> int:
    """Are the two packets in the right order? Return `None` if equal."""
    types = type(left), type(right)
    if types == (int, int):
        return left-right
    elif types == (int, list):
        return compare([left], right)
    elif types == (list, int):
        return compare(left, [right])
    else:
        for L, R in zip(left, right):
            result = compare(L, R)
            return result
        return (0 if len(left) == len(right) else len(left) - len(right))


s = 0
for i, p in enumerate(pairs):
    print(p)
    if compare(p[0], p[1])< 0:
        s += (i+1)
print(s)


signal = [[[2]], [[6]]]
for p in pairs:
    signal.extend(p[0])
    signal.extend(p[1])
print(signal)
import functools
import math
signal.sort(key=functools.cmp_to_key(lambda x,y: compare(x,y)))
p = signal.index([[2]])+1
p *= signal.index([[6]])+1
print(p)