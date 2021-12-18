import copy

def parse(s):
    if "[" not in s:
        return int(s.replace("]",""))
    b = 0
    for i, c in enumerate(s):
        if c == "[":
            b += 1
        elif c == "]":
            b -= 1
        elif b == 1 and c == ",":
            return([parse(s[1:i]), parse(s[i+1:len(s)-1])])

def explode(n):
    global bitschalter
    bitschalter = False
    return rec_explode(n)

def rec_explode(n):
    global bitschalter
    ret = []
    for e in n[::-1]:
        if isinstance(e, list):
            ret.append(rec_explode(e))
        else:
            if bitschalter:
                global pre
                ret.append(e + pre)
                bitschalter = False
                pre = 0
            elif e == -1:
                bitschalter = True
                ret.append(0)
            else:
                ret.append(e)
    return ret[::-1]

def split(n):
    global bitschalter
    bitschalter = True
    return rec_split(n)

def rec_split(n):
    ret = []
    for e in n:
        if isinstance(e, list):
            ret.append(rec_split(e))
        else:
            global bitschalter
            ret.append(e if e < 10 or not bitschalter else [int(e/2), int((e+1)/2)])
            if e >= 10:
                bitschalter = False
    return ret

def check(n):
    global bitschalter, pre, post
    temp = []
    while temp != n:
        temp = copy.deepcopy(n)
        pre, post = 0, 0
        bitschalter = True
        n = rec_check(n, 1)
        n = explode(n)
        if temp != n:
            continue
        n = split(n)
        if temp != n:
            continue  
        break
    return n

def rec_check(n, d):
    ret = []
    for e in n:
        global post
        if isinstance(e, list):
            global bitschalter
            if d == 4 and bitschalter:
                global pre
                bitschalter = False
                pre, post = e
                ret.append(-1)
            else:
                ret.append(rec_check(e, d+1))
        else:
            ret.append(e + post)
            post = 0
    return ret

def add(a, b):
    return [a, b]

def rec_magnitude(n):
    val = 0
    k = 3
    for e in n:
        val += (e if isinstance(e, int) else rec_magnitude(e)) * k
        k = 2
    return val

bitschalter = False
pre = 0
post = 0

if __name__ == "__main__":
    with open("data.txt") as file:
        n = None
        for line in file.readlines():
            n = check(add(n, check(parse(line.strip()))) if n else parse(line))

    # print(n)
    print(rec_magnitude(n))
