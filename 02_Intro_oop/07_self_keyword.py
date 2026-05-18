class Mobile:

    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Mobile Brand:", self.brand)


m1 = Mobile("Samsung")

m1.show()