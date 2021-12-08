UNIQUE_DIGITS = [2, 3, 4, 7]

def numbers_complete(numbers):
    for number in numbers.values():
        if not number:
            return False
    return True

def digit_sort(digit):
    ret = ""
    for i in "a,b,c,d,e,f,g".split(","):
        if i in digit:
            ret += str(i)
    return ret

def digit_contains(digit, contains):
    for c in contains:
        if not c in digit:
            return False
    return True

def digit_eq(digit1, digit2):
    return len(digit1) == len(digit2) and digit_contains(digit1, digit2)

def digit_sub(pre, sub):
    for c in sub:
        pre = pre.replace(c, "")
    return pre

def calc_numbers(line):
    numbers = {i: None for i in range(10)}
    while not numbers_complete(numbers):
        for io in line:
            for digit in io.split(" "):
                l = len(digit)
                if l in UNIQUE_DIGITS:
                    numbers[1 if l == 2 else (4 if l == 4 else (7 if l == 3 else 8))] = digit
                else:
                    if l == 6:
                        if numbers[4]:
                            if  len(digit_sub(digit, numbers[4])) == 2:
                                numbers[9] = digit
                            elif numbers[1]:
                                if len(digit_sub(numbers[1], digit)) == 0:
                                    numbers[0] = digit
                                else:
                                    numbers[6] = digit
                    else:
                        if numbers[1]:
                            if len(digit_sub(numbers[1], digit)) == 0:
                                numbers[3] = digit
                            elif numbers[4]:
                                if len(digit_sub(digit, numbers[4])) == 2:
                                    numbers[5] = digit
                                else:
                                    numbers[2] = digit
    # for number, digit in numbers.items():
    #     print(str(number) + ": " + digit_sort(digit))
    return numbers

def get_val(digit, numbers):
    l = len(digit)
    return 1 if l == 2 else (4 if l == 4 else (7 if l == 3 else (8 if l == 7 else get_val_ununique(digit, numbers))))

def get_val_ununique(digit, numbers):
    for number, digits in numbers.items():
        if digit_eq(digit, digits):
            return number
    return 0

with open("data.txt") as file:
    data = [line.strip().split(" | ") for line in file.readlines()]

val = 0

for line in data:
    numbers = calc_numbers(line)
    k = 1
    x = val
    for digit in line[1].split(" ")[::-1]:
        val += get_val(digit, numbers) * k
        k *= 10

print(val)