# to find factorial by using factorial 
def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", fact(num))



#other method
def fact(n):
    if ( n == 1 or n == 0):
        return 1
    return fact(n-1) * n

num = int(input("enter a number to find factorial: "))
print(fact(num))