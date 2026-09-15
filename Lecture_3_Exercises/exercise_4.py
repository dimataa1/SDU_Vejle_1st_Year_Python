"""
Create:

def password_info(password):
 
The function should:

Use a Python built-in function to find the number of characters in the password.
Store the result in a local variable.
Return the result.
Test:

password_length = password_info("CyberSafe2026")
print("Password length:", password_length)
"""

def password_info(password):
    length = len(password)
    return length


password_length = password_info("CyberSafe2026")
print("Password length:", password_length)