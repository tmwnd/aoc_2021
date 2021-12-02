position = [0, 0]

with open('data.txt') as data:
    line = data.readline()
    while line:
        line = (line.split(" "))
        move = {
            "forward": [int(line[1]), 0],
            "up": [0, -int(line[1])],
            "down": [0, int(line[1])]
        }.get(line[0])

        for i in range(2):
            position[i] += move[i]

        line = data.readline()
    print("Position: " + str(position) + " (" + str(position[0] * position[1]) + ")")