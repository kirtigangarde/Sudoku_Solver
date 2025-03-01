def print_sudoku(grid):
                      """Prints the Sudoku grid in a readable format."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()

def is_valid(grid, row, col, num):
    """Checks if placing `num` at position (row, col) is valid."""
    # Check the row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    """Solves the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num  # Place the number

                        if solve_sudoku(grid):  # Recursively solve
                            return True

                        grid[row][col] = 0  # Backtrack if the solution is invalid

                return False  # Trigger backtracking
    return True  # Puzzle solved

def main():
    # Example unsolved Sudoku grid (0 represents empty cells)
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Unsolved Sudoku:")
    print_sudoku(grid)

    if solve_sudoku(grid):
        print("\nSolved Sudoku:")
        print_sudoku(grid)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()