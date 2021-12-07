with open("data.txt") as file:
    data = [int(crab) for crab in file.readline().split(",")]

min_fuel = 10E6
for i in range(max(data) + 1):
    fuel = sum([abs(crab - i) for crab in data])
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)