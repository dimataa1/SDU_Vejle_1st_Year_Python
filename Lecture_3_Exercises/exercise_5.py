"""
A prime number has exactly two factors: 1 and itself.

For this exercise, we already know that 7 is a prime number.

Create a function:

def explore_prime(prime_number):
 
The function should:

Calculate the square of the prime number.
Calculate the next number after the prime number.
Calculate the previous number before the prime number.
Display all the results.
Test your function
explore_prime(7)
explore_prime(13)
 
Expected output for 7:

Prime number: 7
Previous number: 6
Next number: 8
Square: 49
"""

def explore_prime(prime_number):
    square = prime_number ** 2
    next_number = prime_number + 1
    previous_number = prime_number - 1

    print("Prime number:", prime_number)
    print("Previous number:", previous_number)
    print("Next number:", next_number)
    print("Square:", square)


explore_prime(7)
explore_prime(13)