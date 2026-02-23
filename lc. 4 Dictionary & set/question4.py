#figure out a way to store 9 & 9.0 as seperate values in the set

value = {9, 9.0} #set mai store krne ke bd bhi 9 & 9.0 ko alag alag value ke roop mai store kr diya, kyuki set mai duplicate value store nhi hoti hai, to set mai store krne ke bd hume unique value ki count mil jayegi, to set mai store krne ke bd hume unique value ki count mil jayegi
print(value) #to print the set, it will print only unique values in the set

#qki PYthon mai 9 and 9.0 same value jaisa treate hota hai agar 9 and 9.1, 9.2 etc hota to diff hote but 8, 8.0, 7, 7.0 etc same count honge


#agar hm 9.0 ko as a string store kre to spereatly print ho jayega 

set2 ={9, "9.0"}
print(set2)
#or
set3 = {"9", 9.0} #string hamesha floating value mai return krta hai 
print(set3)

#now we are solving the question
values = {
    ("float", 9.0), ("int", 9) #tuple mai store kr denge
}
print(values)