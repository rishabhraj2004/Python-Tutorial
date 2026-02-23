i = 1
while i<=5:
    print(i)
    if(i==3):
        break  #jab condition satisfy ho jayega to loop agee wexecute nhi hoga yha pe i =3 hote hi loop terminate ho jayega or output 1 2 3 dega
    i +=1


i = 1
while i<=10:
   if(i==3):
        i +=1
        continue # sirf current iteration ko skip krega banki agee ka execute krega yha pe output hoga 1 2 4 5 6 7 8 9 10 sirf 3 skip hoga
   print(i)
   i += 1

#to print only odd no from 1 to 100
i = 1
while i<=100:
   if(i%2 == 0):
        i +=1
        continue
   print(i)
   i += 1

#to print even no in b/w 1 to 100
i = 1
while i<=100:
   if(i%2 != 0):
        i +=1
        continue
   print(i)
   i += 1

#or orther method
i = 1
while i<=100:
   if(i%2 == 1):
        i +=1
        continue
   print(i)
   i += 1

