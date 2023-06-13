from unittest.mock import patch

import pytest

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
    fibonacci_sequence = list(_iterate_fibonacci_sequence())

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


@patch('algorithms.sequences.fibonacci_sequence.ITERATIONS', 5)
def test_validate_iterations_valid_number():
    try:
        _validate_iterations()
    except Exception as error:
        assert False, f'An exception was raised and should not have been. {error}'


@patch('algorithms.sequences.fibonacci_sequence.ITERATIONS', 94)
def test_validate_iterations_iteration_too_large():
    with pytest.raises(ValueError) as error:
        _validate_iterations()

    assert (
        str(error.value)
        == 'You have requested too many iterations - computers can literally only print up to 93 iterations before the'
        ' Fibonacci number exceeds the max value allowed in memory. Please select a lower number and try again.'
    )


@patch('algorithms.sequences.fibonacci_sequence.ITERATIONS', -1)
def test_validate_iterations_iteration_less_than_1():
    with pytest.raises(ValueError) as error:
        _validate_iterations()

    assert str(error.value) == 'ITERATIONS must be greater than or equal to 1.'
