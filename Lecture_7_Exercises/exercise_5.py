"""
Task 5 - Find the longest word in words.txt that does not contain 'e'

Reuses the idea of uses_none from Task 4, checking against
just the letter 'e'.
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


def longest_word_without_e(filename):
    """
    Finds the longest word in the file that does not contain
    the letter 'e'.

    filename: path to a text file with one word per line
    """
    longest = ""

    with open('words.txt') as f:
        for line in f:
            word = line.strip()
            if uses_none(word, "e"):
                # keep track of the longest word found so far
                if len(word) > len(longest):
                    longest = word

    return longest


print(longest_word_without_e('words.txt'))