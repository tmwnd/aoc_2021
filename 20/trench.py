ITERATIONS = 50

from os import read

def print_data(data):
    for line in data:
        for c in line:
            print("#" if c else ".", end="")
        print()

with open("data.txt") as file:
    data = file.readlines()

dict = [c == "#" for c in data[0].strip()]
data = [[c == "#" for c in line.strip()] for line in data[2:]]

#print_data(data)

lit = False

for _ in range(ITERATIONS):
    new_data = []
    for i in range(-1, len(data) + 1):
        new_data.append([])
        for j in range(-1, len(data[0]) + 1):
            val = 0
            for k in range(9):
                i_, j_ = i + int(k / 3) - 1, j + k % 3 - 1
                val += pow(2, 8-k) * (data[i_][j_] if i_ >= 0 and i_ < len(data) and j_ >= 0 and j_ < len(data[0]) else (int(dict[0]) if lit else 0))
            new_data[i + 1].append(dict[val])
    lit = not lit
    data = new_data
    # print()
    # print_data(data)

print_data(data)

print(sum([sum(line) for line in data]))