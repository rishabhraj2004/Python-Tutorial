veggies =[ "potato", "bringal", "ladyfinger", "cucumber"]

for val in veggies:
    print(val) #for loop use in list
print(type(veggies))


#for loop use in tuple
num = (1, 2, 3, 4, 5) #tuple written in prenthesis

for val in num:
    print(val)

print(type(num))

#for loop in string
name = "rishu  patel"
for char in name:
    print(char)
print(type(name))

#use of else
name = "rishu  patel"
for char in name:
    if(char == "e"):
        print("e found")
        break
    print(char) #yha loop pura nhi hua isleye else work nhi hua pura hota to else wala statement print hota
else:
    print("END")

