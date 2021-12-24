inp_tape = [9 for _ in range(14)]
pos_tapes = []
pointer = 0
bitschalter = True

def get_pointer():
    global pointer
    pointer += 1
    return pointer - 1 

def sub(inp_tape, i = None):
    if i == None:
        i = len(inp_tape) - 1
    if i < 0 or i >= len(inp_tape):
        global bitschalter
        bitschalter = False
    elif inp_tape[i] == 1:
        inp_tape[i] = 9
        sub(inp_tape, i-1)
    else:
        global pointer
        pointer = 0
        inp_tape[i] -= 1

def print_tape(tape):
        for n in tape:
            print(n, end="")
        print()

with open("data.txt") as file:
    ins_ = [line.strip() for line in file.readlines()]

func = {
    "inp": lambda inp_tape: inp_tape[get_pointer()],
    "add": lambda a, b: a + b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: int(a / b) if b != 0 else -1,
    "mod": lambda a, b: a % b if a >= 0 and b > 0 else -1,
    "eql": lambda a, b: int(a == b)
}

while bitschalter:
    dict = {c: 0 for c in ['w','x','y','z']}

    for ins in ins_:
        if ins.startswith("inp"):
            f, a = ins.split(" ")
            dict[a] = func[f](inp_tape) 
        else:
            f, a, b = ins.split(" ")
            dict[a] = func[f](dict[a], dict[b] if b in dict else int(b))

    if dict['z'] == 0:
        pos_tapes.append(inp_tape)
        bitschalter = False

    sub(inp_tape)

print_tape(pos_tapes[0])
print_tape(pos_tapes[len(pos_tapes) - 1])