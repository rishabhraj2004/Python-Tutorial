#WAP to find gratest of 3 numbers
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if(a >= b and a >= c):
    print("a is greatest")
elif(b >= c):
    print("b is greatest")
else:
    print("c is greatest")