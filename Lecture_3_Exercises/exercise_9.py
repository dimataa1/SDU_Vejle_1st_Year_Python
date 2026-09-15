"""
Create a function:

def countdown(message, number):
The function should:
Take two parameters: message and number.
Use a for loop and range().
Display the numbers from number down to 1.
After the loop finishes, display the message.
Example:

countdown("Let's start!", 5)
 
Expected output:

5
4
3
2
1
Let's start!
"""

def countdown(message, number):
    for i in range(number, 0, -1):
        print(i)
    print(message)


countdown("Let's start!", 5)