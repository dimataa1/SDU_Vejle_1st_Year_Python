"""
Task 2 - has_double(word) using words.txt

Returns True if the word has two identical adjacent letters.

has_double('billowy') -> True   ('ll')
has_double('python')  -> False

Then count how many words in words.txt have a double letter.
"""

def has_double(word):
    """
    Checks whether a word contains two identical adjacent letters.

    word: the string to check
    """
    for i in range(len(word) - 1):
        # compare each letter with the one right after it
        if word[i] == word[i + 1]:
            return True
    return False


print(has_double('billowy'))   # True
print(has_double('python'))    # False


# --- Count words with a double letter in words.txt ---
def count_doubles(filename):
    """
    Counts how many words in the given file have a double letter.

    filename: path to a text file with one word per line
    """
    count = 0
    with open('words.txt') as f:
        for line in f:
            word = line.strip()  # remove trailing newline/whitespace
            if has_double(word):
                count += 1
    return count


print(count_doubles('words.txt'))