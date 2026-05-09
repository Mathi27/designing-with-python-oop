# objects interacting with each other:

class Student:
    def __init__(self,name):
        self.name = name
    
    def introduce(self):
        print("Hi, I am", self.name)
    
class Classroom:
    def __init__(self,student):
        self.student = student
    
    def start_class(self):
        self.student.introduce()
        print("Class Started")

s1 = Student("Mathi")

room = Classroom(s1)

room.start_class()
        