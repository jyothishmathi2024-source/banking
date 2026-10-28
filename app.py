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

def run_menu():
    account = BankAccount()
    print("--- Welcome to the Banking App (v1.0 - Deposit Only) ---")
    
    # We use a limited loop or simulation for non-interactive runner safety if needed,
    # but a simple standard CLI flow works natively inside docker run -it.
    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Exit")
        choice = input("Enter choice (1-3): ")
        
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
            print("Goodbye!")
            break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    run_menu()
