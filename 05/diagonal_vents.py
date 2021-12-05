import vents

data = vents.data

def get_d_points(s, e):
    for i in range(abs(e[0] - s[0]) + 1):
        vents.add_pos(e[0] + (i if (e[0] < s[0]) else -i), e[1] + (i if (e[1] < s[1]) else -i))

for line in data:
    i, o = [pos.split(",") for pos in line.strip().split(" -> ")]
    i = [int(p) for p in i]
    o = [int(p) for p in o]
    if i[0] != o[0] and i[1] != o[1]:
        if (abs(i[0] - o[0]) == abs(i[1] - o[1])):
            get_d_points(i, o)
        continue
    vents.get_points(i, o)

print(len(vents.doubles))