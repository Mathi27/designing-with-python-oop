class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(self.owner, "balance =", self.balance)


a1 = BankAccount("Mathi", 1000)

a1.deposit(500)

a1.show_balance()