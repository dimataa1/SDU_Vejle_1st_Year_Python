"""
Task 1 - Count occurrences of the letter 's' in a word

Test with:
mississipi
Saskatchewan
snowy sunset
"""

def count_s(word):
    """
    Counts how many times the letter 's' (case-insensitive)
    appears in the given word/string.

    word: the string to search through
    """
    count = 0
    for letter in word:
        # convert to lowercase so 'S' and 's' both count
        if letter.lower() == 's':
            count += 1
    return count


print(count_s('mississipi'))     # 4
print(count_s('Saskatchewan'))   # 2
print(count_s('snowy sunset'))   # 3