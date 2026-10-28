from app.main import BankAccount

def test_initial_balance():
    account = BankAccount()
    assert account.check_balance() == 1000.0

def test_valid_deposit():
    account = BankAccount()
    success, msg = account.deposit(500.0)
    assert success is True
    assert account.check_balance() == 1500.0

def test_invalid_deposit():
    account = BankAccount()
    success, msg = account.deposit(-100.0)
    assert success is False
    assert account.check_balance() == 1000.0

# New Tests Added for Push 2
def test_valid_withdrawal():
    account = BankAccount()
    success, msg = account.withdraw(400.0)
    assert success is True
    assert account.check_balance() == 600.0

def test_insufficient_withdrawal():
    account = BankAccount()
    success, msg = account.withdraw(1200.0)
    assert success is False
    assert account.check_balance() == 1000.0
