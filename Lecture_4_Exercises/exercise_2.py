"""
Description
Your rectangle() function always draws the same size.


import turtle

t= turtle.Turtle(


def rectangle(width, height):

    for i in range(2):

        t.forward(width)

        t.left(90)

        t.forward(height)

        t.left(90)

 
rectangle(120, 60)



turtle.done()



 

Generalize it to:

def rectangle(width, height):
Requirements:

Replace the fixed values with width and height.
Keep the loop.
Test it with:
rectangle(120, 60)
rectangle(200, 100)
rectangle(80, 150)
"""

import turtle
t = turtle.Turtle()

def rectangle(width, height):
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

rectangle(120, 60)
rectangle(200, 100)
rectangle(80, 150)

turtle.done()