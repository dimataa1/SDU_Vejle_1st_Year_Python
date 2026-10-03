"""
Task 4 - Find vowel-less words using uses_none

Write a function that finds words with no vowels, using a
helper function uses_none(word, letters).

Count the number of vowel-less words in words.txt.
"""

def uses_none(word, forbidden_letters):
    """
    Checks whether 'word' contains none of the letters in
    'forbidden_letters'.

    word: the string to check
    forbidden_letters: a string containing letters that must NOT appear
    """
    for letter in word:
        if letter in forbidden_letters:
            return False
    return True


def is_vowel_less(word):
    """
    Checks whether a word contains no vowels (a, e, i, o, u).

    word: the string to check
    """
    return uses_none(word, "aeiou")


print(is_vowel_less("sky"))    # True
print(is_vowel_less("hello"))  # False


# --- Count vowel-less words in words.txt ---
def count_vowel_less(filename):
    """
    Counts how many words in the file contain no vowels.

    filename: path to a text file with one word per line
    """
    count = 0
    with open('words.txt') as f:
        for line in f:
            word = line.strip()
            if is_vowel_less(word):
                count += 1
    return count


print(count_vowel_less('words.txt'))