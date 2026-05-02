# using constructor (__init__)

class Student:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Student("Mathi",24)

print(s1.name)
print(s1.age)
