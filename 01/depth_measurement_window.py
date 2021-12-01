WIDTH = 4

with open('data.txt') as data:
    i = 0
    line_a = data.readline()
    line_b = data.readline()
    line_c = data.readline()
    print(str(int(line_a) + int(line_b) + int(line_c)).rjust(WIDTH) + " (N/A - no previous measurement)")
    while line_c:
        next_line = data.readline()
        if next_line:
            b = int(next_line) + int(line_c) + int(line_b) > int(line_a) + int(line_b) + int(line_c)
            i += b
            print(str(int(next_line) + int(line_c) + int(line_b)).rjust(WIDTH) + " " + ("(increased)" if b else "(decreased)"))
        line_a = line_b
        line_b = line_c
        line_c = next_line
    print(f"There are {i} mesurements that are larger than the previous measurement")