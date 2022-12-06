ll = [int(x) for x in open("input.txt").readlines()]
for i, v in enumerate(ll):
    for j, w in enumerate(ll[i+1:]):
        for k, x in enumerate(ll[j+1:]):
            if v+w+x==2020:
                print(v*w*x)
                