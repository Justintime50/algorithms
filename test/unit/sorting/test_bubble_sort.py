from algorithms.sorting.bubble_sort import bubble_sort


def test_bubble_sort():
    sorted_list = bubble_sort()

    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]
