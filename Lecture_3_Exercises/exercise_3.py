"""
Create a function:

def show_circle(radius):
 
The function should:

Use the math module.
Calculate the area:
area = π × radius²
 
Calculate the circumference:
circumference = 2 × π × radius
 
Display radius, area, and circumference.
Round the calculated values to 2 decimal places.
Test:

show_circle(5)
show_circle(10)
"""

import math


def show_circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    print("Radius:", radius)
    print("Area:", round(area, 2))
    print("Circumference:", round(circumference, 2))


show_circle(5)
show_circle(10)