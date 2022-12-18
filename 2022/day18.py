cubes = [tuple([int(y) for y in x.strip().split(',')]) for x in open("2022/day18.txt").readlines()]


min_x, max_x = min(cubes, key=lambda x: x[0])[0], max(cubes, key=lambda x: x[0])[0]
min_y, max_y = min(cubes, key=lambda y: y[1])[1], max(cubes, key=lambda y: y[1])[1]
min_z, max_z = min(cubes, key=lambda z: z[2])[2], max(cubes, key=lambda z: z[2])[2]


s = 0
for i, c in enumerate(cubes):
    faces = 6
    for j, d in enumerate(cubes):
        if c != d:
            if (abs(c[0]-d[0]) + abs(c[1]-d[1]) + abs(c[2]-d[2])) == 1:
                faces -= 1
    s+=faces
print(s)