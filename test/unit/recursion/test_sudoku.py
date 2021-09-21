from unittest.mock import patch

from algorithms import Sudoku

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


@patch('algorithms.recursion.sudoku.Sudoku.solve_puzzle')
def test_run(mock_solve_puzzle):
    Sudoku.run()

    mock_solve_puzzle.assert_called_once()


@patch('sys.exit')
@patch('algorithms.recursion.sudoku.Sudoku.solve_puzzle', return_value=False)
def test_run_no_solution(mock_solve_puzzle, mock_sys_exit):
    Sudoku.run()

    mock_sys_exit.assert_called_once_with('No solution!')


def test_generate_numpy_grid():
    grid = Sudoku.generate_numpy_grid()

    for i, row in enumerate(grid):
        assert len(row) == 9
        assert len(grid[i]) == 9


def test_check_valid_number():
    check_false_row = Sudoku.check_valid_number(0, 1, 3, GRID)
    check_true_all = Sudoku.check_valid_number(8, 8, 8, GRID)
    check_false_block = Sudoku.check_valid_number(8, 8, 7, GRID)

    assert check_false_row is False
    assert check_true_all is True
    assert check_false_block is False


@patch('algorithms.recursion.sudoku.Sudoku.check_valid_number')
def test_solve_puzzle(check_valid_number):
    solved_grid = Sudoku.solve_puzzle(GRID)
    check_valid_number.assert_called()

    assert solved_grid == [
        [3, 1, 6, 5, 1, 8, 4, 1, 1],
        [5, 2, 1, 1, 1, 1, 1, 1, 1],
        [1, 8, 7, 1, 1, 1, 1, 3, 1],
        [1, 1, 3, 1, 1, 1, 1, 8, 1],
        [9, 1, 1, 8, 6, 3, 1, 1, 5],
        [1, 5, 1, 1, 9, 1, 6, 1, 1],
        [1, 3, 1, 1, 1, 1, 2, 5, 1],
        [1, 1, 1, 1, 1, 1, 1, 7, 4],
        [1, 1, 5, 2, 1, 6, 3, 1, 1],
    ]


# TODO: Test branches of solve_puzzle, this will require dynamically loading a grid most likely
