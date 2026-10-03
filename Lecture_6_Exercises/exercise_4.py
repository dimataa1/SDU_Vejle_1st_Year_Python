"""
Task 4 - Recursive digit_sum(n)

digit_sum(2026) should return 2+0+2+6 = 10

Afterwards, add type checking so it only accepts integers,
and prints an error message otherwise.

Hint: use // and % to separate the last digit from the rest.
"""

def digit_sum(n):
    """
    Recursively sums the digits of a non-negative integer n.

    n: an integer whose digits will be summed
    """
    if not isinstance(n, int):
        print("Error: digit_sum() only accepts integer input.")
        return None

    # work with the absolute value, in case n is negative
    n = abs(n)

    if n < 10:
        # base case: a single digit is its own digit sum
        return n
    else:
        # last digit + recursive sum of the remaining digits
        last_digit = n % 10
        remaining = n // 10
        return last_digit + digit_sum(remaining)


print(digit_sum(2026))     # 10
print(digit_sum(9))        # 9
print(digit_sum(100))      # 1
print(digit_sum("2026"))   # Error message, returns None
print(digit_sum(3.14))     # Error message, returns None