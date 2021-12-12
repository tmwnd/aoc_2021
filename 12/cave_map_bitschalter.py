class Cave:
    def __init__(self, this):
        self.this = this
        self.post = []

    def add_post(self, post):
        self.post.append(post)
        post.post.append(self)

def rec_pathfinder(cave, vis, bitschalter):
    if cave.this.islower():
        if cave in vis:
            if bitschalter or cave.this == "start":
                return 0
            else:
                bitschalter = True
        else:
            vis.append(cave)

    return 1 if cave.this == "end" else sum([rec_pathfinder(c, vis.copy(), bitschalter) for c in cave.post])

caves = {"start": Cave("start")}
root = caves["start"]

with open("data.txt") as file:
    for start, end in [line.strip().split("-") for line in file.readlines()]:
        if start not in caves:
            caves[start] = Cave(start)
        if end not in caves:
            caves[end] = Cave(end)
        caves[start].add_post(caves[end])
 
print(rec_pathfinder(root, [], False))