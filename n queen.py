#Assignment No. 5
# N-Queens Problem using Backtracking

def is_safe(board, row, col, n):
    # Check same row and same column
    for j in range(n):
        if board[row][j] == 1 and j != col:
            return False
    for i in range(n):
        if board[i][col] == 1 and i != row:
            return False

    # Check diagonals (all four directions)
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        r, c = row + dr, col + dc
        while 0 <= r < n and 0 <= c < n:
            if board[r][c] == 1:
                return False
            r += dr
            c += dc

    return True


def solve(board, col, n):
    # If we've processed all columns, success if exactly n queens placed
    if col >= n:
        # ensure we placed exactly n queens
        total = sum(sum(row) for row in board)
        return total == n

    # If this column already has a queen (pre-placed), just move to next column
    col_has_queen = any(board[r][col] == 1 for r in range(n))
    if col_has_queen:
        return solve(board, col + 1, n)

    # Try placing a queen in this column
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve(board, col + 1, n):
                return True
            # backtrack
            board[row][col] = 0

    # No valid placement in this column
    return False


def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))


# User input
n = int(input("Enter N: "))
r = int(input("Enter row for first queen (0 to N-1): "))
c = int(input("Enter column for first queen (0 to N-1): "))

board = [[0] * n for _ in range(n)]

# Place first queen (validate)
if not (0 <= r < n and 0 <= c < n):
    print("Invalid first queen position.")
else:
    board[r][c] = 1

    if solve(board, 0, n):  # start solving from column 0 across all columns
        print("\nFinal N-Queens Board:")
        print_board(board)
    else:
        print("\nSolution does not exist for this starting position.")
