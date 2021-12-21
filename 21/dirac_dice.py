dice = 0
counter = 0

def roll():
    global dice, counter
    dice += 1
    if dice >= 100:
        dice = 0
    counter += 1
    return dice

def play():
    global players
    while True:
        for player in players:
            for _ in range(3):
                player[0] += roll()
                while player[0] > 10:
                    player[0] = player[0] - 10
            player[1] += player[0]
            if player[1] >= 1000:
                return

with open("data.txt") as file:
    players = [[int(line.strip().split(" starting position: ")[1]), 0] for line in file.readlines()]

play()

print(min([player[1] for player in players]) * counter)