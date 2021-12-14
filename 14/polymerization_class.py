MAX_STEPS = 40

def rec_polymerization(pol, ins, d):
    if (d == MAX_STEPS):
        return pol
    ret = {p: 0 for p in pol}
    for p, anz in pol.items():
        i = ins[p]
        ret[p[0] + i] += anz
        ret[i + p[1]] += anz
    return rec_polymerization(ret, ins, d + 1)

with open("data.txt") as file:
    data = file.readlines()

ins = {line.split(" -> ")[0].strip(): line.split(" -> ")[1].strip() for line in data[2:]}
pol = {line.split(" -> ")[0].strip(): 0 for line in data[2:]}

data = data[0].strip()
for i in range(len(data) - 1):
    pol[data[i] + data[i+1]] += 1

pol = rec_polymerization(pol, ins, 0)
letters = {}

for p, anz in pol.items():
    if p[0] not in letters:
        letters[p[0]] = 0
    letters[p[0]] += anz
letters[data[len(data) - 1]] += 1
print(letters)
print(max(letters.values()) - min(letters.values()))