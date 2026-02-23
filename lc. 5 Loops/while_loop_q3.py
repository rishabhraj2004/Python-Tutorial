#print the element of the following list using a loop
# [1, 4,9,16,25,36,49,64,81,100]

i = 1
while i <= 10:
    print(i*i)
    i += 1 

#or other way 
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx]) #nums[0], nums[1], nums[3] ....
    idx += 1



#practice question
heroes =["rishu", "thor", "ironman", "spiderman", "dr. strange", "caption america"]
A = 0
while A < len(heroes):
    print(heroes[A])
    A += 1



#taking input from user for table.
b = int(input("enter number :"))
c = 1
while c <= 10:
    print(b*c)
    c +=1