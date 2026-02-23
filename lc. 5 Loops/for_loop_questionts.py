#print the element of the following list using a for loop
# [1, 4,9,16,25,36,49,64,81,100]

num =[1, 4,9,16,25,36,49,64,81,100]
for el in num:
    print(el)

# search for a number x in this given tuple using for loop
#     (1,4,9,16,25,36,49,64,81,100)


num =(1, 4,9,16,25,36,49,64,81,100,49)

x = 49
idx = 0
for el in num:
    if(el == x):
        print("number found at idx:", idx)
    idx += 1


num =(1, 4,9,16,25,36,49,64,81,100,49)

x = 49
idx = 0
for el in num:
    if(el == x):
        print("number found at idx:", idx)
        break #ek baar aa gaya hai to dusre baar wale pe print nhi krega 
    idx += 1


#WAP to find the factorial of first n namural number(using for)

n = int(input("enter natural no "))
fact = 1
i = 1
for i in range(1, n+1):
    fact *= i



print("factorial =",  fact)
