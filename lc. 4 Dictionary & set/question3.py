#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start withan emty dict & add one by one. Use sub name as key & masks as value. Finally print the dict.

marks = {} #empty dict
x = int(input("Enter marks of subject phy: ")) 
marks.update({"phy": x}) #to add key value pair in the dict, we can also use marks["phy"] = x to add key value pair in the dict
y = int(input("Enter marks of subject chem: "))
marks.update({"chem": y}) #to add key value pair in the dict, we can also use marks["chem"] = y to add key value pair in the dict
z = int(input("Enter marks of subject math: "))
marks.update({"math": z}) #to add key value pair in the dict, we can also use marks["math"] = z to add key value pair in the dict
print(marks) #to print the dict with all the key value pairs of subjects and marks 
