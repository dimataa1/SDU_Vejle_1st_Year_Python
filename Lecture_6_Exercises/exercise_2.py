"""
Task 2 - One-line function to check divisibility

is_multiple(a, b) should return whether a is divisible by b
(i.e. b divides a with no remainder).
"""

def is_multiple(a, b):
    return a % b == 0


print(is_multiple(12, 4))  # True  (12 / 4 = 3 exactly)
print(is_multiple(12, 5))  # False (12 / 5 leaves a remainder)