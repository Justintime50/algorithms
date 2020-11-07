import sys
import numpy as np


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
function or risk getting `NoneType` on the return
"""


# Unfilled items must be a 0


class Sudoku():
    @classmethod
    def run(cls):
        """Run the Sudoku puzzle solver
        """
        global count_numbers_added
        global count_numbers_backtracked
        global grid
        count_numbers_added = 0
        count_numbers_backtracked = 0
        grid = [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]
        ]
        # TODO: Allow for dynamic grid generation
        # grid = cls.generate_numpy_grid
        print('Original:')
        for row in grid:
            print(row)
        print('\n')
        cls.solve_puzzle()
        # TODO: Print the solved puzzle here instead of in the
        # solve_puzzle function

    @classmethod
    def generate_numpy_grid(cls):
        """Generate a numpy grid of dynamic numbers
        """
        # TODO: Fix this generation, currently it works great to
        # generate a grid; however, it does not generate a correct
        # Sudoku grid that starts with only one number per row,
        # column, and block
        numpy_array = []
        sudoku_number_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        distribution = [0.64, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04]
        for i in range(9):
            numpy_array_row = np.random.choice(sudoku_number_choices, 9, True, distribution).tolist()
            numpy_array.append(numpy_array_row)
        grid = numpy_array
        for row in grid:
            print(row)
        return grid

    @classmethod
    def check_valid_number(cls, y, x, n):
        """Checks if a number is valid inside the
        row, column, and block

        y comes before x here based on how the grid
        is drawn, y being first
        """
        # Check the row and column for a number
        # that intersects and is already used
        global grid
        for i in range(9):
            if grid[y][i] == n or grid[i][x] == n:
                return False

        # Check the 3x3 block for a number that
        # is already inside the 3x3 block
        x_block = (x//3)*3
        y_block = (y//3)*3
        for i in range(3):
            for j in range(3):
                if grid[y_block + i][x_block + j] == n:
                    return False

        return True

    @classmethod
    def solve_puzzle(cls):
        """Solves the puzzle recursively by checking
        if numbers are valid, updating the grid, and
        backtracking when necessary until a completed
        grid is built and returned
        """
        global count_numbers_added
        global count_numbers_backtracked
        global grid
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    for n in range(1, 10):
                        if cls.check_valid_number(y, x, n):
                            grid[y][x] = n
                            count_numbers_added += 1
                            cls.solve_puzzle()
                            # Here we backtrack if we hit a dead-end
                            grid[y][x] = 0
                            count_numbers_backtracked += 1
                    return

        print('Solved:')
        for row in grid:
            print(row)
        print(f'Numbers put into the Sudoku puzzle: {count_numbers_added}')
        print(f'Numbers that had to be backtracked due to a dead-end: {count_numbers_backtracked}')
        # TODO: Count how many solutions the solver came up with
        # Only show this prompt if there are indeed more solutions
        show_more = input('Show other solutions? (yes/no)')
        if show_more.lower() != 'yes':
            sys.exit('Skipped showing other solutions.')
        # TODO: Return the solved puzzle here


def main():
    Sudoku.run()


if __name__ == '__main__':
    main()
