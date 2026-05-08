# create a student class that take name and marks od 3 sub as arguments in constructor.
# then create a method to print the average


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        #we run a loop for geting sum
        sum = 0
        for val in self.marks:
            sum += val
        print("hii", self.name, "your avg score is:", sum/3)




s1 = Student("Akku", [90, 95, 85]) #here we take marks as list
s1.average()


#agar hame s1 ke name ko change karna ho to hm direct bhi change kar sakte hai aise
s1 = Student("Rishu", [80, 85, 90])
s1.average()

# #output = hii Akku your avg score is: 90.0
# hii Rishu your avg score is: 85.0