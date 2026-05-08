class Students:
    college_name = "ABC College" #class attribute and its is coomon for whole class

    def __init__(self, name, age):
        self.name = name  #instance attribute and its is unique for each object
        self.age = age

s1 = Students("Rishabh", 20)
s2 = Students("Rishu", 19)
print(s1.name, s1.age, s1.college_name)  # Output: Rishabh 20 ABC College
print(s2.name, s2.age, s2.college_name)  # Output: Rishu 19 ABC College

#agar itnsa nhi likhna hai to direct bhi likh saktey hai aise jisse sirf college name ayega 
print(Students.college_name)  # Output: ABC College