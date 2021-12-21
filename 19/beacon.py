rx = [[1,0,0],[0,0,1],[0,-1,0]]
ry = [[0,0,1],[0,1,0],[-1,0,0]]
rz = [[0,1,0],[-1,0,0],[0,0,1]]

def mul(vector, matrix):
    ret = [0, 0, 0]
    for i, c in enumerate(vector):
        for j in range(3):
            ret[j] += c * matrix[i][j]
    return ret

def spin_vector(vector):
    global rx, ry, rz
    ret = []
    ret.append(vector)
    for m1 in rx, ry, rz:
        ret.append(mul(vector, m1))
        for m2 in rx, ry, rz:
            ret.append(mul(mul(vector, m1), m2))
            for m3 in rx, ry, rz:
                ret.append(mul(mul(mul(vector, m1), m2), m3))
    return ret

def spin(scanner):
    ret = []
    i = -1
    for vector in scanner:
        ret.append([])
        i += 1
        for v in spin_vector(vector):
            ret[i].append(v)
    return ret

def abs_scanner(scanner):
    global abs_beacons
    pos_vectors = spin(scanner)
    for abs_beacon in abs_beacons:
        for j in range(len(pos_vectors[0])):
            for i in range(len(pos_vectors)):
                pos_vector = pos_vectors[i][j]
                dx = abs_beacon[0] - pos_vector[0]
                dy = abs_beacon[1] - pos_vector[1]
                dz = abs_beacon[2] - pos_vector[2]
                for l in range(len(pos_vectors[0])):
                    counter = 0
                    for k in range(len(pos_vectors)):
                        v = pos_vectors[k][l]
                        if [v[0]+dx, v[1]+dy, v[2]+dz] in abs_beacons:
                            counter += 1
                        if counter >= 12:
                            for m in range(len(pos_vectors)):
                                b = pos_vectors[m][l]
                                b = [b[0]+dx, b[1]+dy, b[2]+dz]
                                if b not in abs_beacons:
                                    abs_beacons.append(b)
                            return True
    return False


if __name__ == "__main__":
    scanners = []
    i = -1
    with open("data.txt") as file:
        for line in file.readlines():
            if line.startswith("--- scanner "):
                scanners.append([])
                i += 1
            elif "," in line:
                scanners[i].append([int(vector) for vector in line.strip().split(",")])

    abs_beacons = scanners[0]

    queue = []
    for scanner in scanners[1:]:
        if not abs_scanner(scanner):
            queue.append(scanner)
    while len(queue) > 0:
        scanner = queue.pop()
        if not abs_scanner(scanner):
            queue.insert(0, scanner)

    print(len(abs_beacons))