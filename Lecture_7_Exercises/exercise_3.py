"""
Task 3 - is_abecedarian(word)

Checks whether the letters of a word are in alphabetical order.

is_abecedarian('billowy') -> True
is_abecedarian('python')  -> False

Count how many words in words.txt are abecedarian,
then find the longest one.

Hint: use the < operator between two strings (characters).
"""

def is_abecedarian(word):
    """
    Checks whether the letters in word appear in non-decreasing
    alphabetical order.

    word: the string to check
    """
    for i in range(len(word) - 1):
        # if a later letter is smaller than the one before it,
        # the word is not in alphabetical order
        if word[i + 1] < word[i]:
            return False
    return True


print(is_abecedarian('billowy'))  # True
print(is_abecedarian('python'))   # False


# --- Count abecedarian words and find the longest one ---
def abecedarian_stats(filename):
    """
    Counts the abecedarian words in the file and finds the longest one.

    filename: path to a text file with one word per line
    """
    count = 0
    longest = ""

    with open('words.txt') as f:
        for line in f:
            word = line.strip()
            if is_abecedarian(word):
                count += 1
                if len(word) > len(longest):
                    longest = word

    return count, longest


total, longest_word = abecedarian_stats('words.txt')
print("Count:", total)
print("Longest abecedarian word:", longest_word)