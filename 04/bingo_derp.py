import bingo

data = bingo.data
boards = bingo.boards

def draw(number, boards):
    for i, board in enumerate(boards):
        for j, line in enumerate(board):
            for k, cell in enumerate(line):
                if cell == number:
                    boards[i][j][k] = -1
        if (bingo.check(board)):
            if (len(boards) == 1):
                print(bingo.res(board) * number)
                return []
            boards.remove(board)
            return draw(number, boards)
    return boards

for number in data[0].split(","):
    boards = draw(int(number), boards)
    if len(boards) == 0:
        break