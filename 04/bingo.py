from copy import deepcopy

def gen_boards(data):
    boards = []
    board = [[0 for j in range(5)] for i in range(5)]
    for i, line in enumerate(data[2:len(data)]):
        if line == "":
            boards.append(board)
            board = deepcopy(board)
            continue
        for j, n in enumerate(line.replace("  "," ").split(" ")):
            board[i % 6][j] = int(n)
    boards.append(deepcopy(board))
    return(boards)

def draw(number, boards):
    for i, board in enumerate(boards):
        for j, line in enumerate(board):
            for k, cell in enumerate(line):
                if cell == number:
                    boards[i][j][k] = -1
        if (check(board)):
            print(res(board) * number)
            return []
    return boards

def check(board):
    for i in range(len(board)):
        h_check = 0
        v_check = 0
        for j in range(len(board)):
            h_check += board[i][j]
            v_check += board[j][i]
        if h_check <= -5 or v_check <= -5:
            return True
    return False

def res(board):
    ret = 0
    for line in board:
        for cell in line:
            if cell != -1:
                ret += cell
    return ret

with open("data.txt") as file:
    data = [line.strip() for line in file]
boards = gen_boards(data)

if __name__ == '__main__':
    for number in data[0].split(","):
        boards = draw(int(number), boards)
        if len(boards) == 0:
            break