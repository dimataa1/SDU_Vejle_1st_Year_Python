"""
Make a Mini Banking System

Stage 1 — Basic Account
Create an account with a starting balance of 1,000 DKK. Allow
deposits and withdrawals and display the updated balance.

Stage 2 — Valid Transactions
Reject withdrawals when there is insufficient money and reject zero
or negative transactions.

Stage 3 — Interactive Bank
Create a menu that repeatedly allows the user to:
1. Check balance
2. Deposit money
3. Withdraw money
4. Exit
Handle invalid choices without crashing.
"""

balance = 1000

while True:
    print("\n----- BANK MENU -----")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("Current balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Deposit must be a positive amount.")
        else:
            balance = balance + amount
            print("Deposit successful. New balance:", balance)

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Withdrawal must be a positive amount.")
        elif amount > balance:
            print("Insufficient funds. Current balance:", balance)
        else:
            balance = balance - amount
            print("Withdrawal successful. New balance:", balance)

    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")