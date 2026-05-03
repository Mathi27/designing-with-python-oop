# Creating multiple objects.

class Emp:
    def __init__(self,name,role):
        self.name = name 
        self.role = role 

emp1 = Emp("Mathi","Backend Engineer")
emp2 = Emp("Yuvarajan","MLOps Engineer")

print(emp1.name)
print(emp2.name)

print(emp1.role)
print(emp2.role)



