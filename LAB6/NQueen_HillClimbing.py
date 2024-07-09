import random

def generate_random_board(n):
    return [random.randint(0, n-1) for _ in range(n)]

def count_conflicts(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def steepest_hill_climbing(n, max_iterations=1000):
    current_board = generate_random_board(n)
    current_conflicts = count_conflicts(current_board)
    
    for _ in range(max_iterations):
        if current_conflicts == 0:
            return current_board
        
        best_move = None
        best_conflicts = current_conflicts
        
        for i in range(n):
            for j in range(n):
                if current_board[i] != j:
                    temp_board = current_board[:]
                    temp_board[i] = j
                    temp_conflicts = count_conflicts(temp_board)
                    if temp_conflicts < best_conflicts:
                        best_move = (i, j)
                        best_conflicts = temp_conflicts
        
        if best_move is None:
            break
        
        i, j = best_move
        current_board[i] = j
        current_conflicts = best_conflicts
    
    return None  # No solution found within the maximum iterations

def print_board(board):
    n = len(board)
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(' '.join(row))

# Example usage
n = 5  # Change this to the desired size of the chessboard
solution = steepest_hill_climbing(n)
if solution:
    print("Solution found:")
    print_board(solution)
else:
    print("No solution found within the maximum iterations.")
