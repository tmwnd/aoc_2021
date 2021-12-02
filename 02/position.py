position = [0, 0]

with open('data.txt') as data:
    for line in data:
        line = (line.split(" "))
        move = {
            "forward": [int(line[1]), 0],
            "up": [0, -int(line[1])],
            "down": [0, int(line[1])]
        }.get(line[0])

        for i in range(2):
            position[i] += move[i]
    print("Position: " + str(position) + " (" + str(position[0] * position[1]) + ")")