import mock
from algorithms import FibonacciSequence


def test_fibonacci_sequence():
    fibonacci_sequence = FibonacciSequence.run()
    assert fibonacci_sequence == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]


@mock.patch('algorithms.sequences.fibonnaci_sequence.MAX_ITERATIONS', 94)
@mock.patch('sys.exit')
def test_fibonacci_sequence_iteration_too_large(mock_sys_exit):
    FibonacciSequence.run()
    mock_sys_exit.assert_called_once()
