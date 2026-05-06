# understanding self keyword

class Laptop:
    
    def __init__(self,brand,ram):
        self.brand = brand
        self.ram = ram
    
    def details(self):
        print("Brand: ",self.brand)
        print("RAM: ",self.ram)
l1 = Laptop("Macbook Pro","1TB")

l1.details()