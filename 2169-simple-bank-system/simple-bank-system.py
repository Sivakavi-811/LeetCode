class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.n = len(balance)

    def valid(self, account):
        return 1 <= account <= self.n

    def transfer(self, account1, account2, money):

        if not (self.valid(account1) and self.valid(account2)):
            return False

        if self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True

        return False

    def deposit(self, account, money):

        if self.valid(account):
            self.balance[account - 1] += money
            return True

        return False

    def withdraw(self, account, money):

        if not self.valid(account):
            return False

        if self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True

        return False