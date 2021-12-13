def print_matrix(matrix):
    for line in matrix:
        for c in line:
            print("#" if c else ".", end="")
        print()

with open("data.txt") as file:
    data = [line.strip() for line in file.readlines()]

ins = []
while True:
    index = len(data) - 1
    if data[index] == "":
        data.pop(index)
        break
    ins.append(data.pop(index))
ins = ins[::-1]

data = [[int(p) for p in line.split(",")] for line in data]

x_max = max([x[0] for x in data])
y_max = max([y[1] for y in data])
matrix = [[False for _ in range(x_max + 1)] for _ in range(y_max + 1)]

for x, y in data:
    matrix[y][x] = True
#print_matrix(matrix)

for i in ins:
    #print()
    if "x" in i:
        dx = int(i.split("x=")[1])
        new_matrix = [[False for _ in range(dx)] for _ in range(len(matrix))]
        for x in range(len(new_matrix[0])):
            for y in range(len(new_matrix)):
                new_matrix[y][x] = matrix[y][x] or matrix[y][dx + len(new_matrix[0]) - x]
    if "y" in i:
        dy = int(i.split("y=")[1])
        new_matrix = [[False for _ in range(len(matrix[0]))] for _ in range(dy)]
        for x in range(len(new_matrix[0])):
            for y in range(len(new_matrix)):
                new_matrix[y][x] = matrix[y][x] or matrix[dy + len(new_matrix) - y][x]
    matrix = new_matrix
    #print_matrix(new_matrix)
    break

print(sum([sum(line) for line in matrix]))