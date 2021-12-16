with open("data.txt") as file:
    data = [[int(c) for c in line.strip()] for line in file.readlines()]

def print_dij(dij, p):
    for i, d in enumerate(dij):
        if i % p == 0:
            print()
        print(str(d).rjust(4), end=" ")
    print()

def rec_dij(data, dij, x, y, vis):
    if None not in dij:
        return dij
    for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
        if (x+dx >= 0 and x+dx < len(data) and y+dy >= 0 and y+dy < len(data[0])):
            i = x * len(data) + y
            di = (x+dx) * len(data) + (y+dy)
            if (dij[di] == None or dij[i] + data[x+dx][y+dy] < dij[di]):
                dij[di] = dij[i] + data[x+dx][y+dy]
    low = 10E5
    pos = 0
    for i, _ in enumerate(dij):
        if (dij[i] != None and dij[i] < low and i not in vis):
            low = dij[i]
            pos = i
    vis.append(pos)
    x = int((pos - (pos % len(data))) / len(data))
    y = pos % len(data)
    #print_dij(dij, len(data))
    return rec_dij(data, dij, x, y, vis)

def ite_dij(data, dij, x, y, vis):
    if None not in dij:
        return dij
    for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
        if (x+dx >= 0 and x+dx < len(data) and y+dy >= 0 and y+dy < len(data[0])):
            i = x * len(data) + y
            di = (x+dx) * len(data) + (y+dy)
            if (dij[di] == None or dij[i] + data[x+dx][y+dy] < dij[di]):
                dij[di] = dij[i] + data[x+dx][y+dy]
    low = 10E5
    pos = 0
    for i, _ in enumerate(dij):
        if (dij[i] != None and dij[i] < low and i not in vis):
            low = dij[i]
            pos = i
    vis.append(pos)
    x = int((pos - (pos % len(data))) / len(data))
    y = pos % len(data)
    return dij, x, y, vis        
    

dij = [None for _ in range(len(data) * len(data[0]))]
dij[0] = 0
data[0][0] = 0
vis = [0]

x = 0
y = 0

#dij = rec_dij(data, dij, 0, 0, vis)
while(None in dij):
    dij, x, y, vis = ite_dij(data, dij, x, y, vis)

print(dij[len(dij) - 1])