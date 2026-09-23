"""
Description
The following code draws a rectangle:

for i in range(2):
    t.forward(120)
    t.left(90)
    t.forward(60)
    t.left(90)
Put the code inside a function called:
def rectangle():
Call the function and check that it still draws the same rectangle.
"""

import turtle
t = turtle.Turtle()

def rectangle():
    for i in range(2):
        t.forward(120)
        t.left(90)
        t.forward(60)
        t.left(90)

rectangle()
turtle.done()