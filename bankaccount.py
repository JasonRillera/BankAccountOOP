class BankAccount:
    def __init__(self, rate=.01, balance=0):
        self.int_rate = rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        amount_after_withdraw = self.balance - amount
        if amount_after_withdraw < 0:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            interest_yielded = self.balance * self.int_rate
            self.balance += interest_yielded
        return self

jason = BankAccount()
agnes = BankAccount()

jason.deposit(10).deposit(10).deposit(10).withdraw(5).yield_interest().display_account_info()
agnes.deposit(20).deposit(20).withdraw(5).withdraw(5).withdraw(5).withdraw(5).yield_interest().display_account_info()