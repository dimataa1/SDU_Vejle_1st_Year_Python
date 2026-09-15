"""
Text Analyzer
Stage 1 — Basic Text Analysis

Ask the user to enter a sentence. Display the number of characters, words, and vowels in the text.

Structure the analysis using functions.

Stage 2 — Detailed Analysis

Extend the program to report additional information, such as the number of uppercase letters, lowercase letters, digits, and spaces.

Present the results as a clear text-analysis report.

Stage 3 — Advanced Text Analysis

Extend the program to identify the longest word and calculate the percentage of characters that are vowels.

Add at least one additional text-analysis feature of your own.
"""

def count_characters(text):
    return len(text)


def count_words(text):
    return len(text.split())


def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def count_uppercase(text):
    return sum(1 for char in text if char.isupper())


def count_lowercase(text):
    return sum(1 for char in text if char.islower())


def count_digits(text):
    return sum(1 for char in text if char.isdigit())


def count_spaces(text):
    return sum(1 for char in text if char == " ")


def find_longest_word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)


def count_consonants(text):
    # Extra feature: count consonant letters
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)


def show_text_report(text):
    total_chars = count_characters(text)
    total_words = count_words(text)
    total_vowels = count_vowels(text)
    total_upper = count_uppercase(text)
    total_lower = count_lowercase(text)
    total_digits = count_digits(text)
    total_spaces = count_spaces(text)
    longest_word = find_longest_word(text)
    total_consonants = count_consonants(text)

    vowel_percentage = (total_vowels / total_chars) * 100 if total_chars > 0 else 0

    print("\n----- TEXT ANALYSIS REPORT -----")
    print("Text:", text)
    print("Characters:", total_chars)
    print("Words:", total_words)
    print("Vowels:", total_vowels)
    print("Consonants:", total_consonants)
    print("Uppercase letters:", total_upper)
    print("Lowercase letters:", total_lower)
    print("Digits:", total_digits)
    print("Spaces:", total_spaces)
    print("Longest word:", longest_word)
    print("Vowel percentage:", round(vowel_percentage, 2), "%")


sentence = input("Enter a sentence: ")
show_text_report(sentence)