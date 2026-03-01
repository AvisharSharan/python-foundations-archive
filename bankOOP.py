class Bank:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

acct1 = Bank("Alex", 100)
acct1.deposit(50)
acct1.withdraw(30)
print(acct1.balance)