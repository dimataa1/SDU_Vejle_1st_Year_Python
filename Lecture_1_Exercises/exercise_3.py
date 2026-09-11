"""
Consider these expressions:

8 + 4 * 3
(8 + 4) * 3
8 + (4 * 3)
(8 + 4 * 3)

Before running them:
1. Predict the value of each expression.
2. Which expressions do you think will have the same value?
Now use Python to check your predictions.
"""

print(8 + 4 * 3)
print((8 + 4) * 3)
print(8 + (4 * 3))
print((8 + 4 * 3))

# Answers:
# 1. 8+4*3 = 20, (8+4)*3 = 36, 8+(4*3) = 20, (8+4*3) = 20
# 2. Expressions 1, 3, and 4 are all equal (20), because multiplication
#    happens before addition by default - the parentheses in those
#    cases don't change anything. Only (8+4)*3 differs (36) because
#    the parentheses force the addition to happen first.