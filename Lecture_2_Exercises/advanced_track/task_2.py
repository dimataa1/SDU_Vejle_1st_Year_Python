"""
Create a Password Strength Checker

Stage 1 — Basic Password Check
Ask the user to enter a password and check whether it has at least
8 characters. Display whether the password meets the requirement.

Stage 2 — Strong Password Rules
A strong password must contain:
* at least 8 characters;
* at least one uppercase letter;
* at least one lowercase letter;
* at least one number.
Instead of simply saying weak, tell the user which requirements are
missing.

Stage 3 — Password Strength Rating
Give the password a strength rating based on how many requirements
it satisfies:
For example, for password: Hello123
Length:      ✓
Uppercase:   ✓
Lowercase:   ✓
Number:      ✓
Strength: STRONG
Add another requirement of your own, such as checking for a special
character.
"""

password = input("Enter a password: ")

has_length = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)

special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/"
has_special = any(char in special_characters for char in password)

checks_passed = sum([has_length, has_upper, has_lower, has_number, has_special])

print("Length:      ", "✓" if has_length else "✗")
print("Uppercase:   ", "✓" if has_upper else "✗")
print("Lowercase:   ", "✓" if has_lower else "✗")
print("Number:      ", "✓" if has_number else "✗")
print("Special char:", "✓" if has_special else "✗")

if checks_passed == 5:
    strength = "STRONG"
elif checks_passed >= 3:
    strength = "MEDIUM"
else:
    strength = "WEAK"

print("Strength:", strength)