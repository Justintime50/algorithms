from unittest.mock import patch

from algorithms.sequences.fibonacci_sequence import generate_fibonacci_sequence


def test_fibonacci_sequence():
    fibonacci_sequence = generate_fibonacci_sequence()

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
def test_fibonacci_sequence_iteration_too_large(mock_sys_exit):
    generate_fibonacci_sequence()

    mock_sys_exit.assert_called_once()


@patch('algorithms.sequences.fibonacci_sequence.ITERATIONS', -1)
@patch('sys.exit')
def test_fibonacci_sequence_iteration_less_than_1(mock_sys_exit):
    generate_fibonacci_sequence()

    mock_sys_exit.assert_called_once()
