sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open("data.txt") as data:
    for line in data:
        for i in range(len(sum)):
            sum[i] += int(line[i])
    gamma = 0
    k = 1
    for s in reversed(sum):
        gamma += (s / len(open("data.txt").readlines( )) >= 0.5) * k
        k *= 2
    epsilon = 4095 - gamma
    power = epsilon * gamma
    print(power)