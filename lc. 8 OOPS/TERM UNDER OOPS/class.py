class Student:
    name = "Rishu"  #this is the method to create class


#this is how object is created for the class
s1 = Student()
print(s1.name)  # Output: Rishu
print(s1) #output: <__main__.Student object at 0x7f8b8c8c8c8c>  
print(s1.__dict__)  # Output: {}

s2 = Student()
print(s2.name)  # Output: Rishu same kyuki hm ek hi name define kiye hai 

# s3 = "rishabh"
# print(s3.name)  # Output: AttributeError: 'str' object has no attribute 'name'  kyuki string me name attribute nhi hota hai



#other e.g let suppose we have a car factory and we want to create a class for car and then create objects for different cars




#or other method
class Car:
    color = "black"
    brand = "mercedes"

car1 = Car()
print(car1.color)  # Output: black
print(car1.brand)  # Output: mercedes



#or other method by using constructor or __init__ function
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
car1 = Car("Toyota", "Camry", 2020)
print(car1.make)  # Output: Toyota
print(car1.model)  # Output: Camry
print(car1.year)  # Output: 2020