from unittest.mock import patch

import pytest

from algorithms.recursion.sudoku import (
    GRID,
    _check_valid_number,
    _solve_puzzle,
    generate_numpy_grid,
    solve_sudoku_puzzle,
)


@patch('algorithms.recursion.sudoku._solve_puzzle')
def test_run(mock_solve_puzzle):
    solve_sudoku_puzzle()

    mock_solve_puzzle.assert_called_once()


@patch('algorithms.recursion.sudoku._solve_puzzle', return_value=False)
def test_run_no_solution(mock_solve_puzzle):
    with pytest.raises(Exception) as error:
        solve_sudoku_puzzle()

        assert error.message == 'No solution!'


def test_generate_numpy_grid():
    grid = generate_numpy_grid()

    for i, row in enumerate(grid):
        assert len(row) == 9
        assert len(grid[i]) == 9


def test_check_valid_number():
    check_false_row = _check_valid_number(0, 1, 3, GRID)
    check_true_all = _check_valid_number(8, 8, 8, GRID)
    check_false_block = _check_valid_number(8, 8, 7, GRID)

    assert check_false_row is False
    assert check_true_all is True
    assert check_false_block is False


def test_solve_puzzle():
    """If the puzzle is solved, there will be no more 0s and it will have
    a valid filled grid of numbers.
    """
    solved_grid = _solve_puzzle(GRID)

    for row in solved_grid:
        assert 0 not in row

    assert solved_grid == [
        [3, 1, 6, 5, 7, 8, 4, 9, 2],
        [5, 2, 9, 1, 3, 4, 7, 6, 8],
        [4, 8, 7, 6, 2, 9, 5, 3, 1],
        [2, 6, 3, 4, 1, 5, 9, 8, 7],
        [9, 7, 4, 8, 6, 3, 1, 2, 5],
        [8, 5, 1, 7, 9, 2, 6, 4, 3],
        [1, 3, 8, 9, 4, 7, 2, 5, 6],
        [6, 9, 2, 3, 5, 1, 8, 7, 4],
        [7, 4, 5, 2, 8, 6, 3, 1, 9],
    ]
