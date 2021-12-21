import copy

def play(players, player, i):
    if i >= 3:
        players[int(player)][1] += players[int(player)][0]
        if players[int(player)][1] >= 21:
            global winner
            winner[int(player)] += 1
            return
        play(copy.deepcopy(players), not player, 0)
    for _ in range(3):
        players[int(player)][0] += 1
        while players[int(player)][0] > 10:
                players[int(player)][0] -= 10
        play(copy.deepcopy(players), player, i+1)

with open("data.txt") as file:
    players = [[int(line.strip().split(" starting position: ")[1]), 0] for line in file.readlines()]

winner = [0 for _ in players]
play(players, False, 0)

print(winner)