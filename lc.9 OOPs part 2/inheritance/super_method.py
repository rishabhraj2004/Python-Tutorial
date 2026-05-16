class Car:
    def __init__(self, type):
        self.type = type


    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("car started")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type) #super method use krte hai parent class ke method ko call karne ke liye 
        super().start()

car1 = ToyotaCar("Prius", "E.V")
print(car1.type)
print(car1.start())


#aise super method ko use krte kissi parent class ke method ko kissi dusre  class ke andr use kar saktey hai