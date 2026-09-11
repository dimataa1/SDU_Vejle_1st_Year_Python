"""
Vending Machine

Stage 1 — Basic Purchase
Set up three items with prices (e.g., Water: 15 DKK, Soda: 22 DKK,
Snack: 18 DKK). Ask the user to type the name of the item they want
and then ask them to "insert" money by typing a number. Subtract the
price from the money inserted and display the change.

Stage 2 — Insufficient Funds Loop
If the user doesn't insert enough money, do not just cancel the
transaction. Use a loop to tell them how much is still missing and
ask them to insert more coins until the total amount meets or
exceeds the price of the item.

Stage 3 — Coin Dispenser
Instead of just printing the total change, calculate exactly which
coins the machine should return to give the fewest coins possible.
Print how many 20 DKK, 10 DKK, 5 DKK, 2 DKK, and 1 DKK coins are
dispensed.
"""

items = {"Water": 15, "Soda": 22, "Snack": 18}

print("Available items:", ", ".join(items.keys()))
choice = input("Which item would you like? ")

if choice in items:
    price = items[choice]
    total_inserted = 0

    while total_inserted < price:
        missing = price - total_inserted
        amount = float(input(f"Insert more money. You still need {missing} DKK: "))
        if amount <= 0:
            print("Please insert a positive amount.")
            continue
        total_inserted = total_inserted + amount

    change = int(total_inserted - price)
    print("Payment complete! Your change is:", change, "DKK")

    coin_values = [20, 10, 5, 2, 1]
    remaining = change

    print("Dispensing coins:")
    for coin in coin_values:
        count = remaining // coin
        remaining = remaining % coin
        print(f"{coin} DKK coins:", count)
else:
    print("Item not available.")