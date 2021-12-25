with open("data.txt") as file:
    data = [[c for c in line.strip()] for line in file.readlines()]

def print_data(data):
    for line in data:
        for c in line:
            print(c, end="")
        print()

def move_h(line):
    ret = False
    i = 0
    while i < len(line):
        if line[i] == '>' and line[i+1 if i+1<len(line) else 0] == '.':
            line[i] = '.' if i != 0 else 'x'
            line[i+1 if i+1<len(line) else 0] = '>'
            i += 1
            ret = True
        i += 1
    if line[0] == 'x':
        line[0] = '.'
    return ret

def move_v(data, index):
    ret = False
    i = 0
    while i < len(data):
        if data[i][index] == 'v' and data[i+1 if i+1<len(data) else 0][index] == '.':
            data[i][index] = '.' if i != 0 else 'x'
            data[i+1 if i+1<len(data) else 0][index] = 'v'
            i += 1
            ret = True
        i += 1
    if data[0][index] == 'x':
        data[0][index] = '.'
    return ret

steps = 1
bitschalter = True
while bitschalter == True:
    bitschalter = False

    for line in data:
        bitschalter = move_h(line) or bitschalter

    for i in range(len(data[0])):
        bitschalter = move_v(data, i) or bitschalter
    steps += 1

#print_data(data)
print(steps - 1)