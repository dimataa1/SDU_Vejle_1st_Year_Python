"""
Use: import math

A circle has radius 4.75 m.
Calculate:
* diameter
* circumference
* area

Use math.pi and round results to 2 decimals.
"""

import math

radius = 4.75

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("Diameter:", round(diameter, 2), "m")
print("Circumference:", round(circumference, 2), "m")
print("Area:", round(area, 2), "m^2")