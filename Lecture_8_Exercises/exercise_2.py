"""
Task 2 - is_palindrome(word)

Returns True if the word reads the same backward.
is_palindrome('kayak') -> True

First build the reversed word with a loop and string concatenation.
Bonus: solve it with a single slice using a step (word[::-1]).
"""

def is_palindrome(word):
    """
    Checks whether 'word' reads the same forwards and backwards,
    using a loop to build the reversed string.

    word: the string to check
    """
    reversed_word = ""
    for char in word:
        # prepend each character to build the string in reverse order
        reversed_word = char + reversed_word
    return word == reversed_word


print(is_palindrome('kayak'))   # True
print(is_palindrome('python'))  # False


# --- Bonus: single slice solution ---
def is_palindrome_slice(word):
    """
    Checks whether 'word' is a palindrome using a single
    reversed slice instead of a manual loop.

    word: the string to check
    """
    # word[::-1] reverses the string using a step of -1
    return word == word[::-1]


print(is_palindrome_slice('kayak'))   # True
print(is_palindrome_slice('python'))  # False