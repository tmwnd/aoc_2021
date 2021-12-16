with open("data.txt") as file:
    data = ""
    for binary in [bin(int(h, 16))[2:] for h in file.readline()]:
        data += "0"*(4-len(binary)) + binary

def pkg(data):
    v = int(data[0:3], 2)
    t = int(data[3:6], 2)

    if t == 4:
        val = ""
        i = 6
        while i < len(data):
            val += data[i+1:i+5]
            if (data[i] == "0"):
                break
            i += 5

        return int(val, 2), i + 5
    else:
        val = None if t in [2,5,6,7] else (0 if t == 0 else 1)
        b = 15 if data[6] == "0" else 11

        if t == 0:
            op = lambda val, dv: val + dv
        elif t == 1:
            op = lambda val, dv: val * dv
        elif t == 2:
            op = lambda val, dv: min(val, dv) if val is not None else dv
        elif t == 3:
            op = lambda val, dv: max(val, dv)
        elif t == 5:
            op = lambda val, dv: int(val > dv) if val is not None else dv
        elif t == 6:
            op = lambda val, dv: int(val < dv) if val is not None else dv
        elif t == 7:
            op = lambda val, dv: int(val == dv) if val is not None else dv

        i = 7 + b
        l = int(data[7:7+b], 2)
        
        j = 0
        while (b == 15 and i < l+7+b) or (b == 11 and j < l):
            dv, di = pkg(data[i:])
            i += di
            j += 1

            val = op(val, dv)
                               
        return val, i

print(pkg(data)[0])