"""
Description
You already have:

def polygon(n, length):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)
Create:
def circle(radius):
Requirements:
Calculate the circumference using math.pi.
Store n = 30.
Calculate the length of each small side.
Call polygon() to draw the approximate circle.
Do not create another drawing loop inside circle().
Test:

circle(30)
"""

import math
import turtle

t = turtle.Turtle()

def rectangle(width, height):
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def polygon(n, length):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)

def circle(radius):
    circumference = 2 * math.pi * radius
    n = 30
    length = circumference / n
    polygon(n, length)

circle(30)