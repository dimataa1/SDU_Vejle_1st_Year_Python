"""
Task 1 - Coin change using integer division and modulus

You have 87 cents. Calculate how many quarters (25), dimes (10),
nickels (5), and pennies (1) you can split the cents into,
in descending order, using // and %.
"""

cents = 87

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents // 1

print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)

# 87 -> 3 quarters (75), 1 dime (10), 0 nickels, 2 pennies -> 75+10+0+2 = 87