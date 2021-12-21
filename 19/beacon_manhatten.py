import beacon

def abs_scanner(scanner):
    global abs_beacons
    pos_vectors = beacon.spin(scanner)
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
                            global max_manhattan
                            max_manhattan = max(max_manhattan, dx+dy+dz)
                            for m in range(len(pos_vectors)):
                                b = pos_vectors[m][l]
                                b = [b[0]+dx, b[1]+dy, b[2]+dz]
                                if b not in abs_beacons:
                                    abs_beacons.append(b)
                            return True
    return False

max_manhattan = 0

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

print(max_manhattan)