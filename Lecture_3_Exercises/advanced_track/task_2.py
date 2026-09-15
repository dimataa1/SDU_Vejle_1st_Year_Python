"""
Geometry Toolkit
Stage 1 — Shape Calculations

Create a program that can calculate the area of a rectangle, circle, and triangle.

Organise the calculations into functions and use the math module where appropriate.

Stage 2 — Shape Reports

For each shape, display a clear report containing the dimensions and calculated area. Round calculated values where appropriate.

Stage 3 — Interactive Geometry Calculator

Create a menu that allows the user to choose a shape, enter the required dimensions, and see the result.

The program should continue until the user chooses to exit and should handle invalid menu choices appropriately
"""

import math


def rectangle_area(width, height):
    return width * height


def circle_area(radius):
    return math.pi * radius ** 2


def triangle_area(base, height):
    return 0.5 * base * height


def show_rectangle_report(width, height):
    area = rectangle_area(width, height)
    print("\n----- RECTANGLE REPORT -----")
    print("Width:", width)
    print("Height:", height)
    print("Area:", round(area, 2))


def show_circle_report(radius):
    area = circle_area(radius)
    print("\n----- CIRCLE REPORT -----")
    print("Radius:", radius)
    print("Area:", round(area, 2))


def show_triangle_report(base, height):
    area = triangle_area(base, height)
    print("\n----- TRIANGLE REPORT -----")
    print("Base:", base)
    print("Height:", height)
    print("Area:", round(area, 2))


while True:
    print("\n----- GEOMETRY CALCULATOR -----")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Exit")

    choice = input("Choose a shape (1-4): ")

    if choice == "1":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        show_rectangle_report(width, height)

    elif choice == "2":
        radius = float(input("Enter radius: "))
        show_circle_report(radius)

    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        show_triangle_report(base, height)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")