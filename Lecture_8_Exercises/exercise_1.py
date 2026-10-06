"""
Task 1 - to_leet(text) and count_letter(text, letter)

to_leet(text): returns a copy of text with letters replaced:
a -> 4, e -> 3, i -> 1, o -> 0, s -> 5 (case-insensitive)

count_letter(text, letter): counts occurrences of letter,
case-insensitively.
"""

def to_leet(text):
    """
    Converts text into "leetspeak" by replacing certain letters
    with numbers that resemble them, case-insensitively.

    text: the string to convert
    """
    replacements = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5',
    }

    result = ""
    for char in text:
        lower_char = char.lower()
        if lower_char in replacements:
            result += replacements[lower_char]
        else:
            # keep the original character (including its case) unchanged
            result += char
    return result


def count_letter(text, letter):
    """
    Counts how many times 'letter' appears in 'text',
    ignoring case.

    text: the string to search through
    letter: the single character to count
    """
    count = 0
    for char in text:
        if char.lower() == letter.lower():
            count += 1
    return count


print(to_leet("Leetspeak is awesome"))   # L33t5p34k 15 4w3s0m3
print(count_letter("Mississippi", "s"))  # 4
print(count_letter("Mississippi", "S"))  # 4 (case-insensitive)