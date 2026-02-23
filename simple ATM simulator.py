# Question 10 - simple ATM simulator

# balance
balance = 10000  

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Your balance is:", balance)
    elif choice == '2':
        amt = float(input("Enter deposit amount: "))
        balance = balance + amt
        print("Deposit successful! New balance is:", balance)
    elif choice == '3':
        amt = float(input("Enter withdrawal amount: "))
        if amt > balance - 500:
            print("Cannot withdraw! Minimum balance of 500 must remain.")
        else:
            balance = balance - amt
            print("Withdrawal successful! New balance is:", balance)
    elif choice == '4':
        break