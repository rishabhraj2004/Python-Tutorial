
#this is instance method
class Person:
    name = "anonymus"

    def changeName(self, name):
        self.name = name
        #person.name = name 
        # self.__class__.name = "rahul kumar"
        # #agar aisas karte to print(p1.name) print(Person.name) , self.__class__.name = "rahul kumar" to tino ka output rahulkumar hota , lekin yha aisa nhi kiye h to output rahul kumar and anonymus ayega.



p1 = Person()
p1.changeName("Rahul kumar")
print(p1.name)
print(Person.name)



#same work uding class method
class Person:
    name = "anonymus"

    @classmethod
    def changeName(cls, name):
        cls.name =name #ye change directly class attribute mai hoga.

p1 = Person()
p1.changeName("Rahul kumar")
print(p1.name)  #dono ka output same Rahul kumar
print(Person.name) #dono ka output same Rahul kumar


