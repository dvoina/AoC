pos = {(-1, -1):8, (-1,0):8, (-1,1):6, (0,-1):5, (0,0):4, (0,1):3, (1, -1):2, (1, 0):1, (1,1):0}
def neigh(d, a, k):
    l,c = k
    r = 0
    for x,y in pos:
        if d.get((l+y,c+x))=='#':
            r += 1 << pos[(y,x)]
    return a[r]

_algo, _data = open("day20.in").read().split('\n\n')
algo = {i:_algo[i] for i in range(len(_algo))}
data = {(i,j):v for i,l in enumerate(_data.split()) for j,v in enumerate(l) if v=='#'}

print(algo, data)
_data = {}
print(len(data))
for a in range(2):
    for k in data.keys():
        if neigh(data, algo, k) == '#':
            _data[k] = '#'
    for k in _data.keys():
        data[k] = _data[k]
print(len(data))

