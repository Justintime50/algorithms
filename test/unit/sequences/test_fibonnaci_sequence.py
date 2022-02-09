from unittest.mock import patch

from algorithms.sequences.fibonacci_sequence import (
    _iterate_fibonacci_sequence,
    _validate_iterations,
    generate_fibonacci_sequence,
)


@patch('algorithms.sequences.fibonacci_sequence._validate_iterations')
@patch('algorithms.sequences.fibonacci_sequence._iterate_fibonacci_sequence')
def test_generate_fibonacci_sequence(mock_iterate_sequence, mock_validate_iterations):
    generate_fibonacci_sequence()

    mock_iterate_sequence.assert_called_once()
    mock_validate_iterations.assert_called_once()


def test_iterate_fibonacci_sequence():
    fibonacci_sequence = _iterate_fibonacci_sequence()

    assert fibonacci_sequence == [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
    ]


@patch('algorithms.sequences.fibonacci_sequence.ITERATIONS', 94)
@patch('sys.exit')
def test_validate_iterations_iteration_too_large(mock_sys_exit):
    _validate_iterations()

    mock_sys_exit.assert_called_once()


@patch('algorithms.sequences.fibonacci_sequence.ITERATIONS', -1)
@patch('sys.exit')
def test_validate_iterations_iteration_less_than_1(mock_sys_exit):
    _validate_iterations()

    mock_sys_exit.assert_called_once()
