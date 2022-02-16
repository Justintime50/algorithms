import os

from algorithms.sorting.wordle_solver import _read_file, get_best_guess, get_most_common


def test_get_most_common():
    file_data = _read_file(os.path.join('algorithms', 'assets', 'wordle_answer_list.json'))
    most_common_start, most_common_letters, possible_words = get_most_common(file_data)

    assert type(most_common_start) == list
    assert type(most_common_letters) == list
    assert type(possible_words) == list


def test_get_best_guess():
    file_data = _read_file(os.path.join('algorithms', 'assets', 'wordle_answer_list.json'))
    best_guess = get_best_guess(file_data)

    assert type(best_guess) == list


def test_read_file():
    answer_file_data = _read_file(os.path.join('algorithms', 'assets', 'wordle_answer_list.json'))
    non_answer_file_data = _read_file(
        os.path.join('algorithms', 'assets', 'wordle_non_answer_possible_words_list.json')
    )

    assert len(answer_file_data) == 2309
    assert len(non_answer_file_data) == 10638
