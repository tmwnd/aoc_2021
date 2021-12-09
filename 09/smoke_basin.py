def rec_calc_basin_size(data, x, y):
    val = 1
    if data[x][y] == 9:
        return 0
    data[x][y] = 9
    for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
        if x+dx >= 0 and x+dx < len(data) and y+dy >= 0 and y+dy < len(data[0]):
            if data[x+dx][y+dy] != 9:
                val += rec_calc_basin_size(data, x+dx, y+dy)
    return val


with open("data.txt") as file:
    data = [[int(h) for h in line.strip()] for line in file.readlines()]

basins = []

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] != 9:
            basins.append(rec_calc_basin_size(data, i, j))

val = 1
for x in sorted(basins)[-3:]:
    val *= x
print(val)
            
            
