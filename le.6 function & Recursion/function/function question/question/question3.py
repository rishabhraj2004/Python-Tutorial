#WAF to find the factorial of number n
#simple logic using for loop 
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

#by using function
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

n = int(input("Enter a number: "))
print(factorial(n))