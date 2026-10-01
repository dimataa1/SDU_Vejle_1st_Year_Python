"""
Task 2 - Truth table comparison

Print all four rows of:
a  b  not (a and b)  (not a) or (not b)

Then confirm the two columns match.
"""

print("a      b      not(a and b)      (not a) or (not b)")

values = [True, False]

for a in values:
    for b in values:
        left = not (a and b)
        right = (not a) or (not b)
        print(a, "  ", b, "  ", left, "            ", right)

# Comment / Answer:
# Yes, "not (a and b)" is always equivalent to "(not a) or (not b)".
# This is an application of De Morgan's Law:
# not (a and b) == (not a) or (not b)
# All four rows produce matching values in both columns.