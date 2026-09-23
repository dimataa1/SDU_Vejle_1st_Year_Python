"""
Task 8 - Find and correct the errors

Original code (with errors):

def polyline(n, length, angle)          # missing ":"
    for i in range(n):
        t.forward(Length)               # "Length" instead of "length" (case-sensitive)
        t.left(angle)
def polygon(n, length):
    angle = 360 / n
    polyline(length, angle)             # missing the "n" argument
polygon(5, 50)

Errors found:
1. Missing colon ":" at the end of the polyline() definition.
2. "Length" is capitalized but the parameter is named "length" -
   Python variable names are case-sensitive, so this causes a NameError.
3. polyline() is called with only 2 arguments (length, angle),
   but it requires 3 (n, length, angle).
"""

import turtle

t = turtle.Turtle()

def polyline(n, length, angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)

def polygon(n, length):
    angle = 360 / n
    polyline(n, length, angle)

polygon(5, 50)

turtle.done()