info = {
    
    "name" : "Rishu",
    "learning": "Python",
    "age": 20,
    "hobbies": ["coding", "gaming", "traveling"],
    "married": False,
    "marks": {"math": 90, "science": 85, "english": 92},

}

print(info)



# we can also store value under dictionary in the form of list and tuple

info2 = {
    "name" : ["Rishu", "Akku", "Arpit"], #store data in the form of string
    "learning": ("Python", "Java", "C++"), #store data in the form of tuple
    "age": 20,
    "hobbies": ["coding", "gaming", "traveling"],
    "married": False,
    "marks": {"math": 90, "science": 85, "english": 92}, #store data in the form of dictionary
}
print(info2)
#value mai list dictonary aur tuple store kar sakte hai, BUT KEYS MAI HUM SIRF STRING, NUMBER YA TUPLE STORE KAR SAKTE HAI, LIST YA DICTIONARY STORE NAHI KAR SAKTE HAI.
#keys are writeen in left side of the dictionary and values are written in right side of the dictionary. Keys and values are separated by colon(:) and each key value pair is separated by comma(,). The whole dictionary is enclosed in curly braces({}).
print(type(info2)) #to print type of info2 >>>> Dictionary
#do keys ka name same nhi ho sakta hai, but values ka name same ho sakta hai.


print(info2["name"]) #to print value of name key
print(info2["learning"]) #to print value of learning key
print(info2["marks"]) #to print value of marks key
print(info2["marks"]["math"]) #to print value of math key in marks dictionary

print(info2["hobbies"][0]) #to print first hobby in hobbies list
print(info2["hobbies"][1]) #to print second hobby in hobbies list

# print(info2[surname]) ye print nhi hoga error milega qki ye define nhi h hamare dict mai

info2["name"] = "Rishabh" #to change value of name key, mtlb ke sare purane value jo name ke andr hai usko remove krke bas ye jo add kiye hai (rishabh) bas wahi rhega purana sara value remove ho jayega
print(info2["name"]) #to print updated value of name key

info2["surname"] = "Patel" #to add new key value pair in dictionary
print(info2) #to print updated dictionary

null_dict = {} #to create an empty dictionary
print(null_dict) #to print empty dictionary