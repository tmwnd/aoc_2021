MAX_ITERATIONS = 100
FLASHES = 0

def flash(data, i, j):
    if data[i][j] != -1:
        data[i][j] += 1
        if data[i][j] == 10:
            global FLASHES
            FLASHES += 1
            data[i][j] = -1
            rec_energy(data, i, j)

def rec_energy(data, i, j):
    for dx, dy in [[0,1],[1,0],[1,1],[1,-1]]:
        for k in [-1,1]:
            x = i+dx*k
            y = j+dy*k
            if x >= 0 and x < len(data) and y >= 0 and y < len(data[i]):
                flash(data, x, y)


with open("data.txt") as file:
    data = [[int(i) for i in line.strip()] for line in file.readlines()]

for _ in range(MAX_ITERATIONS):
    for i in range(len(data)):
        for j in range(len(data[i])):
            flash(data, i, j)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == -1:
                data[i][j] = 0

print(FLASHES)