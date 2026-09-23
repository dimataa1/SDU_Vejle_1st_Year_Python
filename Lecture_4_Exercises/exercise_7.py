"""
Task 7 - Preconditions and postconditions

def polygon(n, length):
    angle = 360 / n
    polyline(n, length, angle)

A. Which calls satisfy reasonable preconditions?

polygon(5, 50)    -> reasonable
polygon(2, 50)    -> NOT reasonable (a polygon needs at least 3 sides)
polygon(6, -20)   -> NOT reasonable (negative length makes no sense)
polygon(3, 100)   -> reasonable

B. Two reasonable preconditions for polygon():
1. n must be an integer greater than or equal to 3.
2. length must be a positive number (length > 0).

C. One postcondition describing what should happen after polygon(5, 50):
The turtle draws a regular pentagon with side length 50,
and ends up back at its starting position and orientation
(the shape is closed).
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