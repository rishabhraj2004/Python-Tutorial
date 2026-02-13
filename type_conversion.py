a = 2 
b = 4.25

sum = a + b # here we are adding an integer and a float and the result will be a float because of type conversion 
print(sum) # prints the result of the addition (2.0 + 4.25) which is 6.25  


# casting (type conversion)
c = "5"
d = 10
# print ( c+ d) this will give an error because we cannot add a string and an integer together without converting the string to an integer first
print (int(c) + d) # here we are converting the string "5" to an integer using the int() function and then adding it to the integer 10, which will give us the result 15

r = 3.14
r = str(a) # here we are converting the integer 2 to a string using the str() function and storing it back in variable r
print(type(r)) # this will print <class 'str'> because r is now a string after the conversion