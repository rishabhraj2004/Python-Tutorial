class Student:
   def __init__(self,fullname, age, grade, semester):
        self.fullname = fullname
        self.age = age
        self.grade = grade
        self.semester = semester
        
        # print("adding new student in databse")
        # print(self)  # Output: <__main__.Student object at 0x7f8b8c8c8c8c(this is address of objecte where it is stored)>


s1 = Student("Rishabh", 20, "A", 2)  
s2 = Student("Rishu", 19, "B", 1)
print(s1.fullname)  # Output: Rishabh
print(s1.age)  # Output: 20
print(s1.grade)  # Output: A
print(s1.semester)  # Output: 2

print(s2.fullname)  # Output: Rishu
print(s2.age)  # Output: 19
print(s2.grade)  # Output: B
print(s2.semester)  # Output: 1

# if we want output in single line
print(f"{s1.fullname} is {s1.age} years old, has grade {s1.grade} and is in semester {s1.semester}.")
print(f"{s2.fullname} is {s2.age} years old, has grade {s2.grade} and is in semester {s2.semester}.")
#yha pe f string ka use kiya hai jisse hm easily variables ko string me embed kar sakte hai without using + operator for concatenation.

#method teach by sardha khapra
print(s1.fullname, "is", s1.age, "years old, has grade", s1.grade, "and is in semester", s1.semester)

#or other emthod by using __str__ method
# class Student:
#    def __init__(self,fullname, age, grade, semester):
#         self.fullname = fullname
#         self.age = age
#         self.grade = grade
#         self.semester = semester
        
#    def __str__(self):
#         return f"{self.fullname} is {self.age} years old, has grade {self.grade} and is in semester {self.semester}."
# s1 = Student("Rishabh", 20, "A", 2)
# s2 = Student("Rishu", 19, "B", 1)
# print(s1)  # Output: Rishabh is 20 years old, has grade A and is in semester 2.
# print(s2)  # Output: Rishu is 19 years old, has grade B and is in semester 1.




class Phone:
    #default constructor
    def __init__(self):
        pass

    #parameterized constructor
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

phone1 = Phone("Apple", "iPhone 12", 9999)
print(phone1.brand, phone1.model,"and its price is", phone1.price)  # Output: Apple iPhone 12 and its price is 9999