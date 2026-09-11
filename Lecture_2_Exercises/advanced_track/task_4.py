"""
DNA Sequence Analyzer

Stage 1 — Data Validation
Ask the user to input a short DNA sequence string (e.g., "ATCGG").
Use a loop to check every character. If the string contains any
letters other than A, T, C, or G, print "Invalid DNA sequence" and
ask again.

Stage 2 — Complementary Strand
In DNA, 'A' pairs with 'T', and 'C' pairs with 'G'. Loop through the
user's valid DNA string and construct a new string representing the
complementary strand. Print it out (inputting "ATCG" outputs "TAGC").

Stage 3 — Mutation Scanner
Ask the user to input a second DNA sequence of the exact same length
as the first. Loop through both strings simultaneously. Count how
many times the characters at the same position do not match. Print
out the total number of "mutations" and calculate the percentage of
the DNA that has been mutated.
"""

valid_bases = "ATCG"
pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}


def get_valid_dna(prompt):
    while True:
        sequence = input(prompt).upper()
        if len(sequence) > 0 and all(base in valid_bases for base in sequence):
            return sequence
        else:
            print("Invalid DNA sequence. Please use only A, T, C, and G.")


# First sequence
dna_1 = get_valid_dna("Enter the first DNA sequence: ")

complementary_strand = ""
for base in dna_1:
    complementary_strand = complementary_strand + pairs[base]
print("Complementary strand:", complementary_strand)

# Second sequence (must be same length)
while True:
    dna_2 = get_valid_dna("Enter the second DNA sequence (same length): ")
    if len(dna_2) == len(dna_1):
        break
    else:
        print(f"Length mismatch! First sequence has {len(dna_1)} bases, please match it.")

# Compare the two sequences
mutations = 0
for i in range(len(dna_1)):
    if dna_1[i] != dna_2[i]:
        mutations = mutations + 1

mutation_percentage = (mutations / len(dna_1)) * 100

print("Sequence 1:", dna_1)
print("Sequence 2:", dna_2)
print("Total mutations:", mutations)
print("Mutation percentage:", round(mutation_percentage, 2), "%")