def main():
    balance = 1000.0  # Initial account balance

    while True:
        print("\n--- Banking Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"\nYour current balance is: ₹{balance:.2f}")

        elif choice == '2':
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print(f"Successfully deposited ₹{amount:.2f}.")
            else:
                print("Deposit amount must be positive.")

        elif choice == '3':
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount > 0:
                if balance >= amount:  # Balance validation
                    balance -= amount
                    print(f"Successfully withdrew ₹{amount:.2f}.")
                else:
                    print("\nInsufficient balance! Transaction failed.")
            else:
                print("Withdrawal amount must be positive.")

        elif choice == '4':
            print("Thank you for using the banking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

