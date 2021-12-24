order = ['A','B','C','D']
amphipods = {c: pow(10, i) for i, c in enumerate(order)}
max_energy = -1

def pos_moves(start, space):
    ret = []
    i = start*2 + 2
    if space[i]:
        return ret
    for k in -1,1:
        while i >= 0 and i < len(space) and not space[i]:
            if i not in [2,4,6,8]:
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

def rot(x):
    ret = []
    for i, e in enumerate(x):
        if i > 0:
            ret.append(e)
    ret.append(None)
    return ret

data = [[] for _ in amphipods]
space = [None for _ in range(11)]

with open("data.txt") as file:
    f = file.readlines()
    for line in f[2:len(f)-1]:
        i = 0
        for c in line:
            if c in amphipods:
                data[i].append(c)
                i += 1

pre = [['D','D'],['C','B'],['B','A'],['A','C']]
for i in range(len(data)):
    data[i] = [data[i][0], pre[i][0], pre[i][1], data[i][1]]

for _ in range(len(data)):
    for i in range(len(data)):
        if data[i][len(data[i])-1] == order[i]:
            data[i] = data[i][:len(data[i])-1]

def rec_move(data, space, energy):
    global max_energy

    if energy >= max_energy and max_energy != -1:
        return

    last_energy = energy
    for _ in range(len(data)):
        for i in range(len(data)):
            bitschalter = True
            for d in data[i]:
                if d:
                    bitschalter = False
                    break
            if bitschalter:
                for home in pos_homes(i, space):
                    if space[home] == order[i]:
                        energy += (abs(home - i*2 - 2) + len(data[i])) * amphipods[order[i]]
                        space[home] = None
                        data[i] = data[i][:len(data[i])-1]

        if energy == last_energy:
            break
        last_energy = energy

        if energy >= max_energy and max_energy != -1:
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
                [rot(x) if j == i else x.copy() for j, x in enumerate(data)],
                [data[i][0] if j == move else x for j, x in enumerate(space)],
                energy + (amphipods[data[i][0]] * (abs(move - i*2 - 2) + 1) if data[i][0] else 0)
                    + (amphipods[data[i][1]] if len(data[i]) > 1 and data[i][1] else 0)
                    + (amphipods[data[i][2]] if len(data[i]) > 2 and data[i][2] else 0)
                    + (amphipods[data[i][3]] if len(data[i]) > 3 and data[i][3] else 0)
            )

print(data)
rec_move(data, space, 0)
print(max_energy)