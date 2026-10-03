"""
Task 3 - Predict the output

def shout(word):
    print(word + '!')

x = shout('hey')

Prediction:
When shout('hey') is called, it prints:
hey!

But shout() has no return statement, so its return value is None.
Therefore x is assigned None (not the string "hey!").

If we then do print(x), it would print: None
"""

def shout(word):
    print(word + '!')

x = shout('hey')
# At this point, "hey!" has already been printed by the function call.

print(x)
# Output: None
# (because shout() never returns a value explicitly)