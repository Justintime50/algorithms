import os


"""
FIZZBUZZ

Description: FizzBuzz is a typical coding interview question. Numbers 1 - x are printed;
if they are divisible by 3, the number is replaced with `Fizz`, if the number is divisible by 5,
the number is replaced with `Buzz`, if the number is divisible by 15,
the number is replaced with `FizzBuzz`.

Usage: ITERATIONS=50 venv/bin/python FizzBuzz.py

Lessons Learned:
1) Order matters, ensure that FizzBuzz is first or it could have criteria met for just
Fizz or Buzz
"""


ITERATIONS = int(os.getenv('ITERATIONS', 15))


def generate_fizzbuzz():
    """Iterate through numbers and print FizzBuzz to console."""
    _validate_iterations()
    print(f'Fizz Buzz to {ITERATIONS} iterations:')

    for iteration in range(1, ITERATIONS + 1):
        output = _determine_output(iteration)
        print(output)


def _validate_iterations():
    """Validate the iterations before proceeding."""
    if ITERATIONS < 1:
        raise ValueError('ITERATIONS must be greater than or equal to 1.')


def _determine_output(iteration) -> str:
    """Determine what the output of each iteration is based on its divisibility."""
    fizz = iteration % 3 == 0
    buzz = iteration % 5 == 0

    if fizz and buzz:
        output = 'FizzBuzz'
    elif fizz:
        output = 'Fizz'
    elif buzz:
        output = 'Buzz'
    else:
        output = str(iteration)

    return output


def main():
    generate_fizzbuzz()


if __name__ == '__main__':
    main()
