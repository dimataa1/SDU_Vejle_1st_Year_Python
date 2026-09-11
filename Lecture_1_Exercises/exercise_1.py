"""
Python has two division operators: `/` and `//`.
Before running the code, predict the result of each expression:

17 / 5
17 // 5
20 / 4
20 // 4
-17 // 5

Then run them in Python.

1. What is the difference between `/` and `//`?
2. What type of value does each produce?
3. Does `//` simply remove the decimal part? Use the negative-number
   example to investigate.
"""

print(17 / 5)
print(17 // 5)
print(20 / 4)
print(20 // 4)
print(-17 // 5)

# Answers:
# 1. `/` is true division (always gives an exact decimal result).
#    `//` is floor division (divides then rounds DOWN to a whole number).
# 2. `/` always returns a float. `//` returns an int if both operands
#    are ints, or a float if either operand is a float.
# 3. No. `//` rounds toward negative infinity, not toward zero.
#    -17 // 5 = -4 (not -3), because -3.4 rounds down to -4, not
#    truncated to -3.