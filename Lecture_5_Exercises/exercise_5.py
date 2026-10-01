"""
Task 5 - Analyze the recursive function mystery(n)

def mystery(n):
    if n == 0:
        print("go!")
    else:
        mystery(n - 1)
        print(n)
mystery(3)

How does it differ from the recursive functions seen in the lecture?

In the lecture's typical recursive functions, the work (e.g. printing,
calculating) usually happens BEFORE the recursive call, or the result
of the recursive call is directly used/returned. Here, the recursive
call happens FIRST, and the print(n) statement happens AFTER the
recursive call returns. This means the prints happen in REVERSE order
as the recursion "unwinds" (this is sometimes called a post-order
or "unwinding" pattern) - the function doesn't use the return value
of the call at all; it just triggers print statements during the
unwinding phase.

How many frames exist at the moment "go!" prints?

Call chain:
mystery(3) -> mystery(2) -> mystery(1) -> mystery(0)

At the moment mystery(0) executes print("go!"), all of the calls
above it are still on the call stack, waiting for their recursive
call to return (none of them have reached their print(n) line yet).
So there are 4 frames on the stack at that moment:
mystery(3), mystery(2), mystery(1), mystery(0).
"""

def mystery(n):
    if n == 0:
        print("go!")
    else:
        mystery(n - 1)
        print(n)

mystery(3)

# Actual output order: go!  1  2  3
# This confirms the prints happen during the unwinding phase,
# in reverse order of the original calls.