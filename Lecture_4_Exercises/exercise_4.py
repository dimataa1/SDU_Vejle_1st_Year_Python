"""
Create a reusable function:

def polyline(n, length, angle):
Move the repeated drawing code from polygon() into polyline().

Then refactor polygon() so that it calculates the angle and calls polyline().

Your final program should allow:

polygon(3, 50)
polygon(4, 50)
polygon(6, 50)
 
Important: polygon() should not contain its own for loop after refactoring.
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

polygon(3, 50)
polygon(4, 50)
polygon(6, 50)

turtle.done()