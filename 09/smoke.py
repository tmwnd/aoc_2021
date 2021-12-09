with open("data.txt") as file:
    data = [[int(h) for h in line.strip()] for line in file.readlines()]

val = 0

for i in range(len(data)):
    for j in range(len(data[0])):
        small = data[i][j]
        for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
            x = i + dx
            y = j + dy
            if x >= 0 and x < len(data) and y >= 0 and y < len(data[0]):
                if small >= data[x][y]:
                    small = -1
        if small == data[i][j]:
            val += small + 1

print(val)