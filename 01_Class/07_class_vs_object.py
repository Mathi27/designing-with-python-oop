# class is blueprint, object is real instance

class Mobile :
    
    def __init__(self,model):
        self.model = model
        
    def call(self):
        print(self.model,"calling...")

m1 = Mobile("iPhone")
m2 = Mobile("Samsung")

m1.call()
m2.call()