#WAP to check if a list contains a palidrome of elements. .
#palindrome means a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar. E.G:- maam, racecar, [1,2,3,2,1]


list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3, 4, 5]
list3 = []
list3 = input("Enter a list of elements separated by space: ").split() #user se list ke elements input karwana, split() method se space ke basis par list me convert karna

copy_list1 = list1.copy() #list1 ka copy banaya
copy_list1.reverse() #copy_list1 ko reverse kiya

if(list1 == copy_list1): #agar list1 aur copy_list1 same hai to list1 palindrome hai
    print("list1 is a palindrome")
else:
    print("list1 is not a palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()
if(list2 == copy_list2):
    print("list2 is a palindrome")
else:    
    print("list2 is not a palindrome")

copy_list3 = list3.copy()
copy_list3.reverse()
if(list3 == copy_list3):
    print("list3 is a palindrome")
else:
    print("list3 is not a palindrome")