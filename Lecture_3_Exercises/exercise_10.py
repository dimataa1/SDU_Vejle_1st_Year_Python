"""
Create a function:
def show_message(message, times):

The function should:
1. Take two parameters:
   - message - the text to display
   - times - the number of times the message should be displayed
2. Use a for loop to repeat the code.
3. Use range() to control how many times the loop runs.
4. Use the loop variable to number each message.
5. Display the numbers starting from 1, not 0.
6. Display the message next to each number.

Call your function with:
show_message("Practice Python", 4)

Expected output:
1 Practice Python
2 Practice Python
3 Practice Python
4 Practice Python

Remember: range() starts counting from 0 by default. Think about how
you can make the displayed number start from 1.
"""

def show_message(message, times):
    for i in range(1, times + 1):   # start at 1 instead of 0
        print(i, message)


show_message("Practice Python", 4)