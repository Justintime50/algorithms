from typing import List

import numpy as np

# Fixes for mypy
count_numbers_added: int
count_numbers_backtracked: int

"""
SUDOKU

Definition: A Sudoku puzzle solver that uses recursion. Sudoku is a 9x9 grid that requires you to
enter numbers where each cell is filled but there are no repeats between the numbers in the same
column, row, or box

Usage: venv/bin/pyton algorithms/recursion/sudoku.py

Lessons Learned:
1) The only way this works is if you use back tracking and recursion, otherwise you'll get to
a dead end and cannot continue. Backtracking and recursion will help when we hit a dead end
2) Recursion and returning from recursion is tricky. You must properly return from a recursive
function or risk getting `NoneType` on the return, additionally, you want to make sure you return
at the right place so you don't have an eternal loop and your recursion can move on.
"""

GRID = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


def solve_sudoku_puzzle():
    """Run the Sudoku puzzle solver."""
    global count_numbers_added
    global count_numbers_backtracked
    count_numbers_added = count_numbers_backtracked = 0
    grid = GRID  # Reassign here so we can pass it around and edit the values

    # TODO: Allow for dynamic grid generation
    # grid = generate_numpy_grid()

    print('Original:')
    for row in grid:
        print(row)
    print('\n')

    grid_solved = _solve_puzzle(grid)

    if grid_solved:
        print('Solved:')
        for row in grid:
            print(row)
        print(f'Numbers put into the Sudoku puzzle: {count_numbers_added}')
        print(f'Numbers that had to be backtracked due to a dead-end: {count_numbers_backtracked}')

        # TODO: Count how many solutions the solver came up with
        # Only show this prompt if there are indeed more solutions
        # show_more = input('Show other solutions? (yes/no)')
        # if show_more.lower() != 'yes':
        #     sys.exit('Skipped showing other solutions.')
    else:
        raise Exception('No solution!')


def generate_numpy_grid() -> List[List[int]]:
    """Generate a numpy grid of dynamic numbers."""
    # TODO: Fix this generation, currently it works great to
    # generate a grid; however, it does not generate a correct
    # Sudoku grid that starts with only one number per row,
    # column, and block
    numpy_grid = []
    sudoku_number_choices = range(10)  # Possibilities are 0-9
    distribution = [0.64, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]

    for i in sudoku_number_choices:
        numpy_single_row = np.random.choice(sudoku_number_choices, 9, True, distribution).tolist()
        numpy_grid.append(numpy_single_row)

    for row in numpy_grid:
        print(row)

    return numpy_grid


def _check_valid_number(y: int, x: int, n: int, grid: List[List[int]]):
    """Checks if a number is valid inside the row, column, and block.

    NOTE: y comes before x here based on how the grid is drawn, y being first.
    """
    # Check the row and column for a number that intersects and is already used
    row_column_size = range(9)
    for i in row_column_size:
        if grid[y][i] == n or grid[i][x] == n:
            return False

    # Check the 3x3 block for a number that is already inside the 3x3 block
    block_size = 3
    x_block = (x // block_size) * block_size
    y_block = (y // block_size) * block_size
    for i in range(block_size):
        for j in range(block_size):
            if grid[y_block + i][x_block + j] == n:
                return False

    return True


def _solve_puzzle(grid: List[List[int]]) -> List[List[int]]:
    """Solves the puzzle recursively by checking if numbers are valid, updating the grid, and
    backtracking when necessary until a completed grid is built and returned.
    """
    global count_numbers_added
    global count_numbers_backtracked

    row_column_size = 9
    # Start on the first row and move to each position in that row prior to moving to the next row
    for y in range(row_column_size):
        for x in range(row_column_size):
            # Solve the current position if it has not yet been solved
            if grid[y][x] == 0:
                possible_answers = range(1, 10)
                for n in possible_answers:
                    if _check_valid_number(y, x, n, grid):
                        grid[y][x] = n
                        count_numbers_added += 1

                        if _solve_puzzle(grid):
                            return grid

                        # Here we backtrack if we hit a dead-end
                        grid[y][x] = 0
                        count_numbers_backtracked += 1

                # If we get to this point, the puzzle is not solved, return False so when we check, we keep going
                return False

    return grid


def main():
    solve_sudoku_puzzle()


if __name__ == '__main__':
    main()
