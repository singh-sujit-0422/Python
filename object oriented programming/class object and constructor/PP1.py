# 1. Bank Account Simulation
# Problem:
# Create a class BankAccount with attributes: account_number, account_holder, and balance. Add methods to deposit(amount) and withdraw(amount) and show updated balance after each operation.

# Challenge: Prevent withdrawal if balance is insufficient.


class BankAccount:
    bank = 'Axis Bank'

    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0


    def updated_balance(self):
        print('Your account balance is : ', self.balance)


    def deposit_amount(self, amount):
        if amount <= 0:
            print('Invalid amount. Please check the amount and try again.')
        else:
            print('Transaction successful.')
            self.balance = self.balance + amount
            self.updated_balance()

    
    def withdraw_amount(self, amount):

        if amount > self.balance:
            print(f'You do not have {amount} in your bank account. Your current balance is {self.balance}. Please try again')
        
        else:
            print('Transaction successful.')
            self.balance = self.balance - amount
            self.updated_balance()


shruti = BankAccount('102030405060', 'shruti hasan')

print(shruti.balance) # 0

shruti.updated_balance() # Your account balance is :  0

shruti.deposit_amount(0) # Invalid amount. Please check the amount and try again.

shruti.deposit_amount(-23) # Invalid amount. Please check the amount and try again.

shruti.deposit_amount(100000)
# Transaction successful.
# Your account balance is :  100000


shruti.withdraw_amount(10000000)
# You do not have 10000000 in your bank account. Your current balance is 100000. Please try again


shruti.withdraw_amount(10000)
# Transaction successful.
# Your account balance is :  90000








