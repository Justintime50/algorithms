import mock
from algorithms import FizzBuzz


@mock.patch('algorithms.sequences.fizzbuzz.FizzBuzz.determine_output')
def test_fizzbuzz_run(mock_determine_output):
    FizzBuzz.run()
    assert mock_determine_output.call_count == 15


def test_fizzbuzz_determine_output_fizz():
    output = FizzBuzz.determine_output(3)
    assert output == 'Fizz'


def test_fizzbuzz_determine_output_buzz():
    output = FizzBuzz.determine_output(5)
    assert output == 'Buzz'


def test_fizzbuzz_determine_output_fizzbuzz():
    output = FizzBuzz.determine_output(15)
    assert output == 'FizzBuzz'


def test_fizzbuzz_determine_output_normal():
    output = FizzBuzz.determine_output(1)
    assert output == 1
