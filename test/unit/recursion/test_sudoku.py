import pytest
import mock
from algorithms import Sudoku


@mock.patch('algorithms.recursion.sudoku.Sudoku.solve_puzzle')
def test_run(mock_solve_puzzle):
    Sudoku.run()
    mock_solve_puzzle.assert_called_once()


def test_generate_numpy_grid():
    grid = Sudoku.generate_numpy_grid()
    for i, row in enumerate(grid):
        assert len(row) == 9
        assert len(grid[i]) == 9


def test_check_valid_number():
    check_false_row = Sudoku.check_valid_number(0, 1, 3)
    check_true_all = Sudoku.check_valid_number(8, 8, 8)
    check_false_block = Sudoku.check_valid_number(8, 8, 7)
    assert check_false_row is False
    assert check_true_all is True
    assert check_false_block is False


@pytest.mark.skip('Skipping until I can better test recursion and this function doesn\'t yet return anything')
@mock.patch('algorithms.recursion.sudoku.Sudoku.check_valid_number')
@mock.patch('algorithms.recursion.sudoku.Sudoku.solve_puzzle')
def test_solve_puzzle(mock_solve_puzzle, check_valid_number):
    Sudoku.solve_puzzle()
    check_valid_number.assert_called_once()
    mock_solve_puzzle.assert_called_once()
