DIGITS = [2, 3, 4, 7]

with open("data.txt") as file:
    data = [line.strip().split(" | ") for line in file.readlines()]

numbers = 0

for output in [o[1].split(" ") for o in data]:
    for digit in output:
        if len(digit) in DIGITS:
            numbers += 1

print(numbers)