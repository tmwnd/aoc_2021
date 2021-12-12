from typing import BinaryIO


def flash(data, i, j):
    if data[i][j] != -1:
        data[i][j] += 1
        if data[i][j] == 10:
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

bitschalter = False
iteration = 0
while not bitschalter:
    iteration += 1
    for i in range(len(data)):
        for j in range(len(data[i])):
            flash(data, i, j)
    bitschalter = True
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == -1:
                data[i][j] = 0
            else:
                bitschalter = False
print(iteration)
