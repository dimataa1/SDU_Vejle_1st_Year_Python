""""
Create a small Python program that works with number sequences. Your program should demonstrate the main programming concepts you have learned in Chapters 1–4.

Part 1 — Repeating Numbers
Create a function:

def show_number(number, times):
The function should:
take number and times as parameters;
use a for loop and range();
print number the specified number of times.
Test:

show_number(5, 3)
show_number(10, 5)
 
Part 2 — Fibonacci Sequence
Create:

def show_fibonacci(n):
The Fibonacci sequence begins:
0, 1, 1, 2, 3, 5, 8, 13, ...
Your function should:
start with first = 0 and second = 1;
use n to determine how many numbers are displayed;
use a for loop with range(n);
calculate each next number;
update first and second correctly.
Test:

show_fibonacci(5)
show_fibonacci(10)
Part 3 — Avoid Repeated Code
Your program needs separator lines in several places:

print("--------------------")
 
Instead of repeating this statement, encapsulate it inside a function.

Then reuse that function when displaying your results.

For example, your output might look like:

--------------------
FIBONACCI SEQUENCE
--------------------
0
1
1
2
3
5
8
13
--------------------
Part 4 — Generalization
Your separator currently always has the same length.

Generalize your function so that the caller can choose:

which character is displayed;
how many times it is displayed.
For example:

--------------------
********************
====================
 
Use parameters rather than fixed values.

Part 5 — Functions Working Together
Create a function that produces a complete Fibonacci report.

The caller should only need to provide how many Fibonacci numbers should be displayed.

Your report should contain:

a separator;
a title;
another separator;
the Fibonacci sequence;
a final separator.
Reuse the functions you have already created. Do not copy their code into the new function.

Part 6 — Documentation
Improve your program by adding:

a docstring to your Fibonacci function;
a docstring to your report function;
at least two useful comments explaining important implementation details.
Remember:

Docstring → explains the function and its interface

Comment → explains something about the implementation

 
Part 7 — Think About Your Design
Answer these questions after your code:

Give one example of encapsulation in your program.
Give one example of generalization.
Which function calls another function?
Give one example of a local variable.
What is the interface of your Fibonacci function?
Give one reasonable precondition for your Fibonacci function.
Give one postcondition.
Where have you avoided repeated code?
"""