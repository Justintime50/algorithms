# type: ignore

import json
import os
import string
from collections import Counter, defaultdict

# Place letters here that were incorrect and cannot be used again
DEAD_LETTERS = []

# Place letters here that were correct, but not in the right position (yellow background)
# and say what index they didn't work in, eg:
# {
#     'e': [0, 1],
#     'i': [2, 4],
#     'n': [0, 3],
#     'c': [2],
# }
CORRECT_LETTERS_WRONG_POSITIONS = {}

# Place your word guess here (starting word is `arose`)
VERIFIED_LETTERS = ['', '', '', '', '']


"""Do not edit code below this line!"""
ALPHABET = string.ascii_lowercase
NUM_BEST_GUESSES = 5  # The number of best guesses to return to the user


def main():
    """Wordle has two sets of lists (distinction unknown), all words in the lists are unique and
    are exactly 5 letters long."""
    # TODO: Longterm we should grab the lists from the site in the chance they get updated overtime
    short_list = _read_file(os.path.join('algorithms', 'assets', 'wordle_short_list.json'))
    long_list = _read_file(os.path.join('algorithms', 'assets', 'wordle_long_list.json'))
    combined_lists = short_list + long_list

    total_numbers = len(short_list + long_list)
    print('Total number of Wordles:', total_numbers)

    possible_words = get_best_guess(combined_lists)
    most_common_letters, possible_words = get_most_common(possible_words)
    best_words = get_best_words(most_common_letters, possible_words)

    print(f'Top {NUM_BEST_GUESSES} Best Guesses:')
    for word in best_words:
        print(word)


def get_most_common(possible_words):
    """Gets the most common starting letters and letters overall."""
    letter_start_count = defaultdict(int)
    letter_counts = defaultdict(int)

    # TODO: There are better ways than a double (triple) nested for loop (could we use zip instead?)
    for word in possible_words:
        for letter in ALPHABET:
            if word.startswith(letter):
                letter_start_count[letter] += 1
            for letter in word:
                if letter in ALPHABET:
                    letter_counts[letter] += 1

    most_common_start = Counter(letter_start_count).most_common()
    most_common_letters = Counter(letter_counts).most_common()
    print('Most common starting letter:', most_common_start)
    print('Most common letters:', most_common_letters)

    return most_common_letters, possible_words


def get_best_words(most_common_letters, possible_words):
    letter_probabilities = sorted(
        list(set(most_common_letters) - set(DEAD_LETTERS)),
        key=lambda x: x[1],
        reverse=True,
    )

    letter_weights = {}
    for weight, letter in enumerate(letter_probabilities):
        letter_weights[letter[0]] = len(letter_probabilities) - weight

    highest_ranking_words = {}
    possible_words_count = 0
    for word in possible_words:
        word_failed = False
        letters_that_match_criteria = 0
        for letter in [possible_letter[0] for possible_letter in letter_probabilities]:
            # Toss out words that don't match verified letter positions
            for index, verified_letter in enumerate(VERIFIED_LETTERS):
                if verified_letter != word[index] and verified_letter != '':
                    word_failed = True
                    break
            for (
                correct_letter,
                bad_positions,
            ) in CORRECT_LETTERS_WRONG_POSITIONS.items():
                for bad_position in bad_positions:
                    if correct_letter == word[bad_position]:
                        word_failed = True
                        break
            if letter in word:
                letters_that_match_criteria += 1

        if letters_that_match_criteria == 5 and not word_failed:
            word_weight = 0
            for letter in word:
                word_weight += letter_weights[letter[0]]
                highest_ranking_words[word] = word_weight

        if not word_failed:
            possible_words_count += 1

    print('Possible words:', possible_words_count)

    best_words = []
    for word, weight in sorted(
        highest_ranking_words.items(),
        key=lambda x: x[1],
        reverse=True,
    )[:NUM_BEST_GUESSES]:
        best_words.append((word, weight))

    return best_words


def get_best_guess(combined_lists):
    """Get the best guess based on probability from what's been eliminated,
    what was guess correctly, and what letters remain.
    """
    # TODO: Could we use zip here instead?
    possible_words = []
    for word in combined_lists:
        word_failed = False
        for dead_letter in DEAD_LETTERS:
            if dead_letter in word:
                word_failed = True
                break
        for correct_letter in CORRECT_LETTERS_WRONG_POSITIONS:
            if correct_letter not in word:
                word_failed = True
                break

        if word_failed is True:
            # do nothing as the word is not valid
            pass
        else:
            possible_words.append(word)

    return possible_words


def _read_file(filename):
    with open(filename, 'r') as data:
        word_list = json.load(data)

    return word_list


if __name__ == '__main__':
    main()
