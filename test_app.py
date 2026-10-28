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
