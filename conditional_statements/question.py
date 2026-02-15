# grade students based on marks obtained in an exam.
# marks>=90: Grade A
# marks>=80 and marks<90: Grade B
# marks>=70 and marks<80: Grade C
# marks>=60 and marks<70: Grade D
# marks<60: Grade F

marks = int(input("Enter the marks obtained in the examination:"))
if (marks >= 90):
    Grade = "A"
elif (marks >= 80 and marks < 90):
    Grade = "B"
elif (marks >= 70 and marks < 80):
    Grade = "C"
elif (marks >= 60 and marks < 70):
    Grade = "D"
else:
    Grade = "F"

print("grade of the students is:", Grade)