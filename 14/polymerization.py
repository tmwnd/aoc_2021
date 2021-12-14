MAX_STEPS = 10

def rec_polymerization(pol, ins, d):
    if (d == MAX_STEPS):
        return pol
    ret = ""
    for i in range(len(pol) - 1):
        ret += pol[i] + ins[pol[i] + pol[i+1]]
    return rec_polymerization(ret + pol[len(pol) - 1], ins, d + 1)

with open("data.txt") as file:
    data = file.readlines()

pol = data[0].strip()
ins = {line.split(" -> ")[0].strip(): line.split(" -> ")[1].strip() for line in data[2:]}

pol = rec_polymerization(pol, ins, 0)
letters = {}

for l in pol:
    if l not in letters:
        letters[l] = 0
    letters[l] += 1

print(letters)
print(max(letters.values()) - min(letters.values()))