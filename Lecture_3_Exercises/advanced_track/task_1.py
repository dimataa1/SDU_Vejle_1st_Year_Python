"""
Number Analysis Toolkit
Stage 1 — Number Information

Ask the user for a number and display its square and cube. Organise the program using functions rather than putting all calculations in one block of code.

Stage 2 — Number Properties

Extend the program so that it also determines whether the number is positive, negative, or zero, and whether it is even or odd.

Display all the information as a clear number report.

Stage 3 — Prime Number Analysis

Extend the program to determine whether the number is a prime number.

Finally, allow the user to enter different numbers and generate a complete analysis for each number.
"""

def get_square(number):
    return number ** 2


def get_cube(number):
    return number ** 3


def get_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


def get_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def show_number_report(number):
    square = get_square(number)
    cube = get_cube(number)
    sign = get_sign(number)
    even_odd = get_even_odd(number)
    prime_status = "Prime" if is_prime(number) else "Not prime"

    print("\n----- NUMBER REPORT -----")
    print("Number:", number)
    print("Square:", square)
    print("Cube:", cube)
    print("Sign:", sign)
    print("Even/Odd:", even_odd)
    print("Prime check:", prime_status)


while True:
    user_input = input("\nEnter a number to analyze (or 'q' to quit): ")
    if user_input.lower() == "q":
        print("Goodbye!")
        break

    try:
        number = int(user_input)
        show_number_report(number)
    except ValueError:
        print("Please enter a valid whole number.")