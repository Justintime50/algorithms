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


class FizzBuzz():
    @classmethod
    def run(cls):
        """Iterate through numbers and
        print FizzBuzz to console.
        """
        print(f'Fizz Buzz to {ITERATIONS} iterations:')
        i = 1
        while i <= ITERATIONS:
            output = cls.determine_output(i)
            i += 1
            print(output)

    @classmethod
    def determine_output(cls, i):
        """Determine what the output of each iteration
        is based on its divisibility.
        """
        fizz = (i % 3 == 0)
        buzz = (i % 5 == 0)
        if fizz and buzz:
            output = 'FizzBuzz'
        elif fizz:
            output = 'Fizz'
        elif buzz:
            output = 'Buzz'
        else:
            output = i
        return output


def main():
    FizzBuzz.run()


if __name__ == '__main__':
    main()
