"""
Task 4 - clean_file(input_file, output_file)

Copies only the book text between the two *** marker lines of
any Project Gutenberg file (two-loop pattern: first loop skips
until the starting marker, second loop copies until the ending
marker).

Run it on Pride and Prejudice (ebook #1342) and report the total
number of lines and blank lines.
"""

import urllib.request


def clean_file(input_file, output_file):
    """
    Extracts only the actual book text from a Project Gutenberg
    file, removing the header and footer boilerplate that is
    separated by lines containing '***'.

    input_file: path to the raw downloaded Gutenberg text file
    output_file: path to write the cleaned book text to
    """
    with open(input_file, encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:

        # First loop: skip lines until we reach the starting marker
        for line in infile:
            if '*** START' in line or '***START' in line:
                break

        # Second loop: copy lines until we reach the ending marker
        for line in infile:
            if '*** END' in line or '***END' in line:
                break
            outfile.write(line)


def download_book(url, filename):
    """
    Downloads a text file from a given URL and saves it locally.

    url: the URL of the Project Gutenberg text file
    filename: local path to save the downloaded file to
    """
    urllib.request.urlretrieve(url, filename)


def report_stats(filename):
    """
    Reports the total number of lines and blank lines in a file.

    filename: path to the file to analyze
    """
    total_lines = 0
    blank_lines = 0

    with open(filename, encoding='utf-8') as f:
        for line in f:
            total_lines += 1
            if line.strip() == "":
                blank_lines += 1

    return total_lines, blank_lines


# --- Run on Pride and Prejudice (ebook #1342) ---
url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
download_book(url, "pg1342_raw.txt")
clean_file("pg1342_raw.txt", "pg1342_cleaned.txt")

total, blanks = report_stats("pg1342_cleaned.txt")
print("Total lines:", total)
print("Blank lines:", blanks)

# Note: this requires an active internet connection to run,
# since it downloads the book directly from Project Gutenberg.