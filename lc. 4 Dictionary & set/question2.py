# we are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classroom are needed by all students
    
# sub:- python, java, c++, python, javascript, c, c++, java, python,java

subjects = ["python", "java", "c++", "python", "javascript", "c", "c++", "java", "python", "java"] #set mai store kr diye subjects ko, but hume unique subject ki count chahiye, to hum set ka use karenge, kyuki set mai duplicate value store nhi hoti hai, to set mai store krne ke bd hume unique subject ki count mil jayegi
unique_subjects = set(subjects) #set ka use karte hue hume unique subject ki count mil jayegi
print(len(unique_subjects)) #to print the count of unique subjects, which is the number of classrooms needed




#another way to solve these question
subjects = {
    "python", "java", "c++", "python", "javascript", "c", "c++", "java", "python", "java"
} # subjects ko hi set mai store kar denge to hame unique subject ki count mil jayegi, kyuki set mai duplicate value store nhi hoti hai, to set mai store krne ke bd hume unique subject ki count mil jayegi
print(subjects) #to print the set of subjects, it will print only unique subjects in the set
print(len(subjects)) #to print the count of unique subjects, which is the number of classrooms needed