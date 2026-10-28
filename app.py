class BankAccount:
    def __init__(self, initial_balance=1000.0):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True, f"Successfully deposited ₹{amount:.2f}."
        return False, "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be positive."
        if amount > self.balance:
            return False, "Insufficient balance! Transaction failed."
        self.balance -= amount
        return True, f"Successfully withdrew ₹{amount:.2f}."

def run_menu():
    account = BankAccount()
    print("--- Welcome to the Banking App (v2.0 - Full Features) ---")
    
    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            print(f"Current Balance: ₹{account.check_balance():.2f}")
        elif choice == '2':
            try:
                amt = float(input("Enter deposit amount: ₹"))
                success, msg = account.deposit(amt)
                print(msg)
            except ValueError:
                print("Invalid numeric amount.")
        elif choice == '3':
            try:
                amt = float(input("Enter withdrawal amount: ₹"))
                success, msg = account.withdraw(amt)
                print(msg)
            except ValueError:
                print("Invalid numeric amount.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    run_menu()
