commitee = set()
# commitee.add("rishu") #to add an element in the set
commitee.add("rishu")
commitee.add("akku")
commitee.add("arpit")
commitee.add(1)
commitee.add((9, 8, 7, 6)) #we can also add tuple in the set because tuple is immutable, but we cannot add list or dictionary in the set because they are mutable(changeable)

#TUPLE MAI JO VALUE EK BAAR ASSIGN KAR DIYE WO CHANGE NHI KAR SAKTEY ISLIYE YE  IMMUTABLE HOTE HAI, BUT LIST YA DICTIONARY MAI JO VALUE ASSIGN KAR DIYE WO CHANGE KAR SAKTEY HAI ISLIYE YE MUTABLE HOTE HAI.


commitee.add("rishu") #to add duplicate element in the set, but it will not be added in the set because set does not allow duplicate values
print(commitee) #to print the set, it will print only unique elements in the set

# to check if an element is present in the set or not
print("rishu" in commitee) #to check if rishu is present in commitee set or not, it will return True
print("tarun" in commitee) #to check if tarun is present in comm

#to remove an element from the set
commitee.remove("akku") #to remove akku from commitee set, if the element
# if element is not present in the set then it will raise a KeyError
print(commitee) #to print the updated set after removing an element

print(len(commitee)) #to print the total no of elements in the set

#to remove random element from the set
commitee.pop() #to remove random element from the set, it will remove and return a random element from the set, but we cannot specify which element to remove because set is unordered
print(commitee) #to print the updated set after removing a random element

print(commitee.pop()) #to remove and return a random element from the set, it will remove and return a random element from the set, but we cannot specify which element to remove because set is unordered

#to empety all the values under the set
commitee.clear() #to empty all the values under the set, it will remove all the elements from the set, but it will not delete the set itself(means bd mai add kr sakte hai elements ), we can still use the set after clearing it
print(commitee) #to print the empty set after clearing it


