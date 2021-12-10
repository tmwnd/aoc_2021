brackets = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

points = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

with open("data.txt") as file:
    data = [line.strip() for line in file.readlines()]

val = []
for line in data:
    stack = []
    for bracket in line:
        if bracket not in brackets:
            stack.append(bracket)
        else:
            if stack.pop() != brackets[bracket]:
                stack = []
                break
    temp = 0
    for bracket in stack[::-1]:
        temp *= 5
        temp += points[bracket]
    if temp > 0:
        val.append(temp)

print(sorted(val)[int(len(val) / 2)])