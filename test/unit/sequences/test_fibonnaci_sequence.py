from unittest.mock import patch

from algorithms import FibonacciSequence


def test_fibonacci_sequence():
    fibonacci_sequence = FibonacciSequence.run()

    assert fibonacci_sequence == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]


@patch('algorithms.sequences.fibonnaci_sequence.ITERATIONS', 94)
@patch('sys.exit')
def test_fibonacci_sequence_iteration_too_large(mock_sys_exit):
    FibonacciSequence.run()

    mock_sys_exit.assert_called_once()


@patch('algorithms.sequences.fibonnaci_sequence.ITERATIONS', -1)
@patch('sys.exit')
def test_fibonacci_sequence_iteration_less_than_1(mock_sys_exit):
    FibonacciSequence.run()

    mock_sys_exit.assert_called_once()
