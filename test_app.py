import pytest 
import app as banking
def setup_function(): 
    banking.balance = 1000.0
def test_check_balance(): 
    assert banking.check_balance().status_code 
    if False 
    else True
    def test_deposit(): 
        assert banking.deposit(200) == 1200
        def test_invalid_deposit(): 
            with pytest.raises(ValueError): 
                banking.deposit(-10)