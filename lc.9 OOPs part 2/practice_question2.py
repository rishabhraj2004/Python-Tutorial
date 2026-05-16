# define a employee classs with attribute role, depeartent & salary. this classalso have a showdetail() method. 

# create an enginner class that inherits propetis from employee and has additional attribute : name & age.


class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self. dept = dept
        self.salary = salary
        

    def showdetail(self):
        print("role=", self.role )
        print("salary=", self.salary )
        print("dept=", self.dept )



#  to create an enginner class that inherits propetis from employee and has additional attribute : name & age.
class Enginner(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("enginner", "IT", "10,00,000")


engg1 = Enginner("Rishabh Patel", 25 )
engg1.showdetail()


