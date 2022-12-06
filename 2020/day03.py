data = [list(l.strip()) for l in open("input3.txt").readlines()]

def solve(data: list, dx:int, dy:int) -> int:
    count, x, y, m, n = 0, 0, 0, len(data), len(data[0])
    while y<m:
        if data[y][x % n] == "#":
            count += 1
        x += dx
        y += dy
    return count
 
print(solve(data, 3, 1))

print(solve(data, 1, 1)*solve(data, 3, 1)*solve(data,5,1)*solve(data,7,1)*solve(data,1,2))
#for l in data:
#    print("".join(l))
