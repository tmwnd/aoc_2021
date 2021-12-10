brackets = {
    ")": ["(", 3],
    "]": ["[", 57],
    "}": ["{", 1197],
    ">": ["<", 25137]
}

with open("data.txt") as file:
    data = [line.strip() for line in file.readlines()]

val = 0
for line in data:
    stack = []
    for bracket in line:
        if bracket not in brackets:
            stack.append(bracket)
        else:
            if stack.pop() != brackets[bracket][0]:
                val += brackets[bracket][1]
print(val)