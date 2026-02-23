#wap to find the sum of first n  natural nubers (using while)
n = int(input("enter natural no "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1


print("total sum =", sum)
