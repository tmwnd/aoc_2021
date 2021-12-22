cubes = []

def size_cube():
    global cubes
    val = 0
    for cube in cubes:
        v = 1
        for i in 0,1,2:
            v *= cube[i][1] - cube[i][0] + 1
        val += v
    return val

def split_cube(out, inp):
    add_cube([[out[0][0], inp[0][0]-1],[out[1][0], out[1][1]],[out[2][0], out[2][1]]])
    add_cube([[inp[0][1]+1, out[0][1]],[out[1][0], out[1][1]],[out[2][0], out[2][1]]])
    add_cube([[max(out[0][0], inp[0][0]), min(out[0][1], inp[0][1])],[out[1][0], inp[1][0]-1],[out[2][0], out[2][1]]])
    add_cube([[max(out[0][0], inp[0][0]), min(out[0][1], inp[0][1])],[inp[1][1]+1, out[1][1]],[out[2][0], out[2][1]]])
    add_cube([[max(out[0][0], inp[0][0]), min(out[0][1], inp[0][1])],[max(out[1][0], inp[1][0]), min(out[1][1], inp[1][1])],[out[2][0], inp[2][0]-1]])
    add_cube([[max(out[0][0], inp[0][0]), min(out[0][1], inp[0][1])],[max(out[1][0], inp[1][0]), min(out[1][1], inp[1][1])],[inp[2][1]+1, out[2][1]]])

def contains_cube(out, inp):
    c = 0
    for i in 0,1,2:
        if out[i][0] <= inp[i][0] and out[i][1] >= inp[i][1]:
            c += 1
        elif out[i][0] >= inp[i][0] and out[i][1] <= inp[i][1]:
            c += 1
        else:
            for j in 0,1:
                if out[i][0] <= inp[i][j] and inp[i][j] <= out[i][1]:
                    c += 1
                    continue
    if c == 3:
        return True
    return False

def add_cube(cube):
    global cubes
    for i in 0,1,2:
        if cube[i][0] > cube[i][1]:
            return
    cubes.append(cube)

def sub_cube(cube):
    global cubes
    for c in cubes.copy():
        if contains_cube(c, cube):
            cubes.remove(c)
            split_cube(c, cube)

if __name__ == "__main__":
    with open("data.txt") as file:
        for line in file.readlines():
            cube = [[int(x) for x in c[2:].split("..")] for c in line.strip().replace("on ","").replace("off ","").split(",")]
            sub_cube(cube)
            if line.startswith("on"):
                add_cube(cube)                           

    print(size_cube())