#write a recursive function to calculate the sum of first n natural number
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

num = int(input("Enter a number: "))
print("The sum of first", num, "natural numbers is", calc_sum(num))