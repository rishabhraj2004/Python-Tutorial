student = {
    "name": "Rishabh",
    "age": 20,
    "subjects": {
        "math": 90,
        "science": 85,
        "english": 92
    }
}

print(student.keys()) #to print all keys (name, age, subjects) in student dictionary
#values mai nested dict ke keys bhi print honge kyuki wo first dict ke values hai
print(student.values()) #to print all values (rishabh, 20, maths : 90, science : 85, english : 92) in student dictionary
print(list(student.keys()))  #type casting #to print all keys in student dictionary in the form of list
print(list(student.values())) #type casting #to print all values in student dictionary in the form of list
print(student.items()) #to print all key value pairs in student dictionary as tuples in the form of list
#type casting
print(list(student.keys())) #to print all keys in student dictionary in the form of list
print(list(student.values())) #to print all values in student dictionary in the form of list

# to find total no of keys in student dictionary
print(len(student)) #to print total no of keys in student dictionary
# or another way to find length
print(len(student.keys())) #to print total no of keys in student dictionary



print(student["name"])
print(student.get("name")) #to print value of name key using get method
#difference between [] and get() method to access value of a key in dictionary
# print(student["name2"]) #ye hame error dega
print(student.get("name2")) #ye hame None dega qki name2 key student dict mai nhi hai, but error nhi dega

#AGAR 3 LINE MAI ERROR AYEGA OR USKE BD KE SARE LINE BILKUL SAHI RHEGA PHIR BHI AGEE KA CODE PRINT NHI HOGA.



#to update (here we are adding cities in student dictionary)
print(student.update({"cities": ["munger", "tarapur", "garkha", "chappra"], "ranking": [1100, 1400, 13000, 1324]}))
print(student) #to print updated student dictionary with cities key value pair