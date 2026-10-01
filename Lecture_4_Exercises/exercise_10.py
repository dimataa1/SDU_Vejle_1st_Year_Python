"""
Task 10 - Small program covering Chapters 1-4 concepts
(functions, loops, encapsulation, generalization)

Part 1: show_number(number, times)
Part 2: show_fibonacci(n)
Part 3 & 4: print_separator(char, times) - avoids repeated code, generalized
Part 5: fibonacci_report(n) - reuses the other functions
Part 6: docstrings and comments added
Part 7: design questions answered at the bottom
"""

def show_number(number, times):
    """
    Prints a given number a specified number of times.

    number: the value to print
    times: how many times to print it
    """
    for i in range(times):
        print(number)


def show_fibonacci(n):
    """
    Prints the first n numbers of the Fibonacci sequence.

    n: how many Fibonacci numbers to display
    """
    first = 0
    second = 1
    for i in range(n):
        print(first)
        # calculate the next Fibonacci number before updating first/second
        next_number = first + second
        first = second
        second = next_number


def print_separator(char, times):
    """
    Prints a separator line made of a repeated character.

    char: the character to repeat
    times: how many times to repeat it
    """
    # multiplying a string by an integer repeats it "times" times
    print(char * times)


def fibonacci_report(n):
    """
    Prints a full report containing a title and the Fibonacci sequence.

    n: how many Fibonacci numbers to include in the report
    """
    print_separator("-", 20)
    print("FIBONACCI SEQUENCE")
    print_separator("-", 20)
    # reuse the existing function instead of duplicating the loop logic
    show_fibonacci(n)
    print_separator("-", 20)


# --- Tests ---
show_number(5, 3)
show_number(10, 5)

show_fibonacci(5)
show_fibonacci(10)

print_separator("-", 20)
print_separator("*", 20)
print_separator("=", 20)

fibonacci_report(8)


"""
Part 7 - Design questions

1. Example of encapsulation:
   print_separator() hides how the separator line is built;
   the caller doesn't need to know it's just char * times.

2. Example of generalization:
   print_separator(char, times) works with any character and
   any length, instead of being fixed to "-" * 20.

3. Which function calls another function:
   fibonacci_report() calls both print_separator() and show_fibonacci().

4. Example of a local variable:
   next_number inside show_fibonacci() - it only exists while
   the function is running.

5. Interface of show_fibonacci():
   It takes one parameter, n (an integer), and prints the first
   n numbers of the Fibonacci sequence. That is all a user needs
   to know to use it.

6. Reasonable precondition for show_fibonacci():
   n must be a positive integer (n >= 1).

7. Postcondition:
   After calling show_fibonacci(n), exactly n lines are printed,
   representing the first n Fibonacci numbers starting from 0.

8. Where repeated code was avoided:
   The separator line "--------------------" was printed with
   repeated print() statements; instead it was encapsulated into
   print_separator() and reused everywhere, including inside
   fibonacci_report().
"""