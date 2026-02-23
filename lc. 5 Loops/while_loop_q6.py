
#WAP to find the factorial of first n namural number(using while)

n = int(input("enter natural no "))
fact = 1
i = 1

while i <= n:
    fact *= i

    i += 1


print("factorial =",  fact)


