from algorithms import FibonacciSequence


def test_fibonacci_sequence():
    fibonacci_sequence = FibonacciSequence.run()
    assert fibonacci_sequence == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
