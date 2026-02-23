# DIfference between strings & list in python.


info = ["Ram", 4, 95.65, "munger"]
print(info)
info[0] = "Shyam" #list ke first element ko change karne ke liye hum index 0 ka use karte hai lekin string immutable(nor changable) hoti hai isliye hame error milega
print(info)


str = "hello"
print(str[0]) #string ke first character ko access karne ke liye hum index 0 ka use karte hai
# str[0] = "H" #string ke character ko change karne ke liye hum index ka use karte hai lekin string immutable(nor changable) hoti hai isliye hame error milega