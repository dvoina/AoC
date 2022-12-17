import re

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y



data = [[int(x) for x in re.findall(r"\d+", a.strip())] for a in open("day05.in").read().split("\n")]
data = [((a[0], a[1]),(a[2], a[3])) for a in data if (a[0]==a[2] or a[1]==a[3])]
intersections = set()
for i,l1 in enumerate(data):
    for j,l2 in enumerate(data[i+1:]):
        p = line_intersection(l1, l2)
        intersections.add(p)
print(len(intersections))