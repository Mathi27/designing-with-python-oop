# Default Values in Constructor

class Employee:

    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary


e1 = Employee("Mathi")
e2 = Employee("Kumar", 50000)

print(e1.name, e1.salary)
print(e2.name, e2.salary)