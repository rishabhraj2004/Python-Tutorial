# search for a number x in this given tuple using  loop
#     (1,4,9,16,25,36,49,64,81,100)

nums =  (1, 4 ,9 , 16, 25, 36, 49, 64, 81, 100, 36) #this is a tuple
a = int(input("enter no to find :"))

i = 0
while i < len(nums):
    if(nums[i] == a):
     print("Found at idx", i)
     break #break use nhi karte to at indx5 ke bd bhi finding findi show krta and indx at 10 show karta 
    else:
       print("finding..")
    i += 1
