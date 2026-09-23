"""
Task 5 - Interface vs Implementation

def circle(radius):
    circumference = 2 * math.pi * radius
    n = 30
    length = circumference / n
    polygon(n, length)

circle(50)

Classification:
- circle              -> interface  (the function name, part of what the user calls)
- radius              -> interface  (the parameter the user must provide)
- circle(50)          -> interface  (the actual call the user makes)
- circumference       -> implementation (internal variable, hidden detail)
- n = 30              -> implementation (internal choice of how many sides to use)
- length = circumference / n -> implementation (internal calculation)
- calling polygon() internally -> implementation (hidden helper call)

What does someone need to know to use circle()?
Only that circle() takes one parameter, radius (a number),
and draws an approximate circle with that radius.
They do NOT need to know that it uses n = 30 sides,
how the side length is calculated, or that it calls polygon() internally.
"""