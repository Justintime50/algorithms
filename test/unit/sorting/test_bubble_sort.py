from algorithms import BubbleSort


def test_bubble_sort():
    bubble_sort = BubbleSort.sort()

    assert bubble_sort == [1, 2, 3, 4, 5, 6, 7, 8, 9]
