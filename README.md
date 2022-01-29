<div align="center">

# Algorithms

Classic algorithms including Fizz Buzz, Bubble Sort, the Fibonacci Sequence, a Sudoku solver, and more.

[![Build](https://github.com/Justintime50/algorithms/workflows/build/badge.svg)](https://github.com/Justintime50/algorithms/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/algorithms/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/algorithms?branch=main)
[![Licence](https://img.shields.io/github/license/justintime50/algorithms)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/algorithms/showcase.png" alt="Showcase">

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

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/algorithms/big_o_notation.png" alt="Showcase">

## Available Algorithms

### Recursion

[**Invert Binary Tree - O(n)**](algorithms/recursion/invert_binary_tree.py)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/algorithms/invert_binary_tree.png" alt="Showcase">

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

[**Wordle Solver - O(n^2)**](algorithms/sorting/wordle_solver.py)

```
Total number of Wordles: 12972
Most common starting letter: [('s', 1565), ('c', 922), ('b', 909), ('p', 859), ('t', 815), ('a', 737), ('m', 693), ('d', 685), ('g', 638), ('r', 628), ('f', 598), ('l', 577), ('h', 489), ('w', 413), ('k', 376), ('n', 325), ('e', 303), ('o', 262), ('v', 242), ('j', 202), ('u', 189), ('y', 181), ('i', 165), ('z', 105), ('q', 78), ('x', 16)]
Most common letters: [('s', 173290), ('e', 173212), ('a', 155740), ('o', 115388), ('r', 108108), ('i', 97734), ('l', 87646), ('t', 85670), ('n', 76752), ('u', 65286), ('d', 63778), ('y', 53924), ('c', 52728), ('p', 52494), ('m', 51376), ('h', 45760), ('g', 42744), ('b', 42302), ('k', 39130), ('f', 28990), ('w', 27014), ('v', 18044), ('z', 11284), ('j', 7566), ('x', 7488), ('q', 2912)]
Possible words: 12972
Top 5 Best Guesses:
('arose', 120)
('aeros', 120)
('soare', 120)
('arise', 118)
('raise', 118)
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
# Get a comprehensive list of development tools
make help
```

## Contributing

I will not be accepting pull requests to this repo for new algorithms as this project is more of a playground for my own learning and exploration of algorithms and not an exhaustive collection for reference. I will consider improvement PRs for existing algorithms however.
