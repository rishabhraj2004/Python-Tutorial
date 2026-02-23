#WAP to count the no of students with the "A" grade in the following tuple.
# ["C", "D", "A", "A", "B, "B", "A"]


grades = ("C", "D", "A", "A", "B", "B", "A")
print(grades.count("A")) #tuple me "A" kitni baar aata hai usko count karega




#list the above value in a list and sort them from "A"to "D"

grades_list = list(grades) #tuple ko list me convert kar diya
grades_list.sort() #list ke elements ko ascending order me sort (arrange) karega
print(grades_list)