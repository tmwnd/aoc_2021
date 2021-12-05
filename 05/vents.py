with open("data.txt") as file:
    data = file.readlines()
pos = []
doubles = []

def pos_eq(x1, x2):
    if x1[0] == x2[0] and x1[1] == x2[1]:
        return True
    return False


def add_pos(x, y):
    x1 = [x, y]
    for p in pos:
        if pos_eq(p, x1):
            for d in doubles:
                if pos_eq(d, x1):
                    return
            doubles.append(x1)
            return
    pos.append(x1)

def get_points(s, e):
    for i in range(abs(e[0] - s[0]) + 1):
        for j in range(abs(e[1] - s[1]) + 1):
            add_pos(i + (s[0] if s[0] < e[0] else e[0]), j + (s[1] if s[1] < e[1] else e[1]))
    

if __name__ == "__main__":
    for line in data:
        i, o = [pos.split(",") for pos in line.strip().split(" -> ")]
        i = [int(p) for p in i]
        o = [int(p) for p in o]
        if i[0] != o[0] and i[1] != o[1]:
            continue
        get_points(i, o)

    print(len(doubles))