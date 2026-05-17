class Dog:

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "is barking")


d1 = Dog("Rocky")

d1.bark()