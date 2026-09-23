"""
Task 9 - Fibonacci sequence

Encapsulate and generalize the code by creating:

def show_fibonacci(n):

Requirements:
- Use n to control how many Fibonacci numbers are printed.
- Start with first = 0 and second = 1.
- Use a for loop with range(n).
- Update first and second correctly.

Expected output for show_fibonacci(5):
0
1
1
2
3
"""

def show_fibonacci(n):
    first = 0
    second = 1
    for i in range(n):
        print(first)
        # calculate the next number before overwriting first and second
        next_number = first + second
        first = second
        second = next_number

show_fibonacci(5)
show_fibonacci(8)