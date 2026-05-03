age = int(input("enter your age:"))
if age >=18:
    print("can vote & apply for driving license")

elif age >= 16:
    print("can apply for driving license")
else:
    print("cannot vote or apply for driving license")



num = 6
if(num>3):
    print("greater than 3")
if(num>5):
    print("greater than 5")
#if do baar likhenge to dono baar condition check hogi, or do output dega
elif(num>4): #elif ka matlab else if, agar pehla condition false hua to dusra check karega, agar pehla true hua to dusra check nahi karega
    print("greater than 4")



#uses of if, elif & else 

light = input("enter the traffic light color:")
if light == "red":
    print("stop")
elif light == "green":
    print("go")
elif light == "yellow":
    print("get ready")
else:
    print("invalid input")



#else elif else ke bd print likhne ke liye jo ek tab or 4 space dete hain, usse indentation kehte hain, python me indentation ka bahut importance hai, agar indentation sahi nahi hoga to code error dega, isliye hamesha indentation ka dhyan rakhen.
