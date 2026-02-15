age = int(input("enter the age of the person:"))
if (age >= 18):
    print("can vote & apply for driving license")
    if (age >= 21):
        print("can also apply for a passport")
        if (age >= 80):
            print("can also apply for senior citizen card")
elif (age >= 16):
    print("can apply for driving license")
else:
    print("cannot vote or apply for driving license")




#another question
age = int(input("enter the age of the person:"))
if (age >= 18):
    if (age >= 80):
        print("cannot drive")
    else:
        print("can drive")

else:
    print("cannot drive")