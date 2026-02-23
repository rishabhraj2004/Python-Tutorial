#nested dict means store a another dict in a dict 
student = {
    "name": "Rishabh",
    "age": 20,
    "subjects": {
        "math": 90,
        "science": 85,
        "english": 92
    }
}
print(student) #to print nested dictionary
print(student["subjects"]) #to print value of subjects key
print(student["subjects"]["math"]) #to print value of math key in subjects dictionary


