"""
Task 6 - Improve this function with docstring and comments

Add:
- a docstring explaining what the function does
- an explanation of width
- an explanation of height
- one useful comment inside the function

Answer:
What is the difference between a docstring and a comment?

A docstring explains the INTERFACE of a function - what it does
and what parameters it expects. It is written right after the
function definition and can be accessed with help() or __doc__.

A comment explains something about the IMPLEMENTATION - a detail
about how the code works internally. It is only visible in the
source code itself.
"""

import turtle

t = turtle.Turtle()

def rectangle(width, height):
    """
    Draws a rectangle using the turtle.

    width: the length of the horizontal sides
    height: the length of the vertical sides
    """
    for i in range(2):
        t.forward(width)
        t.left(90)
        # after drawing one horizontal and one vertical side,
        # turning 90 degrees twice completes each corner of the rectangle
        t.forward(height)
        t.left(90)

rectangle(120, 60)

turtle.done()