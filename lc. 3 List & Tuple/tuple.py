num = (2, 1, 3, 1)
print(type(num)) #num ke type ko print karega
print(num[0]) #num ke first element ko access karne ke liye hum index 0 ka use karte hai
print(num[1]) #num ke second element ko access karne ke liye hum index 1 ka use karte hai
print(num[2]) #num ke third element ko access karne ke liye hum index 2 ka use karte hai
print(num[3]) #num ke fourth element ko access karne ke liye hum index 3 ka use karte hai
# num[0] = 5 #tuple ke first element ko change karne ke liye hum index 0 ka use karte hai lekin tuple immutable(nor changable) hoti hai isliye hame error milega
print(num)


num2 =() #empty tuple banane ke liye hum empty parenthesis ka use karte hai
print(type(num2)) #num2 ke  data type ko print karega
print(num2)

num3 =(5,) #single element tuple banane ke liye hum element ke baad comma ka use karte hai, agar comma nahi use karenge to wo int type ka variable ban jayega
print(type(num3)) #num3 ke  data type ko print karega
print(num3) 