"""Write program:
Create list:
numbers = [10, 20, 30, 40, 50]
Check if 30 is present in the list
If present print:
Found
If not present print:
Not Found
Rules
Use:
in"""
numbers = [10, 20, 30, 40, 50]
num=int(input("Enter the number to be searched"))
if num in numbers:
    print("Found")
else:
    print("Not Found")