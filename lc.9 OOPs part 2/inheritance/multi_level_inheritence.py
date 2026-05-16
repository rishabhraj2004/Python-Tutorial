#eg of multi level inheritance
class Car:
    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("car started")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()


#yha pe hm car class se toyota class mai inheritence kiye phir toyota class se fortuner class mai inheritence kiye.
