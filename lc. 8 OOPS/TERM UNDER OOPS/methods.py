class Student:
    def __init__(self, name, ):
        self.name = name

    def welcome(self):
        return f"Welcome {self.name}!" #the diffrence between return and print is that return gives the output to the caller while print gives the output to the console. In this case, we want to return the welcome message so that it can be used elsewhere in the code if needed.
student1 = Student("Alice")
print(student1.welcome())  # Output: Welcome Alice!


#or ther method
class Students:
    collegename= "GEC JAMUI"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks


s1 = Students("Akku", 99)
s1.welcome()
print(s1.get_marks())

#here we use welcome and get_marks as methods of the class Students. The welcome method prints a welcome message with the student's name, while the get_marks method returns the marks of the student. 