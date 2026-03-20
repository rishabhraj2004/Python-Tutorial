import re


a = 5
b = 10 
sum = a + b
print(sum)


#more line of code
a = 2
b = 3
sum = a + b
print(sum)


#here we asre writing code in reduntant form(repateing code) so we can use function to avoid this reduntant code thats why we use function
def add(a, b):
    sum = a + b
    print(sum)

add(90, 10)
add(298, 3)


#function definition a&b is parameters and 90,10 is arguments calc_sum is function name(call)
def cal_sum(a, b):
    return a + b
sum = cal_sum(90, 10)
print(sum)


def print_hello(name):
    print("Hello " + name)

print_hello("Alice")
print_hello("Bob")


#average of 3 no
def calc_avg(a, b, c):
    avg = (a + b + c) / 3
    return avg
average = calc_avg(10, 20, 30)
print(average)