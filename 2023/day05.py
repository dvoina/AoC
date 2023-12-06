from collections import defaultdict

data = open('day05.in').read().strip().split('\n\n')
seeds = [int(x) for x in data[0].split(':')[1].split()]
maps = [m.split('\n') for m in data[1:]]
tables = {}

for i, m in enumerate(maps):
    name=m[0].split()[0]
    ranges = [[int (x) for x in v.split()] for v in m[1:]]
    maps[i] = (name,ranges)
_maps = defaultdict(dict)
_inv_maps = defaultdict(dict)
for m in maps:
    f,t = m[0].split('-to-')
    _maps[f][t]=m[1]
    _inv_maps[t][f]=m[1]

def transf(v, m):
    res = v
    for r in m:
        if r[1] <= v <= r[1] + r[2]:
            res = r[0] + (v-r[1]) 
            break
    return res

def inv_transf(v, m):
    res = v
    for r in m:
        if r[0] <= v <= r[0] + r[2]:
            res = r[1] + (v-r[0]) 
            break
    return res
    
locations = []
for s in seeds:
    soil = transf(s, _maps['seed']['soil'])
    fertilizer = transf(soil, _maps['soil']['fertilizer'])
    water = transf(fertilizer, _maps['fertilizer']['water'])
    light = transf(water, _maps['water']['light'])
    temperature = transf(light, _maps['light']['temperature'])
    humidity = transf(temperature, _maps['temperature']['humidity'])
    location = transf(humidity, _maps['humidity']['location'])
    locations.append(location)
print(min(locations))

seeds = []
locations = min(_inv_maps["location"]["humidity"][0])
for r in _inv_maps["location"]["humidity"]:
    print('.', end='')
    for x in [r[0], r[0]+r[2]]:
        humidity = inv_transf(x, _inv_maps['location']['humidity'])
        temperature = inv_transf(humidity, _inv_maps['humidity']['temperature'])
        light = inv_transf(temperature, _inv_maps['temperature']['light'])
        water = inv_transf(light, _inv_maps['light']['water'])
        fertilizer = inv_transf(water, _inv_maps['water']['fertilizer'])
        soil = inv_transf(fertilizer, _inv_maps['fertilizer']['soil'])
        seed = transf(soil, _inv_maps['soil']['seed'])
        seeds.append(seed)
print(seeds)
 