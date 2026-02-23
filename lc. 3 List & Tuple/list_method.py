list = [2, 1, 9]
print(list)
list.append(5) #list ke end me 5 add karega
print(list)


list.insert(1, 3) #list ke index 1 par 3 add karega to output hoga [2, 3, 1, 9, 5] 5 rhega qki wo inset se pwhlw appeend kiye hai insert se pehle jo method use krke output milta hai uspe hi insert apply ho jata hai.
#starting mai insert karwana ho to starting mai insrt method use krenge, asually jha isert karwana ho waha insert method use krenge
print(list)


list.remove(1) #list me se 1  jha bhi pehli baar ayega to usko ko remove karega, dusri baar ayaa to usko print kar dega. Qki remove method first occurence ko remove karta hai
print(list)


list.pop() #list ke end me se last element ko remove karega
print(list)


list.pop(1) #list ke index 1 par element ko remove karega
print(list)


list.sort() #list ke elements ko ascending order me sort (arrange) karega
print(list)
print(list.count(2)) #list me 2 kitni baar aata hai usko count karega


list.sort(reverse=True) #list ke elements ko descending order me sort (arrange) karega
print(list)


list.reverse() #list ke elements ko reverse order me sort (arrange) karega
print(list)



# all methods describe above not only work on int it can work on different data type list ( float, string etc)

list2 = ["banana", "litchi", "apple"]
print(list2)
list2.sort() #list ke elements ko ascending order(a/q to first letter) me sort (arrange) karega 
print(list2)

list2.sort(reverse=True) #list ke elements ko descending order (a/q to first letter) me sort (arrange) karega
print(list2)

