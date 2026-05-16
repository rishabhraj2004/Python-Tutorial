# eg of single inheritance in python
class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Innova")

#yha pe hm ek dusre class se inherit krke ek naya class banaye hai jiska naam ToyotaCar hai, aur usme Car class ke sare attributes and methods aa gaye hai, to ab hm ToyotaCar ke object se Car class ke methods ko call kr saktey hai. to yha pe car1 aur car2 dono ToyotaCar ke object hai, lekin unme Car class ke methods bhi available hai, to hm unko call krke Car class ke methods ko use kr saktey hai.
print(car1.start())  # Output: Car started
print(car2.stop())   # Output: Car stopped
print(car1.color)   # Output: Black
