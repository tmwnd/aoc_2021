MAX_DAYS = 256

# -1, 0, 1, 2, 3, 4, 5, 6, 7, 8
ttl = [0 for i in range(10)]

def rek_produce(day, ttl):
    for i in range(len(ttl) - 1):
        ttl[i] = ttl[i + 1]
    ttl[9] = 0
    ttl[7] += ttl[0]
    ttl[9] += ttl[0]
    ttl[0] = 0
    if day < MAX_DAYS:
        return rek_produce(day + 1, ttl)
    return ttl

with open("data.txt") as file:
    data = [int(lfish) for lfish in file.readline().split(",")]
for lfish in data:
    ttl[lfish + 1] += 1

rek_produce(1, ttl)

print(sum(ttl))