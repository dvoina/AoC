trees = [[int(x) for x in l.strip()] for l in open("2022/day08.txt").readlines()]

nl = len(trees)
nc = len(trees[0])

def isVisible(l, c, _t):
    vl = True
    for _c in range(c):
        vl = vl and _t[l][_c]<_t[l][c]
    
    vr = True
    for _c in range(c+1, nc):
        vr = vr and _t[l][_c]<_t[l][c]

    vt = True
    for _l in range(l):
        vt = vt and _t[_l][c]<_t[l][c]

    vb = True
    for _l in range(l+1, nl):
        vb = vb and _t[_l][c]<_t[l][c]
    
    return vl or vr or vt or vb

def clamp(x):
    return max(x,1)

def score(l, c, _t):
    val = _t[l][c]

    p=1
    
    cnt = 0
    i = c-1
    while i>=0:
        if _t[l][i]<val:
            cnt += 1
            i -= 1
        else:
            if _t[l][i]>=val: 
                cnt +=1
                break

    p *= clamp(cnt)

    cnt = 0
    i = c+1
    while i<nc:
        if _t[l][i]<val:
            cnt += 1
            i += 1
        else:
            if _t[l][i]>=val: 
                cnt +=1
                break
    p *= clamp(cnt)

    cnt = 0
    i = l-1
    while i>=0:
        if _t[i][c]<val:
            cnt += 1
            i -= 1
        else:
            if _t[i][c]>=val: 
                cnt +=1
                break
    p *= clamp(cnt)

    cnt = 0
    i = l+1
    while i<nl:
        if _t[i][c]<val:
            cnt += 1
            i += 1
        else:
            if _t[i][c]>=val: 
                cnt +=1
                break
    p *= clamp(cnt)


    return p

# part 1
# s = 0
# for l in range(1,nl-1):
#     for c in range(1,nc-1):
#         if(isVisible(l,c,trees)):
#             s += 1
# print(s + 2*nl + 2*(nc-2))

# part 2


maxScore = 0
for l in range(1,nl-1):
    for c in range(1,nc-1):
        if(score(l,c,trees)>maxScore):
            maxScore = score(l,c,trees)
            print (l, c)
print(maxScore)