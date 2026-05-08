# class variables

class Student:
    
    school = "School of Innovation"
    
    def __init__(self,name):
        self.name = name

s1 = Student("Mathi")
s2 = Student("Sriram")

print(s1.name,"-",s1.school)
print(s2.name,"-",s2.school)
