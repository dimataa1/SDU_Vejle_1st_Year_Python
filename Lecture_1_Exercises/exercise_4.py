"""
Try each expression and observe what Python does:

10 + * 2
(10 + 2
10 2
10 / 0
"10" / 2

For each one:
1. Predict whether it will work.
2. Run it.
3. Record the type of error Python reports.
4. Try to explain why the error occurred.
5. Correct the expression if possible.
6. Challenge: Are all programming errors the same type of error?
"""

# Run each of these ONE AT A TIME (comment out the others),
# since the program stops at the first error it hits.

##print(10 + * 2)      # SyntaxError: invalid syntax
#print((10 + 2)       # SyntaxError: '(' was never closed
#print(10 2)          # SyntaxError: invalid syntax
print(10 / 0)        # ZeroDivisionError: division by zero
print("10" / 2)      # TypeError: unsupported operand type(s) for /: 'str' and 'int'

# --- Corrected versions ---
print(10 + 2)          # 12
print((10 + 2))        # 12
print(10 * 2)          # 20 (assuming multiplication was intended)
print(10 / 1)          # 10.0 (avoid dividing by zero)
print(int("10") / 2)   # 5.0 (convert the string to a number first)

# Answers:
# 4. "10 + * 2", "(10 + 2", and "10 2" fail because Python can't even
#    parse them into valid code (missing/extra symbols). "10 / 0"
#    fails because division by zero is mathematically undefined.
#    "10" / 2 fails because you can't divide a string by a number.
# 6. No. SyntaxError happens before the code even runs (Python can't
#    understand it). ZeroDivisionError and TypeError are runtime
#    errors - the code is valid and starts running, but something
#    goes wrong while executing it.