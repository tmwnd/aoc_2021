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

        # int(val, 2)
        return v, i + 5
    else:
        val = 0
        b = 15 if data[6] == "0" else 11

        i = 7 + b
        l = int(data[7:7+b], 2)
        if b == 15:
            while i < l+7+b:
                dv, di = pkg(data[i:])
                val += dv
                i += di
        elif b == 11:
            j = 0
            while j < l:
                dv, di = pkg(data[i:])
                val += dv
                i += di
                j += 1
        return v + val, i

print(pkg(data)[0])