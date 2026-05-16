print(1 + 2) #3
print(type(1 + 2))
print("rishu" + "patel") #rishupatel (here the work of + is to concatenate two string )
print(type("patel"))
print([1, 2, 3] + [4, 5, 6]) #[1, 2, 3, 4, 5, 6] here + woks as merging two lists.
print(type([1, 2, 3]))

#HERE + OPERATORS act as 3 diferrent form . and that diffrenet works known as polymosphism.

#same thigs for classes as above.

#addition of complex number ((1i + 2j) + (2i + 6j) = (3i + 8j)) here terms of i and j added seperetally
#here we are going to code for addition of complex no.

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

#ye logic lga rhe h do complex number ko add krne ka
    def __add__(self, num2):  #agee piche do bar underscore use jkrne se ye dunder function ban gaya
        newReal= self.real + num2.real
        newImg= self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()


num2 = Complex(11, 32)
num2.showNumber()


# # num3 = num1.add(num2)
# # num3.showNumber #print(num3) ye bhi kar saktey the 
# aise add krenge to ye function call krke karna hua 

#agar hame num + num2 aise likh ke krna hai to pehle dunder function banna padega (agee piche 2 underscore lga ke )

num3 = num1 + num2
num3.showNumber()  #agar dunder function nhi banate to ye hame error deta 



#code for sub of 2 complex number 
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

#ye logic lga rhe h do complex number ko add krne ka
    def __sub__(self, num2):  #agee piche do bar underscore use jkrne se ye dunder function ban gaya
        newReal= self.real - num2.real
        newImg= self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()


num2 = Complex(11, 32)
num2.showNumber()


# # num3 = num1.add(num2)
# # num3.showNumber #print(num3) ye bhi kar saktey the 
# aise add krenge to ye function call krke karna hua 

#agar hame num + num2 aise likh ke krna hai to pehle dunder function banna padega (agee piche 2 underscore lga ke )

num3 = num1 - num2
num3.showNumber()