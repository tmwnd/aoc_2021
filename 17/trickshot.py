with open("data.txt") as file:
    ziel_x, ziel_y = [[int(c) for c in xy[2:].split("..")] for xy in file.readline()[13:].split(", ")]

max_height = 0

dy_ = 0
while True:
    for dx in range(max(ziel_x)):
        dy = dy_
        height = 0
        x = 0
        y = 0
        d = [dx, dy]
        while y > min(ziel_y):
            x += dx
            dx += 1 if dx < 0 else (-1 if dx > 0 else 0)
            y += dy
            dy -= 1
            if y > height:
                height = y
            if min(ziel_y) <= y and max(ziel_y) >= y and min(ziel_x) <= x and max(ziel_x) >= x:
                if height > max_height:
                    max_height = height
                    max_d = d
                # print(f"hit: {x=} | {y=}, {height=}, {d=}")
                break
    dy_ += 1
    if (-1 * dy_ < min(ziel_y)):
        break
print(f"{max_height=}, {max_d=}")