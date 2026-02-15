str = "Rishabh Rawat"
str1 = str[0:7] #slicing of string from index 0 to 6
print(str1) #prints the sliced string
str2 = str[:8] #slicing of string from index 0 to 7
print(str2) #prints the sliced string
str3 = str[0: ] #slicing of string from index 0 to end of the string
print(str3) #prints the sliced string
str4 = str[1:4]
print(str4)
str5 = str[2:10:2] #slicing of string from index 2 to 9 with step 2 or escaping next element 
print(str5) #prints the sliced string with step 2
str6 = str[::3] #slicing of string from index 0 to end of the string with step 3 or escaping next 2 element
print(str6) #prints the sliced string with step 3
str7 = str[1:10:3] #slicing of string from index 1 to 9 with step 3 or escaping next 2 element escaping depends on 3 means last element writeen in the str []box
print(str7) #prints the sliced string with step 3
str8 = str[1:]
print(str8) #slicing of string from index 1 to end of the string


print(str[2:10:3])#slicing of string from index 2 to 9 with step 3 or escaping depends on 3 means last element writeen in the str []box


print(str[1:10:3])#slicing of string from index 1 to 9 with step 3 or escaping depends on 3 means last element writeen in the str []box








#negative index
str = "apple"
print(str[-3:-1]) #slicing of string from index -3 to -2
print(str[-4:-1]) #slicing of string from index -4 to -2
print(str[-5:-1]) #slicing of string from index -5 to -2
print(str[-5:-1:2]) #slicing of string from index -5 to -2 with step 2 or escaping next element