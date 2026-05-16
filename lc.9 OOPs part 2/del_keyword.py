class Student :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    


s1 = Student("Rishu", 20)
print(s1.name)  # Output: Rishu
print(s1.age)   # Output: 20

del s1.age
del s1.name
print(s1.name)  # Output: Rishu
# print(s1.age)   # This will raise an AttributeError since 'age' has been deleted