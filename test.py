import unittest

from gradescope_utils.autograder_utils.decorators import weight
from main import *

class TestJukebox(unittest.TestCase):

    @weight(1)
    def test_checking_account_initialization(self):
        test_checking = CheckingAccount("Mehdi")
        assert test_checking.balance == 0
        assert test_checking.owner == "Mehdi"
    
    @weight(1)
    def test_checking_account_deposit(self):
        test_checking = CheckingAccount("Mehdi")
        assert test_checking.balance == 0
        test_checking.deposit(100)
        assert test_checking.balance == 100

    @weight(1)
    def test_checking_account_withdraw(self):
        test_checking = CheckingAccount("Mehdi")
        assert test_checking.balance == 0
        assert not test_checking.withdraw(50)
        test_checking.deposit(100)
        assert test_checking.balance == 100

        assert test_checking.withdraw(50)
        assert test_checking.balance == 50

    @weight(1)
    def test_checking_account_transfer(self):
        test_checking = CheckingAccount("Mehdi")
        recipient = CheckingAccount("Rec")
        assert test_checking.balance == 0
        assert not test_checking.transfer(50, recipient)
        test_checking.deposit(100)
        assert test_checking.balance == 100
        assert recipient.balance == 0
        
        assert test_checking.transfer(40, recipient)
        assert test_checking.balance == 60
        assert recipient.balance == 40

    @weight(2)
    def test_savings_account_initialization(self):
        test_savings = SavingsAccount("Mehdi", 5)
        assert test_savings.balance == 0
        assert test_savings.owner == "Mehdi"
        assert test_savings.interest_rate == 5
    
    @weight(2)
    def test_savings_account_deposit(self):
        test_savings = SavingsAccount("Mehdi", 5)
        assert test_savings.balance == 0
        test_savings.deposit(100)
        assert test_savings.balance == 100

    @weight(4)
    def test_savings_account_accrue_interest(self):
        test_savings = SavingsAccount("Mehdi", 5)
        assert test_savings.balance == 0
        test_savings.deposit(200)
        test_savings.accrue_interest()
        assert test_savings.balance == 210  

    @weight(4)
    def test_savings_account_withdraw(self):
        test_savings = SavingsAccount("Mehdi", 5)
        assert test_savings.balance == 0
        assert not test_savings.withdraw(50)
        test_savings.deposit(100)
        assert test_savings.balance == 100

        assert test_savings.withdraw(50)
        assert test_savings.balance == 45 # 5 fee

    @weight(3)
    def test_savings_account_transfer(self):
        test_savings = SavingsAccount("Mehdi", 5)
        recipient = CheckingAccount("Rec")
        assert test_savings.balance == 0
        assert not test_savings.transfer(50, recipient)
        test_savings.deposit(100)
        assert test_savings.balance == 100
        assert recipient.balance == 0
        
        assert test_savings.transfer(40, recipient)
        assert test_savings.balance == 55 # 5 fee
        assert recipient.balance == 40

    @weight(2)
    def test_locked_account_initialization(self):
        test_locked = LockedAccount("Mehdi", 5)
        assert test_locked.balance == 0
        assert test_locked.owner == "Mehdi"
        assert test_locked.interest_rate == 5
    
    @weight(2)
    def test_locked_account_deposit(self):
        test_locked = LockedAccount("Mehdi", 5)
        assert test_locked.balance == 0
        test_locked.deposit(100)
        assert test_locked.balance == 100

    @weight(3)
    def test_locked_account_accrue_interest(self):
        test_locked = LockedAccount("Mehdi", 5)
        assert test_locked.balance == 0
        test_locked.deposit(200)
        test_locked.accrue_interest()
        assert test_locked.balance == 210  

    @weight(2)
    def test_locked_account_withdraw(self):
        test_locked = LockedAccount("Mehdi", 5)
        assert test_locked.balance == 0
        assert not test_locked.withdraw(50)
        test_locked.deposit(100)
        assert test_locked.balance == 100

        assert not test_locked.withdraw(50)
        assert test_locked.balance == 100

    @weight(2)
    def test_locked_account_transfer(self):
        test_locked = LockedAccount("Mehdi", 5)
        recipient = CheckingAccount("Rec")

        assert test_locked.balance == 0
        assert not test_locked.transfer(50, recipient)

        test_locked.deposit(100)
        assert test_locked.balance == 100
        assert recipient.balance == 0
        
        assert not test_locked.transfer(40, recipient)
        assert test_locked.balance == 100
        assert recipient.balance == 0


if __name__ == "__main__":
    unittest.main()
