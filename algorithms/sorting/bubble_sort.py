# import time
from datetime import datetime

"""
BUBBLE SORT

Description: Bubble Sort is the simplest sorting algorithm that works by
repeatedly swapping the adjacent elements if they are in wrong order.

Usage: venv/bin/python bubble_sort.py

Features:
- Lists can contain multiple duplicate values and still sort properly
- Timestamps show how quickly your data was sorted
- View what numbers were swapped in each step

Lessons Learned:
- 1) The numbers in the list are inconsequential - it's all about the index
and positioning of those numbers.
- 2) Simply iterating over each number isn't good enough, it'll only run once
and never do a second pass.
- 3) This quickly breaks down when you have two values that are the same,
because it will shift a lower value down and the check fails if the next
number is bigger so it thinks it's done.
"""

LIST = [3, 1, 5, 9, 7, 6, 2, 8, 4]


class BubbleSort():
    def sort():
        """Bubble sort a list
        """
        previous_index = 0
        next_index = 1
        new_array = LIST
        i = 1
        num_times_skipped = 0

        print(f'Original: {LIST}')
        start_time = datetime.now()
        while num_times_skipped + 1 != len(LIST):
            # print(i)
            try:
                if (LIST[next_index] < LIST[previous_index]
                        and LIST[next_index] != LIST[previous_index]):
                    new_array.insert(next_index, new_array.pop(previous_index))
                    print(
                        f'{new_array} => Swapped {LIST[next_index]} and {LIST[previous_index]}')
                    # time.sleep(0.1)
                    previous_index += 1
                    next_index += 1
                else:
                    previous_index += 1
                    next_index += 1
                    num_times_skipped += 1
                    # print('Skipped')
            except IndexError:
                # print(f'{i} pass(es) complete!')
                previous_index = 0
                next_index = 1
                num_times_skipped = 0
                i += 1
        end_time = datetime.now() - start_time
        print(f'List sorted successfully in {end_time} with Bubble Sort Algorithm!')
        return new_array


def main():
    BubbleSort.sort()


if __name__ == '__main__':
    main()
