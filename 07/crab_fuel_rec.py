# import sys
# sys.setrecursionlimit(10000)

with open("data.txt") as file:
    data = [int(crab) for crab in file.readline().split(",")]

def rec_calc_fuel(dis):
    return dis if dis <= 1 else dis + rec_calc_fuel(dis - 1)

def calc_fuel(dis):
    return dis * (dis + 1) / 2

min_fuel = 10E10
for i in range(max(data) + 1):
    fuel = sum([calc_fuel(abs(crab - i)) for crab in data])
    if fuel < min_fuel:
        min_fuel = fuel

print(int(min_fuel))