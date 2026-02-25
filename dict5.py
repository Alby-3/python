"""Write program:
Count how many students scored more than 75
Example output:
Number of top students: 3
Rules
Must use:
dictionary
loop
counter variable
Hint (tiny)
You need something like:
count = 0"""
student_details={}
print("Enter the details of the student")
count=0;
for i in range(5):
    Name=input("Enter the  name")
    Marks=int(input("Marks"))
    student_details[Name]=Marks
for Name,Marks in student_details.items():
    if Marks>75:
        count=count+1
print(count)
