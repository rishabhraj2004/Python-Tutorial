class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #this is a private method and we can't access it outside the class

    def reset_password(self):
        print(self.__acc_pass) # you can access the private attribute within the class using self.__acc_pass to yha pe ye chal jayega.
    #yha pass aa jayega qki ye cass ke andar hai to ye private attribute ko access kar sakta hai.


a1 = Account(12345, "pass123")
print(a1.acc_no)    # Output: 12345
# print(a1.__acc_pass)  # This will raise an AttributeError since __acc_pass is private
#yha pe acc pass nhi ayega qki ye class ke bhr hai.
print(a1.reset_password())  # Output: pass123





#other example
class Person:
    __name = "Rishu" # this is a private attribute

    def __hello(self):
        print("Hello, I am a Rishu.") # this is a private method

    def welcome(self):
        self.__hello() # you can access the private method within the class using self.__hello to yha pe ye chal jayega.
    #yha pe welcome ko public krke usmai hello jo private hai uskopublic welcome method ke andr dalke public bna diye hello ko. to welcome ke help se hm hello ko class ke bhr bhi access kr saktey hai, but directly hello ko class ke bhr access nhi kar saktey hai.

p1 = Person()
# print(p1.__name)  # This will raise an AttributeError since __name is private
# print(p1.__hello())  # This will raise an AttributeError since __hello is
print(p1.welcome())  # Output: Hello, I am a person.