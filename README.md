<div align="center">

# Algorithms

Classic algorithms including Fizz Buzz, Bubble Sort, the Fibonacci Sequence, a Sudoku solver, and more.

[![Build](https://github.com/Justintime50/algorithms/workflows/build/badge.svg)](https://github.com/Justintime50/algorithms/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/algorithms/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/algorithms?branch=main)
[![Licence](https://img.shields.io/github/license/justintime50/algorithms)](LICENSE)

<img src="assets/showcase.png" alt="Showcase">

</div>

## Algorithm Complexity

> Time and Space Complexity (Big O Notation)

All algorithms have a complexity known as `Big O Notation`, the more complex an algorithm, the less efficient it gets as more data is introduced. Listed below are the `Big-O` complexities listed from best to worst:

* O(1)
* O(log n)
* O(n)
* O(n * log n)
* O(n^2)
* O(2^n)
* O(n!)

<img src="assets/big_o_notation.png" alt="Big O Notation">

## Available Algorithms

### Recursion

[**Invert Binary Tree - O(n)**](algorithms/recursion/invert_binary_tree.py)

<img src="assets/invert_binary_tree.png" alt="Invert Binary Tree">

[**Sudoku Solver - O(n)**](algorithms/recursion/sudoku.py)

```
Original:
[3, 0, 6, 5, 0, 8, 4, 0, 0]
[5, 2, 0, 0, 0, 0, 0, 0, 0]
[0, 8, 7, 0, 0, 0, 0, 3, 1]
[0, 0, 3, 0, 1, 0, 0, 8, 0]
[9, 0, 0, 8, 6, 3, 0, 0, 5]
[0, 5, 0, 0, 9, 0, 6, 0, 0]
[1, 3, 0, 0, 0, 0, 2, 5, 0]
[0, 0, 0, 0, 0, 0, 0, 7, 4]
[0, 0, 5, 2, 0, 6, 3, 0, 0]


Solved:
[3, 1, 6, 5, 7, 8, 4, 9, 2]
[5, 2, 9, 1, 3, 4, 7, 6, 8]
[4, 8, 7, 6, 2, 9, 5, 3, 1]
[2, 6, 3, 4, 1, 5, 9, 8, 7]
[9, 7, 4, 8, 6, 3, 1, 2, 5]
[8, 5, 1, 7, 9, 2, 6, 4, 3]
[1, 3, 8, 9, 4, 7, 2, 5, 6]
[6, 9, 2, 3, 5, 1, 8, 7, 4]
[7, 4, 5, 2, 8, 6, 3, 1, 9]
Numbers put into the Sudoku puzzle: 769
Numbers that had to be backtracked due to a dead-end: 720
```

### Sequences

[**Fibonnaci Sequence - O(2^n)**](algorithms/sequences/fibonnaci_sequence.py)

```
The Fibonacci Sequence to 20 iterations:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
```

[**Fizz Buzz - O(n)**](algorithms/sequences/fizzbuzz.py)

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

[**Bubble Sort - O(1)**](algorithms/sorting/bubble_sort.py)

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
venv/bin/python algorithms/category/script.py
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

## Attributions

Icons made by <a href="https://www.flaticon.com/authors/becris" title="Becris">Becris</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
