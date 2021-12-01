WIDTH = 4

with open('data.txt') as data:
    i = 0
    line = data.readline()
    print(line.replace("\n", "").rjust(WIDTH) + " (N/A - no previous measurement)")
    while line:
        next_line = data.readline()
        if next_line:
            i += int(next_line) > int(line)
            print(next_line.replace("\n", "").rjust(WIDTH) + " " + ("(increased)" if int(next_line) > int(line) else "(decreased)"))
        line = next_line
    print(f"There are {i} mesurements that are larger than the previous measurement")