order = ['A','B','C','D']
amphipods = {c: pow(10, i) for i, c in enumerate(order)}
max_energy = 10E7

def pos_moves(start, space):
    ret = []
    i = start*2 + 2
    if space[i]:
        return ret
    for k in -1,1:
        while i >= 0 and i < len(space) and not space[i]:
            ret.append(i)
            i += k
        i = start*2 + 3
    return ret

def pos_homes(start, space):
    i = start*2 + 2
    if space[i]:
        return [i]
    ret = []
    for k in -1,1:
        while i >= 0 and i < len(space):
            if space[i]:
                ret.append(i)
                break
            i += k
        i = start*2 + 3
    return ret

data = [[] for _ in amphipods]
space = [None for _ in range(11)]

with open("data.txt") as file:
    for line in file.readlines()[2:4]:
        i = 0
        for c in line:
            if c in amphipods:
                data[i].append(c)
                i += 1

for i in range(len(data)):
    if data[i][1] == order[i]:
        data[i] = [data[i][0]]

def rec_move(data, space, energy):
    global max_energy

    if energy >= max_energy:
        return

    last_energy = energy
    for _ in range(len(data)):
        for i in range(len(data)):
            if len(data[i]) > 0 and data[i][0] == None:
                for home in pos_homes(i, space):
                    if space[home] == order[i]:
                        energy += (abs(home - i*2 - 2) + len(data[i])) * amphipods[order[i]]
                        space[home] = None
                        data[i] = data[i][:len(data[i])-1]

        if energy == last_energy:
            break
        last_energy = energy

        if energy >= max_energy:
            return

    if sum([len(x) != 0 for x in data]) == 0:
        max_energy = energy
        print(energy)
        return

    for i in range(len(data)):
        if len(data[i]) == 0 or data[i][0] == None:
            continue

        for move in pos_moves(i, space):
            rec_move(
                [([None] if len(x) == 1 else [x[1], None]) if j == i else x.copy() for j, x in enumerate(data)],
                [data[i][0] if j == move else x for j, x in enumerate(space)],
                energy + (amphipods[data[i][0]] * (abs(move - i*2 - 2) + 1) if data[i][0] else 0) + (0 if len(data[i]) == 1 or not data[i][1] else amphipods[data[i][1]])
            )

print(data)

rec_move(data, space, 0)
print(max_energy)