"""Write program:
Print students who scored more than 75
Example output:
Top students:
Alby : 85
John : 90"""
student_details={}
print("Enter the details of the student")
for i in range(5):
    Name=input("Enter the name of the student")
    Marks=int(input("Marks"))
    student_details[Name]=Marks
for Name,Marks in student_details.items():
    if Marks>75:
        print(Name,":",Marks)