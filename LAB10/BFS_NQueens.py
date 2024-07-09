def is_valid(board, row, col):

    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def bfs():
    queue = [[]]
    count = 0
    sample_solution = None

    while queue and count == 0:
        board = queue.pop(0)
        row = len(board)

        if row == 8:  
            count += 1
            sample_solution = board
        else:
            for col in range(8):
                if is_valid(board, row, col):
                    queue.append(board + [col])

    if sample_solution:
        print("Sample Solution:")
        for i in range(8):
            print("." * sample_solution[i] + "Q" + "." * (7 - sample_solution[i]))
    else:
        print("No solution found.")


if __name__ == "__main__":
    bfs()
