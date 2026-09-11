"""
Consider the code:

import math
number_of_students = 30
price = 150
discount = 10
total = number_of_students * price
discount_amount = total * discount
final_total = total - discount_amount
print("Final total:", round(final_Total, 2))

The programmer wants a 10% discount.
Find:
* the calculation error
* the naming error
* any other problem

Correct the program.
"""

number_of_students = 30
price = 150
discount = 0.10   # fixed: 10% must be written as 0.10, not 10

total = number_of_students * price
discount_amount = total * discount
final_total = total - discount_amount

print("Final total:", round(final_total, 2))   # fixed: matching capitalization

# Problems found:
# - Calculation error: discount=10 meant "multiply by 10" instead of
#   "10%", making discount_amount 10x too large.
# - Naming error: the code prints "final_Total" (capital T) but the
#   variable is "final_total" -> NameError.
# - Other problem: `import math` is unused, since no math functions
#   are actually called.