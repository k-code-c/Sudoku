def is_valid(board, row, col, num):
    # This will check that the number is not present in the row, column, and the grid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[row - row % 3 + i // 3] [col - col % 3 + i % 3] == num:
            return False
    return True
def find_empty_location(board):
    # Finds the first empty location which is denoted by "*"
    for i in range(9):
        for j in range(9):
            if board[i][j] == '*':
                return i, j
    return None, None

def solve_sudoku(board):
    # Find an empty location
    row, col = find_empty_location(board)

    # If there isn't any empty locations then the puzzle is solved
    if row is None:
        return True
    
    # Try placing a number in the empty location
    for num in map(str, range(1, 10)):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True
            
            # If placing the number does not lead to a solution then we must go back
            board[row][col] = '*'
            # Backtrack, if the number placement does not lead to a solution
    return False
def print_sudoku(board):
    for row in board:
        print("".join(row))

# Read input
input_board = [list(input().strip()) for _ in range(9)]

# Solve the Sudoku puzzle
if solve_sudoku(input_board):
    # Print the solutions
    print_sudoku(input_board)
else:
    # No solution exists
    print("-1") 

    
