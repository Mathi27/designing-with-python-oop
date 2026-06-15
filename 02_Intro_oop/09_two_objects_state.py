# Mini Project
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

# assign
a1 = BankAccount("Mathi", 1000)
a2 = BankAccount("Kumar", 500)

a1.deposit(200)

print(a1.balance)
print(a2.balance)
