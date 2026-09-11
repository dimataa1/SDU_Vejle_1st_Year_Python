"""
Find and fix the problems:

a = 24
b = "250"
total = a + b
print("Students:", A)
print("Total:", total)

The program should calculate the total fee for 24 students paying
250 DKK each. Also improve the variable names.
"""

# Problems found:
# - `b` is a string ("250") added to an int -> TypeError
# - print(..., A) uses "A" (capital), which was never defined
#   (only "a" lowercase exists) -> NameError
# - "a" and "b" are not meaningful variable names

num_students = 24
fee_per_student = 250
total = num_students * fee_per_student   # multiply, not add

print("Students:", num_students)
print("Total:", total)