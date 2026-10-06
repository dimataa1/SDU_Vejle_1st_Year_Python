"""
Task 5 - American-spelling edition using re.sub

Produce an American-spelling edition of frankenstein_cleaned.txt,
normalizing:
  cent(re|er) -> center
  colou?r     -> color
  gray        -> grey   (note: this is actually BrE -> AmE reversed;
                          kept as stated in the task)
  traveller   -> traveler

Report the total number of replacements made by comparing .count
of each spelling before and after.

Challenge: censor(text, words) replaces each occurrence of a word
in 'words' with '*' repeated len(word) times, using re.sub in a loop.
"""

import re


def americanize(input_file, output_file):
    """
    Reads a text file, normalizes certain British/alternate spellings
    to their American equivalents, and writes the result to a new file.
    Reports how many replacements were made for each pattern.

    input_file: path to the source text file
    output_file: path to write the converted text to
    """
    with open(input_file, encoding='utf-8') as f:
        text = f.read()

    total_replacements = 0

    patterns = [
        (r'cent(re|er)', 'center'),
        (r'colou?r', 'color'),
        (r'gray', 'grey'),
        (r'traveller', 'traveler'),
    ]

    for pattern, replacement in patterns:
        # count matches before replacing, using the same pattern
        matches_before = len(re.findall(pattern, text, flags=re.IGNORECASE))
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        total_replacements += matches_before

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

    return total_replacements


replacements_made = americanize(
    "frankenstein_cleaned.txt",
    "frankenstein_american.txt"
)
print("Total replacements made:", replacements_made)


# --- Challenge: censor(text, words) ---
def censor(text, words):
    """
    Replaces every occurrence of each word in 'words' with a string
    of asterisks of the same length, using re.sub in a loop.

    text: the string to censor
    words: a list of words to censor out
    """
    for word in words:
        stars = '*' * len(word)
        # \b ensures only whole-word matches are censored
        pattern = r'\b' + re.escape(word) + r'\b'
        text = re.sub(pattern, stars, text, flags=re.IGNORECASE)
    return text


sample = "The monster frightened the villagers near the castle."
print(censor(sample, ["monster", "villagers"]))
# Output: "The ******* frightened the ********* near the castle."