class Student:

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def result(self):

        if self.mark >= 50:
            print(self.name, "PASSED")
        else:
            print(self.name, "FAILED")


s1 = Student("Mathi", 85)
s2 = Student("Kumar", 35)

s1.result()
s2.result()