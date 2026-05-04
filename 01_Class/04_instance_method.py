# instance methods.

class Car:
    def __init__(self,brand):
        self.brand = brand
    
    def start(self):
        print(self.brand,"car started")
        
c1 = Car("BMW")

c1.start()