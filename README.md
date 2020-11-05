# Algorithms

Here lies classic algorithms and the lessons learned while building them.

[![Build Status](https://travis-ci.com/Justintime50/algorithms.svg?branch=main)](https://travis.com/Justintime50/algorithms)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/algorithms/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/algorithms?branch=main)
[![Licence](https://img.shields.io/github/license/justintime50/algorithms)](LICENSE)

## Available Algorithms

### Sequences

[**Fibonnaci Sequence**](algorithms/sequences/fibonnaci_sequence.py)

```
The Fibonacci Sequence to 20 iterations:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
```

[**Fizz Buzz**](algorithms/sequences/fizzbuzz.py)

```
Fizz Buzz to 15 iterations:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

### Sorting

[**Bubble Sort**](algorithms/sorting/bubble_sort.py)

```
Original: [3, 1, 5, 9, 7, 6, 2, 8, 4]
[1, 3, 5, 9, 7, 6, 2, 8, 4] => Swapped 3 and 1
[1, 3, 5, 7, 9, 6, 2, 8, 4] => Swapped 9 and 7
[1, 3, 5, 7, 6, 9, 2, 8, 4] => Swapped 9 and 6
[1, 3, 5, 7, 6, 2, 9, 8, 4] => Swapped 9 and 2
[1, 3, 5, 7, 6, 2, 8, 9, 4] => Swapped 9 and 8
[1, 3, 5, 7, 6, 2, 8, 4, 9] => Swapped 9 and 4
[1, 3, 5, 6, 7, 2, 8, 4, 9] => Swapped 7 and 6
[1, 3, 5, 6, 2, 7, 8, 4, 9] => Swapped 7 and 2
[1, 3, 5, 6, 2, 7, 4, 8, 9] => Swapped 8 and 4
[1, 3, 5, 2, 6, 7, 4, 8, 9] => Swapped 6 and 2
[1, 3, 5, 2, 6, 4, 7, 8, 9] => Swapped 7 and 4
[1, 3, 2, 5, 6, 4, 7, 8, 9] => Swapped 5 and 2
[1, 3, 2, 5, 4, 6, 7, 8, 9] => Swapped 6 and 4
[1, 2, 3, 5, 4, 6, 7, 8, 9] => Swapped 3 and 2
[1, 2, 3, 4, 5, 6, 7, 8, 9] => Swapped 5 and 4
List sorted successfully in 0:00:00.000080 with Bubble Sort Algorithm!
```

## Install

```bash
make install
```

## Usage

See each script for additional descriptions, usage, features, and lessons learned.

```bash
venv/bin/python src/sorting/bubble_sort.py
venv/bin/python src/sequences/fibonacci_sequence.py
```

## Development

```bash
# Lint the project
make lint

# Run tests
make test

# Run test coverage
make coverage
```
