"""
Task 3 - Score to letter grade

A = (100, 95)
B = (94, 90)
C = (89, 80)
D = (79, 65)
E = (64, 50)
F = (49, 0)

Requirement: test exactly at each boundary and note results in comments.
"""

def letter_grade(score):
    """
    Converts a numeric score (0-100) to a letter grade (A-F).

    score: an integer or float from 0 to 100
    """
    if score >= 95:
        return "A"
    elif score >= 90:
        return "B"
    elif score >= 80:
        return "C"
    elif score >= 65:
        return "D"
    elif score >= 50:
        return "E"
    else:
        return "F"


# --- Boundary tests ---
print(letter_grade(100))  # A  (top of A range)
print(letter_grade(95))   # A  (lower boundary of A)
print(letter_grade(94))   # B  (upper boundary of B)
print(letter_grade(90))   # B  (lower boundary of B)
print(letter_grade(89))   # C  (upper boundary of C)
print(letter_grade(80))   # C  (lower boundary of C)
print(letter_grade(79))   # D  (upper boundary of D)
print(letter_grade(65))   # D  (lower boundary of D)
print(letter_grade(64))   # E  (upper boundary of E)
print(letter_grade(50))   # E  (lower boundary of E)
print(letter_grade(49))   # F  (upper boundary of F)
print(letter_grade(0))    # F  (bottom of F range)

# All boundaries land in the expected grade with no gaps or overlaps,
# because using ">=" checks in descending order correctly covers
# every value between two boundaries.