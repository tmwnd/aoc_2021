with open("data.txt") as file:
    tile = [[int(c) for c in line.strip()] for line in file.readlines()]
data = [[0 for _ in range(len(tile[0]) * 5)] for _ in range(len(tile) * 5)]

for i, line in enumerate(tile):
    for j, c in enumerate(line):
        for k in range(5):
            for l in range(5):
                data[i + len(tile)*k][j + len(tile[0])*l] = (c+k+l) % 10 + int(((c+k+l) - ((c+k+l) % 10)) / 10)

def print_dij(dij, p):
    for i, d in enumerate(dij):
        if i % p == 0:
            print()
        print(str(d).rjust(4), end=" ")
    print()

def ite_dij(data, dij, vis, q):
    x,y = [0,0]

    while dij[len(dij) - 1] == None:
        while ([x,y] in vis):
            p = q[min(q)]
            x, y = p[0]
            if (len(p) == 1):
                del q[min(q)]
            else:
                q[min(q)] = p[1:]

        for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
            if (x+dx >= 0 and x+dx < len(data) and y+dy >= 0 and y+dy < len(data[0])):
                i = x * len(data) + y
                di = (x+dx) * len(data) + (y+dy)
                if (dij[di] == None or dij[i] + data[x+dx][y+dy] < dij[di]):
                    dij[di] = dij[i] + data[x+dx][y+dy]
                    if dij[di] not in q:
                        q[dij[di]] = [[x+dx, y+dy]]
                    else:
                        q[dij[di]].append([x+dx, y+dy])

        vis.append([x, y])
    print(dij[len(dij) - 1])
    return dij

dij = [None for _ in range(len(data) * len(data[0]))]
dij[0] = 0
data[0][0] = 0

dij = ite_dij(data, dij, [], {0: [[0, 0]]})