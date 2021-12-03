def read():
    with open("data.txt") as file:
        data = [line.strip() for line in file]
    return data

def avg(data, i):
    avg = 0
    for line in data:
        avg += int(line[i])
    return avg / len(data) >= 0.5

def rm(data, i, avg):
    return list(filter(lambda x: int(x[i]) == avg, data))

data_oxygen = read()
data_co2 = data_oxygen.copy()
i = 0
while len(data_oxygen) > 1:
    data_oxygen = rm(data_oxygen, i, int(avg(data_oxygen , i)))
    i += 1
i = 0
while len(data_co2) > 1:
    data_co2 = rm(data_co2, i, int(not avg(data_co2 , i)))
    i += 1

print(int(data_oxygen[0], 2) * int(data_co2[0], 2))