# Create account class with 2 attributes - balance and account number 
# Create methods for credit and debit & printing balance

class Account:
    def __init__(self, acc_number, balance):
        self.acc_number = acc_number
        self.balance = balance
        print("YOur account has been created ! Your account number is", self.acc_number,"and the balance is ", balance )
    def credit(self, amount):
        print("You are adding into your account", self.acc_number,"for amount", amount, "and the balance is ", self.balance+amount )
        self.balance += amount
    def debit(self, amount):
        print("You are withdrawing from your account", self.acc_number,"for amount", amount, "and the balance is ", self.balance-amount )
        self.balance += amount

a1 = Account(123,200)
a1.credit(200)
a1.debit(300)
