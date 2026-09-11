"""
Without running Python first, predict the type of the value produced
by each expression:

100 / 4
100 // 4
5 * 3
5.0 * 3
"Python"
"10" + "20"
abs(-8.5)
round(9.8)

Then use `type()` to check each prediction.
For example: type(100 / 4)

1. Why is `100 / 4` different in type from `100 // 4`?
2. What happens with `"10" + "20"`? Why?
"""

print(type(100 / 4))
print(type(100 // 4))
print(type(5 * 3))
print(type(5.0 * 3))
print(type("Python"))
print(type("10" + "20"))
print(type(abs(-8.5)))
print(type(round(9.8)))

# Answers:
# 1. `/` (true division) always returns a float in Python 3, even
#    when the result is a whole number (100/4 = 25.0). `//` (floor
#    division) returns an int when both operands are ints (100//4 = 25).
# 2. "10" + "20" gives "1020" (a string), not 30. With strings, `+`
#    means concatenation (joining text together), not addition.