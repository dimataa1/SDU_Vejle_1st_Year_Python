"""
The `abs()` function computes the absolute value of a number.
Predict the result of:

abs(-15)
abs(15)
abs(-3.7)
abs(0)

Now experiment.
1. What happens if you write: abs("15")
2. What type of error do you get?
3. Why do you think Python accepts `abs(-15)` but not `abs("15")`?
"""

print(abs(-15))
print(abs(15))
print(abs(-3.7))
print(abs(0))

# Now try this - it raises an error
print(abs("15"))

# Answers:
# 1. It raises an error instead of returning a value.
# 2. TypeError: bad operand type for abs(): 'str'
# 3. abs() only makes sense for numbers (it needs to know the numeric
#    sign to possibly flip it). A string has no numeric sign, so
#    Python refuses rather than guessing/auto-converting it.