collection = {1, 2, 3, 4, "rishu", "akku", 1, 1, 2, 3,} #to create a set with 4 elements, set is a collection of unique elements, it does not allow duplicate values, it is unordered, it is mutable, it is defined by curly braces({}) or by using set() function.
#set duplicate value ko print nhi krata hai, set ke elements ka order fix nhi hota hai, set ke elements ko change krna possible nhi hota hai, but set me new element add krna possible hota hai.
#set kahi bhi kissi ko bhi print kr dega like kabhi 1 agee hoga to kabhi rishu to kabhi akku
print(collection) #to print the set
print(type(collection)) #to print the type of collection >>>> set
collection.add(5) #to add an element in the set
print(collection) #to print the updated set
print(len(collection)) #to print the total no of elements in the set
collection.remove(2) #to remove an element from the set, if the element is not present in the set then it will raise a KeyError
print(collection) #to print the updated set after removing an element



collectin2 = {} # this is not a set, this is a dictionary, to create an empty set we have to use set() function
print(type(collectin2)) #to print the type of collectin2 >>>> dictionary

collection3 = set() #to create an empty set
print(type(collection3)) #to print the type of collection3 >>>> set