"""Write a program:
Store 5 students and marks.
Then print:
1️⃣ Highest mark student
Example:
Highest mark student: John : 95
Requirements
You MUST use:
dictionary
loop
if condition
NOT allowed:
max(student_details.values())"""
student_details={}
print("Enter the details of the students:")
for i in range(5):
    Name=input("Enter the name of the student")
    marks = int(input("Enter the marks of the student"))
    student_details[Name]=marks
highest_name=""
highest_mark=-1
for Name,Marks in student_details.items():
    if Marks > highest_mark:
        highest_mark=Marks
        highest_name=Name
print("Name",highest_name,"highest mark is",highest_mark)