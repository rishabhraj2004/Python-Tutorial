#WAF to take input from user and classified the enter number as neven or odd
def classify_number(num):
    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")

num = int(input("Enter a number: "))
classify_number(num)