"""
Create a folder called `Introduction-to-Programming` in Visual Studio
Code. Inside the folder, create a Python file called `week1.py`.

Imagine you are planning a one-day university workshop for 126
students. The students will work in groups of 8, the workshop lasts
6 hours, and the participation cost is 175 DKK per student.

Create a Python program that uses arithmetic expressions to calculate
and display:
* the number of complete groups of 8 students;
* the number of students who will not fit into a complete group;
* the total participation cost for all students;
* the total workshop time in minutes;
* the total workshop time in seconds;

Use different arithmetic operators and parentheses where appropriate.
Do not use variables yet.
"""

print("Complete groups of 8:", 126 // 8)
print("Students left over:", 126 % 8)
print("Total participation cost (DKK):", 126 * 175)
print("Total workshop time in minutes:", 6 * 60)
print("Total workshop time in seconds:", 6 * 60 * 60)