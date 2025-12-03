# Create Account class with 2 attributes - balance and account no. create methodes for debit,credit and printing the balance.

class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    
    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("bdt.", amount, "was debited")
        print("Total balance is =", self.get_balande())
        
    def credit(self, amount):
        self.balance += amount
        print("bdt.", amount, "was crebited")
        print("Total balance is =", self.get_balande())
    
    def get_balande(self):
        return self.balance
    
    
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(25000)
acc1.debit(3500)
        