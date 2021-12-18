import snailfish_numbers as sn

with open("data.txt") as file:
    data = [sn.parse(line.strip()) for line in file.readlines()]

max_magnitude = 0

for i, s1 in enumerate(data):
    for s2 in data[i+1:]:
        max_magnitude = max(max_magnitude, sn.rec_magnitude(sn.check(sn.add(s1, s2))))
        max_magnitude = max(max_magnitude, sn.rec_magnitude(sn.check(sn.add(s2, s1))))

print(max_magnitude)